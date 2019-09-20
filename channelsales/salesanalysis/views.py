from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sales
from .serialisers import FilterQueryRequestSerialiser, SelectQueryRequestSerialiser
from .helper import modify_filter_params_to_dict, modify_search_params_to_dict, modify_order_params_to_dict


@api_view(['GET'])
def fetch_data(request):

    params = request.query_params
    select = params.get('search')
    filter_by = params.get('filterBy')
    group_by = params.get('groupBy')
    order_by = params.get('orderBy')

    if select in [None, ""] or filter_by in [None, ""]:
        return Response({"Error": "No value to be shown"}, status=400)

    select_query_objects = modify_search_params_to_dict(select)
    select_serialiser = SelectQueryRequestSerialiser(data=select_query_objects)
    if select_query_objects is None or len(select_query_objects) == 0 or not select_serialiser.is_valid():
        return Response({"Error": "Invalid data to search"}, status=400)

    filter_query_objects = modify_filter_params_to_dict(filter_by)
    filter_serialiser = FilterQueryRequestSerialiser(data=filter_query_objects)
    if filter_query_objects is None or len(filter_query_objects) == 0 or not filter_serialiser.is_valid():
        return Response({"Error": "Invalid data to filter"}, status=400)

    if group_by is not None and group_by != '':
        group_query_objects = group_by.split(',')
    else:
        group_query_objects = []

    if order_by is not None and order_by != '':
        order_by = modify_order_params_to_dict(order_by)
    else:
        order_by = ''

    query_object = dict()
    query_object['select'] = select_query_objects
    query_object['filter'] = filter_query_objects
    query_object['group'] = group_query_objects
    query_object['order'] = order_by

    data = Sales.filter_data(**query_object)
    if data is None:
        return Response(data={"Error fetching data"}, status=400)
    return Response(data=data, status=200)








