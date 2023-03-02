from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .user_manager import UserManager
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from ..common.models import BaseModel
# from phonenumber_field.modelfields import PhoneNumberField


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("Email"), max_length=60, unique=True, null=True)
    username = models.CharField(verbose_name=_("Username"), max_length=30, unique=True)
    # phone = PhoneNumberField(verbose_name=_("Phone"), unique=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=12, unique=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=30)
    last_name = models.CharField(verbose_name=_("Lastname"), max_length=30)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to='authors', default='user.png', null=True, blank=True)

    date_joined = models.DateTimeField(verbose_name=_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(verbose_name=_("last login"), auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Authors(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name=_('User'))
    about = RichTextField(verbose_name=_("About author"))
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    telegram = models.CharField(verbose_name=_("Telegram"), max_length=70, null=True, blank=True)
    instagram = models.CharField(verbose_name=_("Instagram"), max_length=70, null=True, blank=True)
    facebook = models.CharField(verbose_name=_("Facebook"), max_length=70, null=True, blank=True)
    twiter = models.CharField(verbose_name=_("Twiter"), max_length=70, null=True, blank=True)
    youtube = models.CharField(verbose_name=_("Youtube"), max_length=70, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Subscribes(BaseModel):
    author = models.ForeignKey(Authors, verbose_name=_('Author'), on_delete=models.CASCADE,
                               related_name='author_subscribers')
    user = models.ForeignKey(Users, verbose_name=_('User'), related_name='user_subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return f"Author: {self.author} | User : {self.user}"

    class Meta:
        verbose_name = "Subsicribe"
        verbose_name_plural = "Subsicribes"
