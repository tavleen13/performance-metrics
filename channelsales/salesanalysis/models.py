from django.db import models


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

    @classmethod
    def filter_data(cls, **kwargs):

        filter_fields = kwargs.get('filter')
        select_fields = kwargs.get('select')
        group_fields = kwargs.get('group')
        order_fields = kwargs.get('order')

        # A generic query to do select, filter, group by and order by operations
        try:
            objs = cls.objects.filter(**filter_fields).values(*group_fields).annotate(**select_fields).order_by(order_fields)
            return objs
        except Exception:
            return None

