from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from recipes.models import Recipe

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/recipes/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipes/', include('recipes.urls')),
]
