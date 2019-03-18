from rest_framework import serializers
from . import models


class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientRecord
        fields = ('record_id', 'visit_no',
                  'on_arrival', 'diagnosis', 'tx',
                  'report_suggestions', 'medication',
                  'advice', 'query', 'case', 'created_at')


class PatientCaseSerializer(serializers.ModelSerializer):
    patient_records = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='patient_:patientrecord-detail'
    )

    class Meta:
        model = models.PatientCase
        fields = ('case_id', 'patient',
                  'mp', 'icd_sub_code', 'icd_code',
                  'hpc', 'moi',
                  'd_and_v', 'clinical_note', 'no_of_visits',
                  'created_at', 'patient_records')


class PatientSerializer(serializers.ModelSerializer):
    patient_cases = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='patient_:patientcase-detail'
    )

    class Meta:
        model = models.Patient
        fields = ('patient_id', 'last_name',
                  'first_name', 'middle_name', 'dob',
                  'sex', 'blood_type', 'address', 'pincode',
                  'country_code', 'occupation', 'contact_no_1',
                  'contact_no_2', 'email', 'allergies', 'dhx', 'ca',
                  'iddm', 'niddm', 'mi', 'af', 'registered_at', 'patient_cases')
