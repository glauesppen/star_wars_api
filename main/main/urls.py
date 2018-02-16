from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import RedirectView

urlpatterns = [
    url('admin/', admin.site.urls),
    # Redirect / to api planets
    url(r'^$', RedirectView.as_view(url='/api/planets/')),
    # API Planets URLS
    url('api/', include('planet.urls')),
]