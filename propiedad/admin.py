from django.contrib import admin
from propiedad.models import propiedad

# Register your models here.
@admin.register(propiedad)
class propiedadadmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']