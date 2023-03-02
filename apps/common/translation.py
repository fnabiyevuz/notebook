from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs, FAQs


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(AboutUs, AboutUsTranslationOptions)


class FAQsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


translator.register(FAQs, FAQsTranslationOptions)
