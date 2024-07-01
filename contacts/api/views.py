from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from common.response import get_paginated_response, get_standard_response
from contacts.logic.core import (
    svc_contacts_get_contact_by_id,
    svc_contacts_mark_phone_spam,
    svc_contacts_search_contact_by_name,
    svc_contacts_search_contact_by_phone,
)
from contacts.api.serializers import ContactListWithSpamSerializer


class ContactNameSearchView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, search_query):
        try:
            error, contacts = svc_contacts_search_contact_by_name(
                search_query=search_query, serialize=False
            )
            return get_paginated_response(
                self, error, contacts, ContactListWithSpamSerializer
            )
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ContactPhoneSearchView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, search_query):
        try:
            error, contacts = svc_contacts_search_contact_by_phone(
                search_query=search_query
            )
            return get_paginated_response(
                self, error, contacts, ContactListWithSpamSerializer
            )
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ContactDetailView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, contact_id):
        try:
            error, contact = svc_contacts_get_contact_by_id(
                contact_id=contact_id, user=request.user, serialize=True
            )
            return get_standard_response(error, contact)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MarkPhoneSpamView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, phone):
        try:
            error = svc_contacts_mark_phone_spam(phone=phone, spammed_by=request.user)
            return get_standard_response(error, None)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
