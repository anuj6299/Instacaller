from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from common.constants import Length


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, phone: str, password: str, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=Length.PHONE_NUMBER, unique=True)
    name = models.CharField(
        max_length=Length.PERSON_NAME_MAX_LENGTH, null=False, blank=False
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.phone
