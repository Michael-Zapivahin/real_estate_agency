from django.contrib import admin


from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    list_filter = ['new_building']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['price', 'new_building', 'construction_year', 'town']
    raw_id_fields = ['liked_by']
    inlines = [
        OwnerInline
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']




admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

