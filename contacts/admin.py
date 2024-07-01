from django.contrib import admin
from common.history_view_admin import HistoryViewAdmin
from contacts.models import Contact, Spam


class ContactAdmin(admin.ModelAdmin):
    list_display = ("phone", "name", "email", "owner")
    # TODO: is ordering needed in admin panel?
    ordering = ("-pk",)

    # override
    object_history_template = "custom_history_template.html"
    history_view = HistoryViewAdmin.history_view


admin.site.register(Contact, ContactAdmin)


class SpamAdmin(admin.ModelAdmin):
    list_display = ("phone", "spammed_by")
    # TODO: is ordering needed in admin panel?
    ordering = ("-pk",)

    # override
    object_history_template = "custom_history_template.html"
    history_view = HistoryViewAdmin.history_view


admin.site.register(Spam, SpamAdmin)
