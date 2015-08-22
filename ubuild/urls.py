from django.conf.urls import include, url


urlpatterns = [
    url(r'^display/$', 'ubuild.views.display'),
    url(r'^create/$', 'ubuild.views.create'),
]