"""This file contains all your helper functions, so you can avoid repetitive manipulations for validating each sub query"""
from django.db.models import Sum, Avg, Func, F


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'

def modify_search_params_to_dict(select_query):
    dict_object = dict()
    for params in select_query.split(','):
        value = params.split('_')
        if len(value) == 0:
            return None
        if len(value) == 2 and value[0].lower() == 'total':
            dict_object[params] = Sum(value[1])
        elif len(value) == 1 and value[0].lower() == 'cpi':
            dict_object['cpi'] = Round(Avg(F('spend')/F('installs')))
    return dict_object

def modify_filter_params_to_dict(query_by):

    dict_object = dict()
    for params in query_by.split(','):
        value = params.split('=')
        if len(value) != 2:
            return None
        dict_object[value[0]] = value[1]
    return dict_object

def modify_order_params_to_dict(order_by):

    order_by_list = order_by.split(',')
    if len(order_by_list) != 2:
        return ''
    if order_by_list[1] == 'asc':
        return order_by_list[0]
    elif order_by_list[1] == 'desc':
        return '-' + order_by_list[0]
    return ''

