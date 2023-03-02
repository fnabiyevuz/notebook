from modeltranslation.translator import translator, TranslationOptions
from .models import Categories, Tags, Articles, Comments


class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Categories, CategoriesTranslationOptions)


class TagsTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Tags, TagsTranslationOptions)


class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(Articles, ArticlesTranslationOptions)


class CommentsTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(Comments, CommentsTranslationOptions)
