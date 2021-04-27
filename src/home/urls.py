
from django.urls import path

from home.views import index, query, result, dateshow

urlpatterns = [
    path(r'', result, name='result'),
    path(r'dateshow/', dateshow, name='dateshow'),
    # path(r'query/', query),
]