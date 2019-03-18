from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/v1/icd/', include('ICD.urls', namespace='icd')),
    url(r'^api/v1/patient_/', include('Patient.urls',
        namespace='patient_')),
]
