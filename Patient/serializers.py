from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
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
        model = User
        fields = ('id', 'username', 'password', 'email', 'groups')
        extra_kwags = {
            "password": {
                "write_only": True
            }}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        group = validated_data['groups'][0].name
        my_group = Group.objects.get(name=group)
        user_obj.groups.add(my_group)
        return validated_data


class MedicalPractitionerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.MedicalPractitioner
        fields = ('mp_id', 'last_name', 'user',
                  'first_name', 'middle_name',
                  'dob', 'sex', 'address', 'clinic_address',
                  'degree', 'field', 'email', 'hospital',
                  'pincode', 'country_code', 'registered_at')
        ordering = ('mp_id')
