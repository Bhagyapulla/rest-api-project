from rest_framework.views import APIView
from rest_framework.response import Response
class TokenWelcomeView(APIView):
    def get(self,request):
        return Response({"message":f"Welcome,{request.user.username}!This is a token-protected view."})
