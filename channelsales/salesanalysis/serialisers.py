from rest_framework import serializers


class SelectQueryRequestSerialiser(serializers.Serializer):

    total_impressions = serializers.models.Sum(required=False)
    total_clicks = serializers.models.Sum(required=False)
    total_installs = serializers.models.Sum(required=False)
    total_revenue = serializers.models.Sum(required=False)
    total_spend = serializers.models.Sum(required=False)
    cpi = serializers.models.Avg(required=False)


class FilterQueryRequestSerialiser(serializers.Serializer):

    date = serializers.DateField(required=False)
    date__lte = serializers.DateField(required=False)
    date__gte = serializers.DateField(required=False)
    date__month = serializers.IntegerField(required=False)
    date__year = serializers.IntegerField(required=False)
    country = serializers.CharField(max_length=2, required=False)




