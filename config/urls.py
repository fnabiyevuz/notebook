from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("rosetta/", include('rosetta.urls'))
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
