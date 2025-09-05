import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_management.serializers import UserSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data correctly
            
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')  # Fix naming
            username = email  # Use firstname as username
            
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse(
                    {"message": "Email already exists.", "status": "error"},
                    status=400
                )

            # Validate password match
            if password != confirm_password:
                return JsonResponse(
                    {"message": "Passwords do not match.", "status": "error"},
                    status=400
                )

            # Create and save the new user
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,  # Ensure username is set
                email=email,
                password=password  # `create_user` automatically hashes the password
            )

            return JsonResponse(
                {"message": "User registered successfully!", "status": "success"},
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"message": "Invalid JSON format.", "status": "error"},
                status=400
            )

    return JsonResponse(
        {"message": "Invalid request method. POST required.", "status": "error"},
        status=405
    )