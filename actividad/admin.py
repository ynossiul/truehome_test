from django.contrib import admin
from actividad.models import actividad

# Register your models here.
@admin.register(actividad)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ['title']