from django.urls import path

from home.views import index, list_customers, delete_customer, create_customer_form,  create_customer, find, update  #feedback

urlpatterns = [
    # path(r'feedback', feedback, name='feedback_url'),
    path(r'', index, name='index'),

    path('customers', list_customers, name='customers_list_url'),
    path('customer/<customerId>/delete', delete_customer, name='delete_customer_url'),

    path('customer/form/create', create_customer_form, name='create_customer_form'),
    path('customer/create', create_customer, name='create_customer'),

    path('customer/<int:customer_id>', find, name='find_customer'),

    path('customer/<int:customer_id>/update', update, name='update_customer'),
]