from django.http.response import JsonResponse
from api.models import StreetCenterline

def index(request):
    area = StreetCenterline.closest_sidewalk.get_area(point=request.GET['point'])
    # roomba normal speed = ~1ft/1sec
    return JsonResponse({'seconds': round(area, 2), 'minutes': round(area/60, 2), 'hours': round(round(area/60, 2)/60, 2)})
