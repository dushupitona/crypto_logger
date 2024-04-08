from django.db import models
from django import forms

# Create your models here.

class BTCUSD_info_model(models.Model):
    log_date = models.DateTimeField()
    last_price = models.DecimalField(max_digits=12, decimal_places=2)
    index_price = models.DecimalField(max_digits=12, decimal_places=2)
    mark_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.log_date)
