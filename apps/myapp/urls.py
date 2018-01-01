from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time_display$', views.index),
#    url(r'^admin/', admin.site.urls),
]
