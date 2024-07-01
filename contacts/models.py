from django.db import models
from django.core.validators import validate_email

from common.abstract_models import AbstractTime, AbstractExternalFacing
from common.constants import Length

from account.models import User


class Contact(AbstractTime, AbstractExternalFacing):
    """
    Contact model keeps the records of contacts of a user
    """

    name = models.CharField(
        max_length=Length.PERSON_NAME_MAX_LENGTH, null=False, blank=False
    )
    phone = models.CharField(max_length=Length.PHONE_NUMBER, null=False, blank=False)
    email = models.EmailField(validators=[validate_email], null=True, blank=True)

    # this contact belong to this user
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # TODO - if a user is deleted, should we keep his contacts in our db?
    # this depends on privacy policy and business team decision
    # right now I am keeping the contacts even if owner is deleted

    # TODO: if scale is high, we can index phone because
    #  most of the get queries on this table are by phone
    # We can index phone like below -
    # class Meta:
    #     indexes = [models.Index(fields=["phone"])]

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"


class Spam(AbstractTime):
    """
    Spam model keeps the records of phone numbers which are marked as spam by a user
    """

    phone = models.CharField(max_length=Length.PHONE_NUMBER, null=False, blank=False)

    # this user mark above contact as spam
    spammed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        # one user should spam a phone once only
        unique_together = ["phone", "spammed_by"]

    def __str__(self) -> str:
        return f"{self.phone} - {self.spammed_by}"
