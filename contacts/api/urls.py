from django.urls import path
from contacts.api.views import (
    ContactDetailView,
    ContactNameSearchView,
    ContactPhoneSearchView,
    MarkPhoneSpamView,
)


app = "contacts"

urlpatterns = [
    path(
        "search/name/<str:search_query>",
        ContactNameSearchView.as_view(),
        name="handler-contact-search-by-name",
    ),
    path(
        "search/phone/<str:search_query>",
        ContactPhoneSearchView.as_view(),
        name="handler-contact-search-by-phone",
    ),
    path(
        "<uuid:contact_id>",
        ContactDetailView.as_view(),
        name="handler-contact-detail",
    ),
    path(
        "spam/<str:phone>",
        MarkPhoneSpamView.as_view(),
        name="handler-mark-phone-spam",
    ),
]
