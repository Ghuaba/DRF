from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    """
    A simple API view to handle tasks.
    """
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.
        """
        #data = {"message": "This is a GET request"}
        #return Response(data)
        return Response("hOLA POOL")

    def post(self, request):
        """
        Handle POST requests.
        """
        data = {"message": "This is a POST request", "data": request.data}
        return Response(data)