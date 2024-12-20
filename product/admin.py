from django.contrib import admin
from .models import items
class itemsAdmin(admin.ModelAdmin):
    list_display=("name","image","price","description")


admin.site.register(items,itemsAdmin)   
# Register your models here.
