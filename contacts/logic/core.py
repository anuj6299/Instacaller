"""
Views will call only these core functions
No code logic here - Only call functions
"""

import logging, uuid
from typing import Union

# imports from common module
from common.validate import is_phone_number_valid

# imports from current module
from contacts.api.serializers import ContactListWithSpamSerializer
from contacts.error_codes import ErrorCode
from contacts.logic.service import (
    svc_get_contact_by_id,
    svc_mark_phone_spam,
    svc_search_contact_by_name,
    svc_search_contact_by_phone,
)
from contacts.models import Contact

# imports from other modules
from account.models import User


logger = logging.getLogger(__name__)


def svc_contacts_search_contact_by_name(
    search_query: str,
    serialize: bool = False,
) -> tuple[ErrorCode, Union[list[Contact], list[dict]]]:
    """
    Core function to search contacts by name
    """
    logger.debug(f">> ARGS: {locals()}")

    error, contacts = svc_search_contact_by_name(search_query)
    if error:
        return error, None

    if serialize:
        contacts = ContactListWithSpamSerializer(contacts, many=False).data

    return ErrorCode(ErrorCode.SUCCESS), contacts


def svc_contacts_search_contact_by_phone(
    search_query: str, serialize: bool = False
) -> tuple[ErrorCode, Union[list[Contact], list[dict]]]:
    """
    Core function to search contacts by phone
    """
    logger.debug(f">> ARGS: {locals()}")

    if not is_phone_number_valid(phone=search_query):
        return ErrorCode(ErrorCode.INVALID_PHONE), None

    error, contacts = svc_search_contact_by_phone(search_query)
    if error:
        return error, None

    if serialize:
        contacts = ContactListWithSpamSerializer(contacts, many=False).data

    return ErrorCode(ErrorCode.SUCCESS), contacts


def svc_contacts_get_contact_by_id(
    contact_id: uuid, user: User, serialize: bool = False
) -> tuple[ErrorCode, Union[dict, Contact]]:
    """
    Core function to get contact details by contact_id
    """
    logger.debug(f">> ARGS: {locals()}")
    error, contact = svc_get_contact_by_id(contact_id=contact_id)
    if error:
        return error, None

    if serialize:
        contact = {
            **ContactListWithSpamSerializer(contact, many=False).data,
            "email": (
                contact.email
                if User.objects.filter(phone=contact.phone).exists()
                and Contact.objects.filter(owner=user, phone=contact.phone).exists()
                else None
            ),
        }

    return ErrorCode(ErrorCode.SUCCESS), contact


def svc_contacts_mark_phone_spam(phone: str, spammed_by: User) -> ErrorCode:
    """
    Core function to mark phone spam
    """
    logger.debug(f">> ARGS: {locals()}")

    if not is_phone_number_valid(phone=phone):
        return ErrorCode(ErrorCode.INVALID_PHONE)

    error, _ = svc_mark_phone_spam(phone=phone, spammed_by=spammed_by)
    if error:
        return error

    return ErrorCode(ErrorCode.SUCCESS)
