from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientRecord
        fields = ('record_id', 'visit_no',
                  'on_arrival', 'diagnosis', 'tx',
                  'report_suggestions', 'medication',
                  'advice', 'query', 'case', 'created_at')
        ordering = ('created_at')


class PatientCaseSerializer(serializers.ModelSerializer):
    patient_records = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = models.PatientCase
        fields = ('case_id', 'patient',
                  'mp', 'icd_sub_code', 'icd_code',
                  'hpc', 'moi',
                  'd_and_v', 'clinical_note', 'no_of_visits',
                  'created_at', 'patient_records')


class PatientSerializer(serializers.ModelSerializer):
    patient_cases = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = models.Patient
        fields = ('patient_id', 'last_name',
                  'first_name', 'middle_name', 'dob',
                  'sex', 'blood_type', 'address', 'pincode',
                  'country_code', 'occupation', 'contact_no_1',
                  'contact_no_2', 'email', 'allergies', 'dhx', 'ca',
                  'iddm', 'niddm', 'mi', 'af', 'registered_at', 'patient_cases')


class MedicalPractitionerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True
    )
    # user_ = User.objects.get_queryset(user=user)
    # group_name = user_.groups.values_list('name', flat=True)
    class Meta:
        model = models.MedicalPractitioner
        fields = ('mp_id', 'last_name', 'user',
                  'first_name', 'middle_name',
                  'dob', 'sex', 'address', 'clinic_address',
                  'degree', 'field', 'email', 'hospital',
                  'pincode', 'country_code', 'registered_at')
        ordering = ('mp_id')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'groups')
