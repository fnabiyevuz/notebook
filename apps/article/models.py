from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel
from ckeditor.fields import RichTextField

from apps.user.models import Users


class Categories(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=50, unique=True)
    icon = models.ImageField(verbose_name=_("Icon image"), upload_to='category_images')
    slug = models.SlugField(verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tags(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=50, unique=True)
    slug = models.SlugField(verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Articles(BaseModel):
    title = models.CharField(verbose_name=_("About user"), max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='category_articles',
                                 verbose_name=_("Category"), )
    tag = models.ManyToManyField(Tags, verbose_name=_('Tag'))
    text = RichTextField(verbose_name=_('Text'))
    image = models.ImageField(upload_to='articles', verbose_name=_('Image'))
    min_to_read = models.IntegerField(verbose_name=_("Minute to read"), default=0)
    slug = models.SlugField(verbose_name=_("Slug"))

    def save(self, *args, **kwargs):
        if self.text:
            self.min_to_read = int(len(self.text.split()) / 180) + 1
        super(Articles, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comments(BaseModel):
    article = models.ForeignKey(Articles, verbose_name="Article", on_delete=models.CASCADE, related_name="article_comments")
    commenter = models.ForeignKey(Users, verbose_name="Commenter", on_delete=models.CASCADE, related_name="user_comments")
    text = models.TextField(verbose_name="Text")
    parent = models.ForeignKey('self', verbose_name="Comment parent", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return str(self.commenter) + ' comment ' + str(self.text)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
