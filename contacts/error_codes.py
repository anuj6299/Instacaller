import logging

from common.constants import ModuleErrorPrefix
from common.base_error_code import BaseErrorCode
from rest_framework import status

logger = logging.getLogger(__name__)


class ErrorCode(BaseErrorCode):
    INVALID_PHONE = "001"

    CONTACT_DOES_NOT_EXIST = "201"
    PHONE_ALREADY_SPAMMED = "202"

    ERROR_CODE_HTTP_MAP = {
        INVALID_PHONE: status.HTTP_400_BAD_REQUEST,
        CONTACT_DOES_NOT_EXIST: status.HTTP_400_BAD_REQUEST,
        PHONE_ALREADY_SPAMMED: status.HTTP_400_BAD_REQUEST,
    }

    def get_string_for_invalid_phone(kwargs: dict):
        return "invalid phone"

    def get_string_for_contact_does_not_exist(kwargs: dict):
        return "contact with this id does not exist"

    def get_string_for_phone_already_spammed(kwargs: dict):
        return "user has already marked this phone spam"

    CODE_MESSAGE_MAP = {
        INVALID_PHONE: get_string_for_invalid_phone,
        CONTACT_DOES_NOT_EXIST: get_string_for_contact_does_not_exist,
        PHONE_ALREADY_SPAMMED: get_string_for_phone_already_spammed,
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
