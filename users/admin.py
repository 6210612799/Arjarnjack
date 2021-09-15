from django.contrib import admin

# Register your models here.
from .models import Couses, Nisit


class CousesAdmin(admin.ModelAdmin):
    list_display = ("id","subject","term","couseid","num_student","year",)


class NisitAdmin(admin.ModelAdmin):
    filter_horizontal = ("couses",)
admin.site.register(Couses , CousesAdmin)
admin.site.register(Nisit , NisitAdmin)