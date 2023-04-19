from . import views
from django.urls import path, include, reverse_lazy
from .views import dashboard, profile_list, profile, register
from django.contrib.auth import views as auth_views


app_name = 'social_network'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password-change/', auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy(
                'account:password_change_done')), name='password_change'),
    path('register/', register, name='register'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
