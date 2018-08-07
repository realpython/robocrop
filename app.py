import logging

import envconfig
import tornado

from pilbox.app import (
    logger,
    options,
    parse_command_line,
    PilboxApplication,
)


# This is based on https://github.com/agschwender/pilbox/
# blob/342c3460a177f0cf23325025d6227a58fba38de2/pilbox/app.py#L346-L357
# but makes the number of Tornado workers configurable via the
# WEB_CONCURRENCY env var
def start_server(app=None):
    if options.debug:
        logger.setLevel(logging.DEBUG)
    server = tornado.httpserver.HTTPServer(
        app if app else PilboxApplication())
    logger.info("Starting server...")
    try:
        server.bind(options.port)
        server.start(1 if options.debug else envconfig.int('WEB_CONCURRENCY'))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    parse_command_line()
    start_server()
