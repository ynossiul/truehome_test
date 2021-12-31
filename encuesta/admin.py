from django.contrib import admin
from encuesta.models import encuesta


# Register your models here.
@admin.register(encuesta)
class propiedad_admin(admin.ModelAdmin):
    list_display = ('activity',)
    list_filter = ('activity',)
    search_fields = ['activity']