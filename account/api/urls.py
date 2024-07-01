from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account.api.views import RegisterView


app = "account"

urlpatterns = [
    ####################### urls provided by rest_framework_simplejwt #######################
    path("login", TokenObtainPairView.as_view(), name="handler-token-obtain-pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="handler-token-refresh"),
    # #######################################################################################
    path("register", RegisterView.as_view(), name="handler-register"),
]
