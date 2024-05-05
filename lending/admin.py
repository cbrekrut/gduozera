from django.contrib import admin
from .models import House, Service, ServiceImage

admin.site.register(House)

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]

admin.site.register(Service, ServiceAdmin)