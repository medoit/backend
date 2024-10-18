from django.contrib import admin
from .models import *

@admin.register(Snls)
class SnslAdmin(admin.ModelAdmin):
    list_display = ('id', 'pan', 'serias')

@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_sub', 'serias', 'since_formatted', 'till_formatted', 'sale_date_formatted', 'pan')
    search_fields = ['pan']

    def since_formatted(self, obj):
         return obj.since.strftime("%Y-%m-%d %H:%M")
    since_formatted.short_description = "Дата начала действия"

    def till_formatted(self, obj):
         return obj.till.strftime("%Y-%m-%d %H:%M")
    till_formatted.short_description = "Дата окончания действия"

    def sale_date_formatted(self, obj):
         return obj.sale_date.strftime("%Y-%m-%d %H:%M:%S")
    sale_date_formatted.short_description = "Дата добавления"

admin.site.register(Terminal)
admin.site.register(Transaction)