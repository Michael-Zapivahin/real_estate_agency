from django.contrib import admin
from django.conf.urls import url

from property import views

urlpatterns = [
    url(r'^$', views.show_flats),
    url(r'^search/$', views.show_flats),
    url(r'^admin/', admin.site.urls),
]
