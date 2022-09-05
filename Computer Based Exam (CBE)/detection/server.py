import argparse
import asyncio
import json
import logging
import os
import ssl
import uuid

import cv2
from aiohttp import web
from av import VideoFrame

from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder

ROOT = os.path.dirname(__file__)

FACE_fn = os.path.join(ROOT, 'haarcascade_frontalface_default.xml')

logger = logging.getLogger('pc')
pcs = set()


# count = 0

class VideoTransformTrack(VideoStreamTrack):
    def __init__(self, track):
        super().__init__()  # don't forget this!
        self.track = track
        self.count = 0

    async def recv(self):
        frame = await self.track.recv()
        face_fn = cv2.CascadeClassifier(FACE_fn)
        img = frame.to_ndarray(format='bgr24')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_fn.detectMultiScale(gray_img, 1.1, 5)

        # if (faces[1]< 1):
        # count +=1480
        # log_info("counter" , count)
        # print(''+ count)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

        # rebuild a VideoFrame, preserving timing information
        new_frame = VideoFrame.from_ndarray(img, format='bgr24')
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame


async def index(request):
    content = open(os.path.join(ROOT, 'index.html'), 'r').read()
    return web.Response(content_type='text/html', text=content)


async def javascript(request):
    content = open(os.path.join(ROOT, 'client.js'), 'r').read()
    return web.Response(content_type='application/javascript', text=content)


async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(
        sdp=params['sdp'],
        type=params['type'])

    pc = RTCPeerConnection()
    pc_id = 'PeerConnection(%s)' % uuid.uuid4()
    pcs.add(pc)

    def log_info(msg, *args):
        logger.info(pc_id + ' ' + msg, *args)

    log_info('Created for %s', request.remote)

    # prepare local media
    # player = MediaPlayer(os.path.join(ROOT, 'demo-instruct.wav'))
    # if args.write_audio:
    #   recorder = MediaRecorder(args.write_audio)
    # else:
    #   recorder = MediaBlackhole()

    @pc.on('iceconnectionstatechange')
    async def on_iceconnectionstatechange():
        # log_info('ICE connection state is %s', pc.iceConnectionState)
        if pc.iceConnectionState == 'failed':
            await pc.close()
            pcs.discard(pc)

    @pc.on('track')
    def on_track(track):
        log_info('Track %s received', track.kind)

        # if track.kind == 'audio':
        #    pc.addTrack(player.audio)
        #   recorder.addTrack(track)
        if track.kind == 'video':
            local_video = VideoTransformTrack(track)
            pc.addTrack(local_video)

        @track.on('ended')
        async def on_ended():
            log_info('Track %s ended', track.kind)
            # await recorder.stop()

    # handle offer
    await pc.setRemoteDescription(offer)
    # await recorder.start()

    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type='application/json',
        text=json.dumps({
            'sdp': pc.localDescription.sdp,
            'type': pc.localDescription.type
        }))


async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WebRTC audio / video / data-channels demo')
    parser.add_argument('--cert-file', help='SSL certificate file (for HTTPS)')
    parser.add_argument('--key-file', help='SSL key file (for HTTPS)')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port for HTTP server (default: 8080)')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--write-audio', help='Write received audio to a file')
    args = parser.parse_args()
    #
    # if args.verbose:
    #     logging.basicConfig(level=logging.DEBUG)
    # else:
    #     logging.basicConfig(level=logging.INFO)
    #
    # if args.cert_file:
    #     ssl_context = ssl.SSLContext()
    #     ssl_context.load_cert_chain(args.cert_file, args.key_file)
    # else:
    ssl_context = None

    app = web.Application()
    app.on_shutdown.append(on_shutdown)
    app.router.add_get('/', index)
    app.router.add_get('/client.js', javascript)
    app.router.add_post('/offer', offer)
    web.run_app(app, access_log=None, port=args.port, ssl_context=ssl_context)
