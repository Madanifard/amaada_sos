from django.contrib import admin
from .models.insurance_policy import InsurancePolicy


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ('person', 'insurance', 'insured', 'start_date',
                    'end_date', 'unique_id', 'confirmed_at', 'created_at', 'updated_at')
    search_fields = ('person__first_name', 'person__last_name',
                     'insurance__name', 'insured__name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
