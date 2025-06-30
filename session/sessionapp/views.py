from rest_framework.views import APIView
from rest_framework.response import Response

class SessionWelcomeView(APIView):
    def get(self,request):
        return Response({"message":f"Hello,{request.user.username}.you are logged in using session Authentication."})

