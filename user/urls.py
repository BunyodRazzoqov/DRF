from django.urls import path

from user.views import UserLoginApiView, UserLogoutApiView

urlpatterns = [
    path('get-token/', UserLoginApiView.as_view()),
    path('logout/', UserLogoutApiView.as_view()),

]
