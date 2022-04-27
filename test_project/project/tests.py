from datetime import datetime
from django.test import TestCase

from project.models import BordeauxAPIHandler

# Create your tests here.

class APIHandlerTest(TestCase):
    def test_record_from_json(self):
        bm_heure = '2022-04-27T04:00:00+00:00'
        bm_prevision = 10
        
        json = { 'fields': { 'bm_heure': bm_heure, 'bm_prevision': bm_prevision } }
        record = BordeauxAPIHandler.record_from_json(json)

        assert(record.prevision == bm_prevision)
        assert(record.datetime == datetime.fromisoformat(bm_heure))
    
    def test_get_today_records(self):
        pass
