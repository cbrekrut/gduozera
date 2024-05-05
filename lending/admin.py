from django import forms
from django.contrib import admin
from .models import House, Service, ServiceImage

admin.site.register(House)

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceForm(forms.ModelForm):
     class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 100}),
        }

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]
    form = ServiceForm

admin.site.register(Service, ServiceAdmin)

