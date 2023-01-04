from django.contrib import admin
from .models import Family, Confirmation, Bf_Family, Friends

# Register your models here.
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'tickets'
    ]

@admin.register(Bf_Family)
class Bf_FamilyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'tickets'
    ]

@admin.register(Friends)
class Friends_FamilyAdmin(admin.ModelAdmin):
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