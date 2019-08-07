

class NewMiddlewares(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("*****************************")
        print("Initializing the middlewares.")
        print("*****************************")

    def __call__(self, request):
        print("*****************************")
        print("WE ARE IN THE REQUEST PHASE  ")
        print("*****************************")
        return self.get_response(request)

    def process_request(self,request):

        print("Print the request string.")
        print(request)

    def process_exception(self, request, exception):
        print("ERROR Occured")