from django.contrib import admin
from .models import CreditCardApplication

@admin.register(CreditCardApplication)
class CreditCardApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "dob", "employment_status", "income", "agreed_terms")
    list_filter = ("gender", "employment_status", "bank_account", "agreed_terms", "state", "country")
    search_fields = ("first_name", "last_name", "email", "ssn", "mobile_phone")
    readonly_fields = ("ssn",)  # Keeping SSN read-only for security reasons
    ordering = ("last_name", "first_name")
    fieldsets = (
        ("Personal Information", {
            "fields": ("first_name", "middle_name", "last_name", "dob", "gender", "ssn")
        }),
        ("Contact Details", {
            "fields": ("work_phone", "home_phone", "mobile_phone", "email")
        }),
        ("Address", {
            "fields": ("address1", "address2", "street", "state", "zip_code", "country")
        }),
        ("Employment", {
            "fields": ("company", "employment_status", "job_title", "employment_duration")
        }),
        ("Financial Information", {
            "fields": ("income", "bank_account", "bank_name")
        }),
        ("Preferences & Terms", {
            "fields": ("language", "agreed_terms")
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """Disable delete action in admin."""
        return False  # Prevent accidental deletions

    def has_add_permission(self, request):
        """Disable add action in admin if needed."""
        return True  # Change to False if no manual entry is allowed

