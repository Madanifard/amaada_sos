from django.contrib import admin
from insured.models.insured import Insured


@admin.register(Insured)
class InsuredAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
