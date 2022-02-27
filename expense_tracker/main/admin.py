from django.contrib import admin

from expense_tracker.main.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Expense)
class ProfileAdmin(admin.ModelAdmin):
    pass
