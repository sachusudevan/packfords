from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import include, path
from .views import RegisterAPIView, LoginAPIView, LogoutAllView, LogoutAPIView, RefreshTokenView

app_name = 'authentication'
 
urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('refresh/token', RefreshTokenView.as_view()),

]
