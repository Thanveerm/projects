from django.db import models

class Inerg(models.Model):
    API_WELL_NUMBER = models.CharField(max_length=200)
    PRODUCTION_YEAR = models.CharField(max_length=100)
    QUARTER = models.CharField(max_length=100)
    OWNER_NAME = models.CharField(max_length=200)
    COUNTRY = models.CharField(max_length=200)
    TOWNSHIP = models.CharField(max_length=200)
    WELL_NAME = models.CharField(max_length=200)
    WELL_NUMBER =models.CharField(max_length=100)
    OIL = models.CharField(max_length=100)
    GAS = models.CharField(max_length=100)
    BRINE = models.CharField(max_length=100)
    DAYS = models.CharField(max_length=100)


    def __str__(self):
            return self.COUNTRY
