from rest_framework import serializers
from . import models
from django.contrib.auth.models import Group


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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name',
                  'email', 'password', 'user_type', 'date_joined')
        extra_kwargs = {
            "password": {
                "write_only": True
            }}
        read_only_fields = ('user_type', 'date_joined')

    def create(self, validated_data):
        import datetime
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        middle_name = validated_data['middle_name']
        last_name = validated_data['last_name']
        user_type = 2
        user_obj = models.CustomUser(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            user_type=user_type
        )
        user_obj.set_password(password)
        user_obj.save()
        my_group = Group.objects.get(id=user_type)
        user_obj.groups.add(my_group)
        return validated_data


class MedicalPractitionerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.MedicalPractitioner
        fields = ('mp_id', 'user',
                  'dob', 'sex', 'address', 'clinic_address',
                  'degree', 'field', 'hospital',
                  'pincode', 'country_code')
        ordering = ('mp_id')


# Check groups of User
