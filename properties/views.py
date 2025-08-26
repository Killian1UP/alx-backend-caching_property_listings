from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .serializers import PropertySerializer

# Cache for 15 minutes (60*15 seconds)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse(serializer.data, safe=False)
