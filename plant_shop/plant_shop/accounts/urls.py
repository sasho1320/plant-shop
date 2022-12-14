from django.urls import path
from plant_shop.accounts.views import SignInView, SignUpView, SignOutView, dashboard_view, my_orders_view, \
    profile_edit_view, change_password_view, order_detail_view, forgot_password, reset_password_validate, reset_password

urlpatterns = [
    path('login/', SignInView.as_view(), name='login-user'),
    path('register/', SignUpView.as_view(), name='register-user'),
    path('logout/', SignOutView.as_view(), name='logout-user'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('my-orders/', my_orders_view, name='my-orders'),
    path('profile-edit/', profile_edit_view, name='profile-edit'),
    path('profile-password-change/', change_password_view, name='profile-password-change'),
    path('order-detail/<int:order_id>/', order_detail_view, name='order-detail'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('reset-password/', reset_password, name='reset-password'),
    path('reset-password-validate/<uidb64>/<token>/', reset_password_validate, name='reset-password-validate'),
]

from .signals import send_email_on_successful_sign_up
