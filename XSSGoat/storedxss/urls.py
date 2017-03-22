from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^comments/create/$', views.CommentsFormView.as_view(),
        name='comments-create'),
    url(r'^comments/$', views.CommentsListView.as_view(),
        name='comments-list'),
    url(r'^opinions/create/$', views.OpinionCreateView.as_view(),
        name='opinions-create'),
]
