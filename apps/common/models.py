from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    class Meta:
        abstract = True


class ContactUs(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    email = models.EmailField(verbose_name=_('Email'), max_length=25)
    subject = models.CharField(verbose_name=_('Subject'), max_length=255)
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class AboutUs(models.Model):
    email = models.EmailField(verbose_name=_('Email'), max_length=25)
    # phone = PhoneNumberField(verbose_name=_("Phone"), unique=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=12, unique=True)
    text = models.TextField(verbose_name='Text')

    telegram = models.CharField(verbose_name=_("Telegram"), max_length=70, null=True, blank=True)
    instagram = models.CharField(verbose_name=_("Instagram"), max_length=70, null=True, blank=True)
    facebook = models.CharField(verbose_name=_("Facebook"), max_length=70, null=True, blank=True)
    twiter = models.CharField(verbose_name=_("Twiter"), max_length=70, null=True, blank=True)
    youtube = models.CharField(verbose_name=_("Youtube"), max_length=70, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "AboutUs"
        verbose_name_plural = "AboutUs"


class SubscribeForNewsletter(BaseModel):
    email = models.EmailField(verbose_name='Email', max_length=25)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "SubscribeForNewsletter"
        verbose_name_plural = "SubscribeForNewsletters"


class FAQs(BaseModel):
    question = models.CharField(verbose_name=_('Question'), max_length=255)
    answer = RichTextField(verbose_name=_("Answer"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"