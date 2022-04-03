from django.urls import path
from .views.user import create_user, get_user_by_token, login, logout, user_state

urlpatterns = [
    # user
    path('user/create/', create_user, name='create_user'),
    path('user/login/', login, name="login"),
    path('user/profile/', get_user_by_token, name="get_user_by_token"),
    path('user/logout/', logout, name="logout"),
    path('user/state/', user_state, name="user_state"),
    
    # 
    
]