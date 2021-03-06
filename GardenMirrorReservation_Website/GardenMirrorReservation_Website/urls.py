"""GardenMirrorReservation_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# To allow media files to be inserted
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include # added include
from django.contrib import admin
from home import views as hviews # to remove after rtest is complete
# django rest framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', hviews.UserViewSet)
router.register(r'profileinfo', hviews.UserProfileInfoViewSet)
# router.register(r'ionicregister', hviews.ionicregister)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',hviews.index,name="index"),
    url(r'^home/',include('home.urls')),
    url(r'^special/',hviews.special,name="special"),
    url(r'^rtest/',hviews.rtest,name="rtest"),
    url(r'^ionicregister/',hviews.ionicregister,name="ionicregister"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

