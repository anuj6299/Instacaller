import logging, uuid
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

# imports from current module
from contacts.error_codes import ErrorCode
from contacts.models import Contact, Spam

# imports from other modules
from account.models import User


logger = logging.getLogger(__name__)


def svc_mark_phone_spam(phone: str, spammed_by: User = None) -> tuple[ErrorCode, Spam]:
    """
    Service function to mark a phone number spam
    """
    logger.debug(f">> ARGS: {locals()}")
    try:
        spam = Spam.objects.create(phone=phone, spammed_by=spammed_by)
    except IntegrityError:
        return ErrorCode(ErrorCode.PHONE_ALREADY_SPAMMED), None
    return None, spam


def svc_create_contact(
    name: str, phone: str, email: str = None, owner: User = None
) -> Contact:
    """
    Service function to create contact
    """
    logger.debug(f">> ARGS: {locals()}")
    contact = Contact.objects.create(name=name, phone=phone, email=email, owner=owner)
    return contact


def svc_get_contact_by_id(
    contact_id: uuid,
) -> tuple[ErrorCode, Contact]:
    """
    Service function to get contact by id
    """
    logger.debug(f">> ARGS: {locals()}")
    try:
        contact = Contact.objects.get(external_id=contact_id)
    except ObjectDoesNotExist:
        return ErrorCode(ErrorCode.CONTACT_DOES_NOT_EXIST), None
    return None, contact


def svc_search_contact_by_name(search_query: str) -> tuple[ErrorCode, list[Contact]]:
    """
    Service function to search contact by name
    """
    logger.debug(f">> ARGS: {locals()}")

    return None, Contact.objects.filter(name__startswith=search_query).order_by(
        "-pk"
    ) | Contact.objects.filter(name__icontains=search_query).order_by("-pk")


def svc_search_contact_by_phone(
    search_query: str,
) -> tuple[ErrorCode, list[Contact]]:
    """
    Service function to search contact by phone
        1. If user found with the phone, return contact details saved by this user
        2. If user not found with the phone, return all contacts with that phone
    """
    logger.debug(f">> ARGS: {locals()}")

    try:
        user = User.objects.get(phone=search_query)
        contacts = Contact.objects.filter(owner=user, phone=search_query).order_by(
            "-pk"
        )
    except ObjectDoesNotExist:
        contacts = Contact.objects.filter(phone=search_query).order_by("-pk")
    return None, contacts
