from django.http import JsonResponse
from .serializers import PropertySerializer
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse({"properties": serializer.data})
