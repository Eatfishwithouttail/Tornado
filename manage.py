from  app import make_app
from tornado import options
from tornado.ioloop import IOLoop
from tornado.options import define




if __name__ == '__main__':
    define('port', default=8000, type=int, help="you server port ")
    define('host', default='0.0.0.0', type=str, help='host name')
    options.parse_command_line()

    app = make_app(options.options.host)
    app.listen(options.options.port)

    print("starting web server http://%s:%s" % (options.options.host, options.options.port))
    IOLoop.current().start()
