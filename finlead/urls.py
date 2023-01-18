
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("app.urls")),
    path('user/', include("user.urls")),
    path('accounts/', include('allauth.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'user.views.my_custom_page_not_found_view'
handler400 = 'user.views.my_custom_bad_request_view'
handler403 = 'user.views.my_custom_permission_denied_view'
handler500 = 'user.views.my_custom_error_view'
