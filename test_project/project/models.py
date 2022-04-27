from datetime import datetime
from django.db import models
import requests

# Create your models here.

class TraficRecord(models.Model):
    datetime = models.DateTimeField()
    prevision = models.IntegerField()

    def __str__(self) -> str:
        return '<%s, %s>' % (self.datetime, self.prevision)


class BordeauxAPIHandler():

    @classmethod
    def record_from_json(cls, json: dict) -> TraficRecord:
        date = datetime.fromisoformat(json['fields']['bm_heure'])
        prevision = int(json['fields']['bm_prevision'])
        return TraficRecord(datetime=date, prevision=prevision)

    @classmethod
    def records_from_json(cls, json: dict) -> list[TraficRecord]:
        return [cls.record_from_json(record) for record in json['records']]

    @classmethod
    def get_today_records(cls) -> list[TraficRecord]:
        url = 'https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193'
        records = []

        response = requests.get(url=url)
        if (response.status_code != 200):
            raise ValueError('temporary')
        
        return cls.records_from_json(response.json())
    
