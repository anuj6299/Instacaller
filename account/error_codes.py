import logging

from common.constants import Length, ModuleErrorPrefix
from common.base_error_code import BaseErrorCode
from rest_framework import status

logger = logging.getLogger(__name__)


class ErrorCode(BaseErrorCode):
    INVALID_PHONE_TYPE = "001"
    INVALID_PHONE = "002"
    INVALID_NAME_TYPE = "003"
    INVALID_NAME_LENGTH = "004"
    INVALID_PASSWORD_TYPE = "005"
    # TODO: Requirement for password validation was not mentioned in the doc, so have not added here,
    # but can add similar error codes for all password validations like below -
    # INVALID_PASSWORD_LENGTH = "00X"
    INVALID_EMAIL_TYPE = "006"

    MISSING_NAME = "101"
    MISSING_PHONE = "102"
    MISSING_PASSWORD = "103"

    USER_ALREADY_EXIST = "201"

    ERROR_CODE_HTTP_MAP = {
        INVALID_NAME_LENGTH: status.HTTP_400_BAD_REQUEST,
        INVALID_NAME_TYPE: status.HTTP_400_BAD_REQUEST,
        INVALID_PASSWORD_TYPE: status.HTTP_400_BAD_REQUEST,
        INVALID_PHONE: status.HTTP_400_BAD_REQUEST,
        INVALID_PHONE_TYPE: status.HTTP_400_BAD_REQUEST,
        INVALID_EMAIL_TYPE: status.HTTP_400_BAD_REQUEST,
        MISSING_PHONE: status.HTTP_400_BAD_REQUEST,
        MISSING_NAME: status.HTTP_400_BAD_REQUEST,
        MISSING_PASSWORD: status.HTTP_400_BAD_REQUEST,
        USER_ALREADY_EXIST: status.HTTP_400_BAD_REQUEST,
    }

    def get_string_for_invalid_phone_type(kwargs: dict):
        return "phone should be string"

    def get_string_for_invalid_name_type(kwargs: dict):
        return "name should be string"

    def get_string_for_invalid_password_type(kwargs: dict):
        return "password should be string"

    def get_string_for_invalid_email_type(kwargs: dict):
        return "email should be string"

    def get_string_for_invalid_phone(kwargs: dict):
        return "invalid phone"

    def get_string_for_invalid_name_length(kwargs: dict):
        return f"name length should be less than {str(Length.PERSON_NAME_MAX_LENGTH)}"

    def get_string_for_user_already_exist(kwargs: dict):
        return "user with this phone already exist"

    def get_string_for_missing_phone(kwargs: dict):
        return "missing phone"

    def get_string_for_missing_name(kwargs: dict):
        return "missing name"

    def get_string_for_missing_password(kwargs: dict):
        return "missing password"

    CODE_MESSAGE_MAP = {
        INVALID_PHONE_TYPE: get_string_for_invalid_phone_type,
        INVALID_PHONE: get_string_for_invalid_phone,
        INVALID_NAME_LENGTH: get_string_for_invalid_name_length,
        INVALID_NAME_TYPE: get_string_for_invalid_name_type,
        INVALID_PASSWORD_TYPE: get_string_for_invalid_password_type,
        INVALID_EMAIL_TYPE: get_string_for_invalid_email_type,
        MISSING_NAME: get_string_for_missing_name,
        MISSING_PHONE: get_string_for_missing_phone,
        MISSING_PASSWORD: get_string_for_missing_password,
        USER_ALREADY_EXIST: get_string_for_user_already_exist,
    }

    def __init__(self, code, **kwargs) -> None:
        (
            logger.debug(f">> ARGS: {locals()}")
            if code
            in [
                self.SUCCESS,
                self.CREATED,
            ]
            else logger.warning(f"{self.CODE_MESSAGE_MAP[code](kwargs)} - {locals()}")
        )
        self.ERROR_CODE_HTTP_MAP.update(super(ErrorCode, self).ERROR_CODE_HTTP_MAP)
        self.CODE_MESSAGE_MAP.update(super(ErrorCode, self).CODE_MESSAGE_MAP)
        super(ErrorCode, self).__init__(
            code,
            self.ERROR_CODE_HTTP_MAP[code],
            (
                self.CODE_MESSAGE_MAP[code](kwargs)
                if code not in [self.SUCCESS, self.CREATED]
                else None
            ),
            ModuleErrorPrefix.ACCOUNT,
        )
