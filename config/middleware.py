import time


class RequestTimingMiddleware:
    """Measure how long Django takes to answer each request."""

    def __init__(self, get_response):
        # Runs only ONCE, when the server starts.
        self.get_response = get_response

    def __call__(self, request):
        # 1) Code here runs BEFORE the view (on the way in).
        start = time.perf_counter()

        # 2) Pass the request on to the next middleware, and finally the view.
        response = self.get_response(request)

        # 3) Code here runs AFTER the view (on the way out).
        duration_ms = (time.perf_counter() - start) * 1000
        response["X-Response-Time-ms"] = f"{duration_ms:.1f}"
        print(f"[timing] {request.method} {request.path} took {duration_ms:.1f} ms")

        return response
