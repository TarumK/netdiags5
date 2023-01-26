from django.contrib import admin
from .models import Sector, Server, Log

# Register your models here.


admin.site.register(Sector)
admin.site.register(Server)
admin.site.register(Log)
