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
    path('password_change/', auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy(
                'social_network:password_change_done')), name='password_change'),
    path('register/', register, name='register'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/update', views.post_update, name='post_update'),
    path('update/updaterecord/<slug:slug', views.update_record, name='update_record'),
]
