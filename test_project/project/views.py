from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.http import JsonResponse
from datetime import datetime

from project.models import BordeauxAPIHandler

# Create your views here.

def get_traffic(request):
    try:
        date = datetime.fromisoformat(request.GET['datetime'])
    except KeyError:
        raise BadRequest('datetime field is missing')
    
    records = BordeauxAPIHandler.get_today_records()
    
    closest_record = min(records, key=lambda r: abs(r.datetime - date))
    previsions = [record.prevision for record in records]
    min_prevision = min(previsions)
    max_prevision = max(previsions)
    avg_prevision = sum(previsions) / len(previsions)
    
    return JsonResponse({
        'prevision': closest_record.prevision,
        'min': min_prevision,
        'max': max_prevision,
        'avg': avg_prevision,
        'good_time': closest_record.prevision < avg_prevision
    })
