from django.db import models

# Create your models here.

class BTCUSD_info_model(models.Model):
    last_price = models.DecimalField(max_digits=12, decimal_places=2)
    index_price = models.DecimalField(max_digits=12, decimal_places=2)
    mark_price = models.DecimalField(max_digits=12, decimal_places=2)