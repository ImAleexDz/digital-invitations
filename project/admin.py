from django.contrib import admin
from .models import Family, Confirmation

# Register your models here.
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'tickets'
    ]

@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'tickets',
        'confirm',
        'message'
    ]