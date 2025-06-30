
class RequestTimerMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        import time
        start_time = time.time()
        method = environ.get('REQUEST_METHOD')
        path = environ.get('PATH_INFO')

        print(f"[Custom Middleware] {method} {path} - Started")

        def custom_start_response(status, headers, exc_info=None):
            duration = time.time() - start_time
            print(f"[Custom Middleware] {method} {path} - Completed in {duration:.4f}s")
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)
