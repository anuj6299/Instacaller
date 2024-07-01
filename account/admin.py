from django.contrib import admin
from common.history_view_admin import HistoryViewAdmin
from account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("phone", "name", "email")
    # TODO: is ordering needed in admin panel?
    ordering = ("-pk",)

    # override
    object_history_template = "custom_history_template.html"
    history_view = HistoryViewAdmin.history_view


admin.site.register(User, UserAdmin)
