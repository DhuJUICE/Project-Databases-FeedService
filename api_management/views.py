from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

#User management functionality imports
from user_management.views import *

#API ENDPOINT FOR SIGNUP/REGISTER
class Feed(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Call the regular function
        response = feed_view(request)

        # If the other function returns a JsonResponse, return its content as JSON
        if isinstance(response, JsonResponse):
            # Deserialize the content if it's a JsonResponse
            return JsonResponse(json.loads(response.content), status=response.status_code)

        # Handle other response types if necessary
        return JsonResponse({"error": "Unexpected response type"}, status=500)