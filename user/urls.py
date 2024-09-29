from django.urls import path

from user.views import UserLoginApiView, UserLogoutApiView, UserRegisterAPIView

urlpatterns = [
    path('get-token/', UserLoginApiView.as_view()),
    path('logout/', UserLogoutApiView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),

]
