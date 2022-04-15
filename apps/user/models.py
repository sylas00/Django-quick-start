from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# 这里选择直接继承AbstractBaseUser 和PermissionsMixin 而不是拓展AbstractUser类 是为了精简User表字段 其他字段可自行添加

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = "username"

    mobile_phone = models.CharField(max_length=20, blank=True, verbose_name='手机号码')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月日')

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
