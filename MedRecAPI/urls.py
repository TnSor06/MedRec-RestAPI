from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework import routers
from Patient import views
router = routers.SimpleRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'patient_cases', views.PatientCaseViewSet)
router.register(r'patient_records', views.PatientRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/v1/icd/', include('ICD.urls', namespace='icd')),
    url(r'^api/v1/patient_/', include((router.urls, 'Patient'),
        namespace='patient_')),

]
