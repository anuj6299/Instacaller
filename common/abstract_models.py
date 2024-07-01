import uuid
from django.db import models


class AbstractExternalFacing(models.Model):
    """
    Used by classes to implement uuid as unique field. This is helpful for -
    1. Use external_id as external facing IDs shared with clients.
       Great as we will not leak information about models
       that would have happened with auto increment integer PK
    2. As FKs when we want to decouple apps into Microservices in future
    """

    external_id = models.UUIDField(
        default=uuid.uuid4, unique=True, null=False, blank=False, editable=False
    )

    class Meta:
        abstract = True


class AbstractTime(models.Model):
    """
    Used by classes to keep track when the instance was created and last modified
    """

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
