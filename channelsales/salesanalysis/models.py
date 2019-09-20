from django.db import models

# Create your models here.
class Sales(models.Model):

    date =  models.DateField(null=False)
    channel = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    os = models.CharField(max_length=50, null=False)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=8, decimal_places=2)
    revenue = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'sales'