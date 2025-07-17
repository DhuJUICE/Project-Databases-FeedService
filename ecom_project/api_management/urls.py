from django.urls import path
from . import views


#token view imports
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
	#default homepage load
	path('', views.defaultHomePage, name='defaultHomePage'),

	#Used for logging users in - No need for the login endpoint
	path('api/token', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),

	#USER MANAGEMENT API ENDPOINTS
	path('api/register', views.Register.as_view(), name='api-register'),

	#PROJECT MANAGEMENT API ENDPOINTS
	path('api/project', views.ProjectManagement.as_view(), name='project-management'),
	path('api/project/<int:pk>', views.ProjectManagement.as_view(), name='project-management-with-id'),

	#client management endpoint
	path('api/client', views.ClientManagement.as_view(), name='client-management'),
	# GET MEMBER count
	#path('api/member/count', views.MemberCount.as_view(), name='member-count'),  

]
