"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.authtoken import views
from config import custom_obtain_token
from config import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config.jwt_views import MyTokenObtainPairView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('book/', include('book.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('olcha/', include('olcha.urls')),
                  path('users/', include('user.urls')),
                  path('api-token-auth/', custom_obtain_token.CustomAuthToken.as_view()),
                  path('api/token/access/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('post/', include('post.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
