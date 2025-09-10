import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .neo4j_utils import get_personalized_feed

@csrf_exempt
def feed_view(request):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            
            if not username:
                return JsonResponse(
                    {"message": "Username is required.", "status": "error"},
                    status=400
                )
            
            # Get the personalized feed from Neo4j
            feed = get_personalized_feed(username)
            
            return JsonResponse(
                {"message": "Feed fetched successfully!", "status": "success", "feed": feed},
                status=200
            )
            
        except json.JSONDecodeError:
            return JsonResponse(
                {"message": "Invalid JSON format.", "status": "error"},
                status=400
            )
    
    return JsonResponse(
        {"message": "Invalid request method. GET required.", "status": "error"},
        status=405
    )
