from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    path('profile/', views.ProfileView, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_email.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
    
]
