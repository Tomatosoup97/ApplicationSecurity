from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^csp/', include('CSP.urls', namespace='csp')),
    url(r'^user-welcome/', include('xssheader.urls', namespace='xssheader')),
    url(r'^events/', include('sql_inj.urls', namespace='events')),
    url(r'^dom/', include('domxss.urls', namespace='dom')),
    url(r'^cookies/', include('cookies.urls', namespace='cookies')),
    url(r'^', include('storedxss.urls', namespace='storedxss')),
    url(r'^', include('core.urls', namespace='core')),
]
