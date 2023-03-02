from modeltranslation.translator import translator, TranslationOptions
from .models import Users, Authors


class UsersTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


translator.register(Users, UsersTranslationOptions)


class AuthorsTranslationOptions(TranslationOptions):
    fields = ('about',)


translator.register(Authors, AuthorsTranslationOptions)
