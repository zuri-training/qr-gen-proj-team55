from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("qr_gen/", include("qr_gen_app.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path("", include("qr_gen_app.urls")),


# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


