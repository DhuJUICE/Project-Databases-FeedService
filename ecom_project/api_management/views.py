from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from project_management.models import PROJECT
from .serializers import ProjectSerializer
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

#default page to make uptime robot get to a live section
def defaultHomePage(request):
    return render(request, 'defaultPage.html')

from client_management.models import CLIENT
from .serializers import ClientSerializer

#Client management endpoint to get and add clients to the database
class ClientManagement(APIView):
    permission_classes = [AllowAny]  # Change to IsAuthenticated if needed

    def get(self, request, *args, **kwargs):
        clients = CLIENT.objects.all().order_by('name')  # Sorted alphabetically
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Optionally add POST for creating clients here
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API ENDPOINT FOR HANDLING PROJECT CREATION, UPDATES, READS, AND DELETES
class ProjectManagement(APIView):
    permission_classes = [AllowAny]  # Change to IsAuthenticated if needed

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                project = PROJECT.objects.get(pk=pk)

                print("Below is the project\n")
                print(project)

            except PROJECT.DoesNotExist:
                return JsonResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProjectSerializer(project)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        projects = PROJECT.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            project = PROJECT.objects.get(pk=pk)
        except PROJECT.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            project = PROJECT.objects.get(pk=pk)
        except PROJECT.DoesNotExist:
            return JsonResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return JsonResponse({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


#User management functionality imports
from user_management.views import *

#API ENDPOINT FOR SIGNUP/REGISTER
class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Call the regular function
        response = register_view(request)

        # If the other function returns a JsonResponse, return its content as JSON
        if isinstance(response, JsonResponse):
            # Deserialize the content if it's a JsonResponse
            return JsonResponse(json.loads(response.content), status=response.status_code)

        # Handle other response types if necessary
        return JsonResponse({"error": "Unexpected response type"}, status=500)