from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.views import CustomObtainTokenPairView, UserCrudView, ChangePasswordView

urlpatterns = [
    path("", UserCrudView.as_view(), name="user-crud"),
    path("token/", CustomObtainTokenPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path(
        "password-reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
