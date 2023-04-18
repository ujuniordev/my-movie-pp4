from . import views
from django.urls import path, include
from .views import dashboard, profile_list, profile, register


app_name = 'social_network'

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
