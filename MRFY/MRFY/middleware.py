class BrewCoffeeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.POST.get('http_method') == 'BREW':
            request.brew_method = True
        else:
            request.brew_method = False
        response = self.get_response(request)
        return response
