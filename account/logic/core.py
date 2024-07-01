"""
Views will call only these core functions
No code logic here - Only call functions
"""

import logging
from typing import Union

from account.api.serializers import UserSerializer
from account.error_codes import ErrorCode
from account.logic.service import svc_register_user
from account.logic.validate import svc_validate_request_data_register_user
from account.models import User


logger = logging.getLogger(__name__)


def svc_account_register_user(
    request_data: dict,
    serialize: bool = False,
) -> tuple[ErrorCode, Union[User, dict]]:
    """
    Core function to register user
        1. Validate request data - return error if any
        2. Create user
        3. Serialize user data if asked
        4. Return user data
    """
    logger.debug(f">> ARGS: {locals()}")

    error = svc_validate_request_data_register_user(request_data=request_data)
    if error:
        return error, None

    error, user = svc_register_user(request_data)
    if error:
        return error, None

    if serialize:
        user = UserSerializer(user, many=False).data

    return ErrorCode(ErrorCode.CREATED), user
