#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
async web application.
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body='hello world')


@asyncio.coroutine
def init(looper):
    app = web.Application(loop=looper)
    app.router.add_route('GET', '/', index)
    srv = yield from looper.create_server(app.make_handler(), '127.0.0.1', 9001)
    logging.info('server started at http://127.0.0.1:9001...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()