from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url('api/', include('planet.urls')),
]