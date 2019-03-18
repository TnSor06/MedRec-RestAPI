from django.conf.urls import url

from . import views

app_name = 'Patient'

urlpatterns = [
    url(r'^(?P<patient_pk>\w+)/patient_cases/(?P<patient_case_pk>\w+)/patient_records/$',
        views.ListCreatePatientRecords.as_view(), name='patient_records'),
    url(r'^(?P<patient_pk>\w+)/patient_cases/(?P<patient_case_pk>\w+)/patient_records/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatientRecords.as_view(),
        name='patient_record_detail'),
    url(r'^(?P<patient_pk>\w+)/patient_cases/$',
        views.ListCreatePatientCases.as_view(), name='patient_cases'),
    url(r'^(?P<patient_pk>\w+)/patient_cases/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatientCases.as_view(),
        name='patient_case_detail'),
    url(r'^$',
        views.ListCreatePatients.as_view(), name='patients'),
    url(r'^(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatients.as_view(),
        name='patient_detail')
]
