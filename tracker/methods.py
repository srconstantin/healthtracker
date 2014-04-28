from django.db import models
from tracker.models import Daily, Food, Activity, Medication, Supplement
import datetime

def CreateDaily(energy):
    d = Daily(date = datetime.datetime.now(), energylevel = energy)
    d.save()

