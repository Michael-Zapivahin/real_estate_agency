from django.contrib import admin


from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    list_filter = ['new_building']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['price', 'new_building', 'construction_year', 'town']
    raw_id_fields = ["liked_by"]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

