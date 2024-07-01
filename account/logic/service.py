import logging

from account.error_codes import ErrorCode
from account.models import User
from django.core.exceptions import ObjectDoesNotExist

from contacts.logic.service import svc_create_contact

logger = logging.getLogger(__name__)


def svc_register_user(request_data: dict) -> tuple[ErrorCode, User]:
    """
    Service function to register user
        1. Check if user already exist. If already exist, return error.
        2. Create user and return user.
    """
    logger.debug(f">> ARGS: {locals()}")

    try:
        user = User.objects.get(phone=request_data["phone"])
        return ErrorCode(ErrorCode.USER_ALREADY_EXIST), None
    except ObjectDoesNotExist:
        user = User.objects.create_user(
            phone=request_data["phone"],
            password=request_data["password"],
            name=request_data["name"],
            email=request_data.get("email", ""),
        )
        svc_create_contact(
            name=request_data["name"],
            phone=request_data["phone"],
            email=request_data.get("email"),
            owner=user,
        )
    return None, user
