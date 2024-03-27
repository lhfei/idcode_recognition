from django.contrib import admin

from .models import IDCode

# Register your models here.

class IDCodeApiAdmin(admin.ModelAdmin):
    list_display = ('recognition', 'content', 'img_url', 'created')
    model = IDCode
    list_per_page = 10
    
admin.site.register(IDCode, IDCodeApiAdmin)