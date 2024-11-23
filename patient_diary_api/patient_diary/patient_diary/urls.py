from django.urls import path
from django.conf import settings
from api.endpoints import api, get_patient_image
from django.conf.urls.static import static

urlpatterns = [
    path("api/", api.urls),
]


if settings.DEBUG:
    urlpatterns += [
        path("media/<str:snils>.jpg", get_patient_image),
    ]