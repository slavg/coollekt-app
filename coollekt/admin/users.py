from django.contrib import admin

from coollekt.models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
