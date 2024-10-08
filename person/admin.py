from django.contrib import admin
from .models.person import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number',
                    'national_code', 'birth_date', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email',
                     'national_code', 'mobile_number')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
