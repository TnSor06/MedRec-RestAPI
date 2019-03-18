from django.conf.urls import url

from . import views

app_name = 'ICD'

urlpatterns = [
    url(r'^icd_codes/(?P<icd_code_pk>\w+)/icd_sub_codes/$',
        views.ListCreateICDSubCodes.as_view(), name='icd_sub_codes'),
    url(r'^icd_codes/(?P<icd_code_pk>\w+)/icd_sub_codes/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyICDSubCodes.as_view(),
        name='icd_sub_code_detail'),
    url(r'^icd_codes/$',
        views.ListCreateICDCodes.as_view(), name='icd_codes'),
    url(r'^icd_codes/(?P<pk>\w+)/$',
        views.RetrieveUpdateDestroyICDCodes.as_view(),
        name='icd_code_detail')
]
