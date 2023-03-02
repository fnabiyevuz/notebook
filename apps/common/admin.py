from django.contrib import admin
from .models import ContactUs, AboutUs, SubscribeForNewsletter, FAQs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "message")
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "email", "subject")
    date_hierarchy = 'created_at'


admin.site.register(ContactUs, ContactUsAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "text")
    list_display_links = ("id", "email", "phone")
    search_fields = ("id", "email", "phone")


admin.site.register(AboutUs, AboutUsAdmin)


class SubscribeForNewsletterAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    list_display_links = ("id", "email")
    search_fields = ("id", "email")
    date_hierarchy = 'created_at'


admin.site.register(SubscribeForNewsletter, SubscribeForNewsletterAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer")
    list_display_links = ("id", "question")
    search_fields = ("id", "question", "answer")
    date_hierarchy = 'created_at'


admin.site.register(FAQs, FAQsAdmin)
