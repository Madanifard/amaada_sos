from django.contrib import admin
from insurance.models.insurance import Insurance
from insurance.models.insured import Insured
from insurance.models.plan import Plan
from insurance.models.person import Person
from insurance.models.insurance_policy import InsurancePolicy


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number',
                    'national_code', 'birth_date', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email',
                     'national_code', 'mobile_number')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Insured)
class InsuredAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id', 'created_at', 'updated_at')
    search_fields = ('name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ('person', 'insurance', 'insured', 'start_date',
                    'end_date', 'unique_id', 'confirmed_at', 'created_at', 'updated_at')
    search_fields = ('person__first_name', 'person__last_name',
                     'insurance__name', 'insured__name', 'unique_id')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
