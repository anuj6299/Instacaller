import logging

from account.error_codes import ErrorCode
from common.constants import Length
from common.validate import is_phone_number_valid

logger = logging.getLogger(__name__)


def _validate_phone(request_data: dict) -> ErrorCode:
    logger.debug(f">> ARGS: {locals()}")
    if not request_data.get("phone"):
        return ErrorCode(ErrorCode.MISSING_PHONE)
    if not isinstance(request_data["phone"], str):
        return ErrorCode(ErrorCode.INVALID_PHONE_TYPE)
    if not is_phone_number_valid(phone=request_data["phone"]):
        return ErrorCode(ErrorCode.INVALID_PHONE)


def _validate_name(request_data: dict) -> ErrorCode:
    logger.debug(f">> ARGS: {locals()}")
    if not request_data.get("name"):
        return ErrorCode(ErrorCode.MISSING_NAME)
    if not isinstance(request_data["name"], str):
        return ErrorCode(ErrorCode.INVALID_NAME_TYPE)
    if len(request_data["name"]) > Length.PERSON_NAME_MAX_LENGTH:
        return ErrorCode(ErrorCode.INVALID_NAME_LENGTH)


def _validate_password(request_data: dict) -> ErrorCode:
    logger.debug(f">> ARGS: {locals()}")
    if not request_data.get("password"):
        return ErrorCode(ErrorCode.MISSING_PASSWORD)
    if not isinstance(request_data["password"], str):
        return ErrorCode(ErrorCode.INVALID_PASSWORD_TYPE)


def _validate_email(request_data: dict) -> ErrorCode:
    logger.debug(f">> ARGS: {locals()}")
    if request_data.get("email") and not isinstance(request_data["email"], str):
        return ErrorCode(ErrorCode.INVALID_EMAIL_TYPE)


def svc_validate_request_data_register_user(request_data: dict) -> ErrorCode:
    logger.debug(f">> ARGS: {locals()}")

    error = _validate_phone(request_data)
    if error:
        return error

    error = _validate_name(request_data)
    if error:
        return error

    error = _validate_password(request_data)
    if error:
        return error

    error = _validate_email(request_data)
    if error:
        return error
