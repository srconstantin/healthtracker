from django.db import models


class Daily(models.Model):
    date = models.DateField()
    energylevel = models.IntegerField()
    def __unicode__(self):
        return str(self.date)
    

class Food(models.Model):
    food = models.CharField(max_length=200)
    day = models.ForeignKey(Daily)
    quantity = models.FloatField()
    def __unicode__(self):
        return self.food

class Activity(models.Model):
    activity = models.CharField(max_length=200)
    day = models.ForeignKey(Daily)
    quantity = models.FloatField()
    def __unicode__(self):
        return self.activity

class Medication(models.Model):
    medication = models.CharField(max_length=200)
    day = models.ForeignKey(Daily)
    quantity = models.FloatField()
    def __unicode__(self):
        return self.medication

class Supplement(models.Model):
    supplement = models.CharField(max_length=200)
    day = models.ForeignKey(Daily)
    quantity = models.FloatField()
    def __unicode__(self):
        return self.supplement


    
