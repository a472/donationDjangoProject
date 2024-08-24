from django.contrib import admin

from .models import Donor, Donations, PhoneNumberField
# Register your models here.

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'village')
    search_fields = ('first_name', 'last_name')


@admin.register(Donations)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'amount', 'donation_date')
    list_filter = ('donation_date',)
    search_fields = ('donor__first_name', 'donor__last_name')


