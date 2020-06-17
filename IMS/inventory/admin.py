from django.contrib import admin
from inventory.models import *

# Register your models here.
@admin.register(Desktop,Laptop,Mobile)
class ViewAAdmin(admin.ModelAdmin):
    pass
