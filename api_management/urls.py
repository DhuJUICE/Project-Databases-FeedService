from django.urls import path
from . import views

#token view imports
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	#USER MANAGEMENT API ENDPOINTS
	path('api/feed', views.Feed.as_view(), name='api-feed'),
]
