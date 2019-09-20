from django.db import models
from django.db.models import Avg, Sum, F, Func

# Create your models here.

"""
USECASE1 : cls.objects.filter(date__lte='2017-06-01').values('channel', 'country').annotate(total_impressions=Sum('impressions'),
                                                                total_clicks=Sum('clicks')).order_by('-total_clicks')
                                                                
USECASE2: cls.objects.filter(date__month=5, date__year=2017, os='ios').values('date').annotate(total_installs=Sum('installs')).order_by('date')

USECASE3: cls.objects.filter(date='2017-06-01', country='US').values('os').annotate(total_revenue=Sum('revenue')).order_by('-total_revenue')

USECASE4 : cls.objects.filter(country='CA').values('channel').annotate(CPI=cls.Round(Avg(F('spend')/F('installs'))), total_spend=Sum('spend')).order_by('-CPI')                                                          
                                                                """
class Sales(models.Model):

    date = models.DateField(null=False)
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

    class Round(Func):
        function = 'ROUND'
        template = '%(function)s(%(expressions)s, 2)'

    @classmethod
    def filter_data(cls, **kwargs):
        filter_fields = kwargs.get('filter')
        select_fields = kwargs.get('select')
        group_fields = kwargs.get('group')
        order_fields = kwargs.get('order')
        try:
            objs = cls.objects.filter(**filter_fields).values(*group_fields).annotate(**select_fields).order_by(order_fields)
            return objs
        except Exception:
            return None

