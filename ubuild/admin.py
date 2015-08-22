from django.contrib import admin
from .models import logs,urls
# Register your models here.
admin.autodiscover()
admin.site.register(logs)
admin.site.register(urls)