from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^users', views.get_users, name='users'),
]
