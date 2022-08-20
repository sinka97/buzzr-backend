from django.urls import path

from .views.merchant import create_merchant
from .views.user import create_user, get_user_by_token, login, logout, user_state
from .views.test import test_webpage
from .views.order import accept_queue,change_status,query_status,get_orders_of_merchant,get_orders_of_merchant_specific_status

urlpatterns = [
    # user
    path('user/create/', create_user, name='create_user'),
    path('user/login/', login, name="login"),
    path('user/profile/', get_user_by_token, name="get_user_by_token"),
    path('user/logout/', logout, name="logout"),
    path('user/state/', user_state, name="user_state"),
    
    # test webpage
    path('test/webpage', test_webpage, name='test_webpage'),
    
    # queue
    path('queue/create',accept_queue,name="accept_queue"),
    path('queue/update',change_status,name="change queue status"),
    path('queue/check-status',query_status,name="check status of order"),
    
    # merchant
    path('merchant/create',create_merchant,name="create_merchant"),
    
    # merchant-order
    path('merchant/get-orders',get_orders_of_merchant,name="get orders of merchant"),
    path('merchant/get-orders-with-status',get_orders_of_merchant_specific_status,name="get orders of merchant with specific status"),
    
]