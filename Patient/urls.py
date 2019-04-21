from django.conf.urls import url

from . import views

app_name = 'Patient'

urlpatterns = [
    url(r'^patient/(?P<patient_pk>\w+)/patient_cases/(?P<patient_case_pk>\w+)/patient_records/$',
        views.ListCreatePatientRecords.as_view(), name='patient_records'),
    url(r'^patient/(?P<patient_pk>\w+)/patient_cases/(?P<patient_case_pk>\w+)/patient_records/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatientRecords.as_view(),
        name='patient_record_detail'),
    url(r'^patient/(?P<patient_pk>\w+)/patient_cases/$',
        views.ListCreatePatientCases.as_view(), name='patient_cases'),
    url(r'^patient/(?P<patient_pk>\w+)/patient_cases/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatientCases.as_view(),
        name='patient_case_detail'),
    url(r'^patient/$',
        views.ListCreatePatients.as_view(), name='patients'),
    url(r'^patient/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyPatients.as_view(),
        name='patient_detail'),
    url(r'^medical_practitioner/$',
        views.ListCreateMedicalPractitioner.as_view(), name='medical_practitioners'),
    url(r'^medical_practitioner/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyMedicalPractitioner.as_view(),
        name='medical_practitioner_detail'),
    url(r'^user/$',
        views.ListCreateUser.as_view(), name='users'),
    url(r'^user/(?P<pk>[a-zA-Z0-9-]+)/$',
        views.RetrieveUpdateDestroyUser.as_view(), name='users_detail'),
]
