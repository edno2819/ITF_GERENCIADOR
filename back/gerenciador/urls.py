from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from gerenciador.views import *

urlpatterns = [
    # ADMIN
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("summernote/", include("django_summernote.urls")),

    # TEMPLATES
    path("", home, name='home'),
    path("saq/", include("saq.urls")),
    path("treinamento/", include("treinamento.urls")),

    # API
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
