from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def fetch_data(request):

    params = request.query_params
    filter_by = params.get('filterBy')
    group_by = params.get('groupBy')
    order_by = params.get('orderBy')

