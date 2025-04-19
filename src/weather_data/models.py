from django.db import models

class WeatherRecord(models.Model):
    year = models.IntegerField(primary_key=True)
    jan = models.FloatField(null=True, blank=True)
    feb = models.FloatField(null=True, blank=True)
    mar = models.FloatField(null=True, blank=True)
    apr = models.FloatField(null=True, blank=True)
    may = models.FloatField(null=True, blank=True)
    jun = models.FloatField(null=True, blank=True)
    jul = models.FloatField(null=True, blank=True)
    aug = models.FloatField(null=True, blank=True)
    sep = models.FloatField(null=True, blank=True)
    oct = models.FloatField(null=True, blank=True)
    nov = models.FloatField(null=True, blank=True)
    dec = models.FloatField(null=True, blank=True)

 
    win = models.FloatField(null=True, blank=True)   
    spr = models.FloatField(null=True, blank=True)   
    sum = models.FloatField(null=True, blank=True)   
    aut = models.FloatField(null=True, blank=True)   
    ann = models.FloatField(null=True, blank=True)   

    class Meta:
        db_table = "weather_record"
        ordering = ['year']

    def __str__(self):
        return f"Weather Record for {self.year}"

