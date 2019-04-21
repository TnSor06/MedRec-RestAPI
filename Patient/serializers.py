from rest_framework import serializers
from . import models
from django.contrib.auth.models import Group
from django.utils import timezone
import pytz


class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientRecord
        fields = ('record_id', 'visit_no',
                  'on_arrival', 'diagnosis', 'tx',
                  'report_suggestions', 'medication',
                  'advice', 'query', 'case', 'created_at')
        ordering = ('created_at')
        read_only_fields = ('record_id',)

    def create(self, validated_data):
        on_arrival = validated_data['on_arrival']
        diagnosis = validated_data['diagnosis']
        tx = validated_data['tx']
        report_suggestions = validated_data['report_suggestions']
        medication = validated_data['medication']
        advice = validated_data['advice']
        query = validated_data['query']
        case = validated_data['case']
        case_visit_incr = models.PatientCase.objects.filter(
            case_id__exact=int(case.case_id)).order_by('case_id')[0]
        case_visit_incr.no_of_visits += 1
        created_at = timezone.now()
        focus_id = '{}'.format(
            case.case_id)
        try:
            record = models.PatientRecord.objects.filter(
                record_id__startswith=int(focus_id)).order_by('-record_id')[0]
            record_id = record.record_id
            visit_no = record.visit_no
        except IndexError:
            visit_no = 0
            record_id = int('{}{}'.format(focus_id, '0000'))
        finally:
            visit_no = 1
            record_id += 1
        record_obj = models.PatientRecord(
            record_id=record_id, visit_no=visit_no,
            on_arrival=on_arrival, diagnosis=diagnosis, tx=tx,
            report_suggestions=report_suggestions, medication=medication,
            advice=advice, query=query, case=case, created_at=created_at
        )
        record_obj.save()
        return record_obj


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
        read_only_fields = ('case_id', 'patient_records')

    def create(self, validated_data):
        patient = validated_data['patient']
        mp = validated_data['mp']
        icd_sub_code = validated_data['icd_sub_code']
        icd_code = validated_data['icd_code']
        hpc = validated_data['hpc']
        moi = validated_data['moi']
        d_and_v = validated_data['d_and_v']
        clinical_note = validated_data['clinical_note']
        no_of_visits = 0
        created_at = timezone.now()
        focus_id = '{}'.format(
            patient.patient_id)
        try:
            case_id = models.PatientCase.objects.filter(
                case_id__startswith=int(focus_id)).order_by('-case_id')[0].case_id
        except IndexError:
            case_id = int('{}{}'.format(focus_id, '0000'))
        finally:
            case_id += 1
        case_obj = models.PatientCase(
            patient=patient,
            mp=mp, icd_sub_code=icd_sub_code, icd_code=icd_code,
            hpc=hpc, moi=moi,
            d_and_v=d_and_v, clinical_note=clinical_note,
            no_of_visits=no_of_visits, created_at=created_at
        )
        case_obj.save()
        return case_obj


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
        read_only_fields = ('patient_id', 'patient_cases')

    def create(self, validated_data):
        last_name = validated_data['last_name']
        first_name = validated_data['first_name']
        middle_name = validated_data['middle_name']
        dob = validated_data['dob']
        sex = validated_data['sex']
        blood_type = validated_data['blood_type']
        address = validated_data['address']
        pincode = validated_data['pincode']
        country_code = validated_data['country_code']
        occupation = validated_data['occupation']
        contact_no_1 = validated_data['contact_no_1']
        contact_no_2 = validated_data['contact_no_2']
        email = validated_data['email']
        allergies = validated_data['allergies']
        dhx = validated_data['dhx']
        ca = validated_data['ca']
        iddm = validated_data['iddm']
        niddm = validated_data['niddm']
        mi = validated_data['mi']
        af = validated_data['af']
        registered_at = timezone.now()
        focus_id = '{:03d}{:03d}'.format(
            country_code.country_code, pincode.pincode)
        # Code to avoid duplicate
        try:
            patient_id = models.Patient.objects.filter(
                patient_id__startswith=int(focus_id)).order_by('-patient_id')[0].patient_id
        except IndexError:
            patient_id = int('{}{}'.format(focus_id, '0000000000'))
        finally:
            patient_id += 1
        patient_obj = models.Patient(
            patient_id=patient_id, last_name=last_name,
            first_name=first_name, middle_name=middle_name, dob=dob,
            sex=sex, blood_type=blood_type, address=address, pincode=pincode,
            country_code=country_code, occupation=occupation, contact_no_1=contact_no_1,
            contact_no_2=contact_no_2, email=email, allergies=allergies, dhx=dhx, ca=ca,
            iddm=iddm, niddm=niddm, mi=mi, af=af, registered_at=registered_at
        )
        patient_obj.save()
        return patient_obj


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name',
                  'email', 'password', 'user_type', 'date_joined')
        extra_kwargs = {
            "password": {
                "write_only": True
            }}
        read_only_fields = ('user_type', 'date_joined', 'id')

    def create(self, validated_data):
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
        return user_obj


class MedicalPractitionerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=models.CustomUser.objects.all())

    class Meta:
        model = models.MedicalPractitioner
        fields = ('user', 'mp_id',
                  'dob', 'sex', 'address', 'mobile_number', 'clinic_address',
                  'degree', 'field', 'hospital',
                  'pincode', 'country_code')
        ordering = ('mp_id')
        read_only_fields = ('mp_id',)

    def create(self, validated_data):
        user = validated_data['user']
        dob = validated_data['dob']
        sex = validated_data['sex']
        address = validated_data['address']
        mobile_number = validated_data['mobile_number']
        clinic_address = validated_data['clinic_address']
        degree = validated_data['degree']
        field = validated_data['field']
        hospital = validated_data['hospital']
        pincode = validated_data['pincode']
        country_code = validated_data['country_code']
        focus_id = '{:03d}{:03d}'.format(
            country_code.country_code, pincode.pincode)
        try:
            mp_id = models.MedicalPractitioner.objects.filter(
                mp_id__startswith=int(focus_id)).order_by('-mp_id')[0].mp_id
        except IndexError:
            mp_id = int('{}{}'.format(focus_id, '000000'))
        finally:
            mp_id += 1
        mp_obj = models.MedicalPractitioner(
            mp_id=mp_id, user=user,
            dob=dob, sex=sex,
            address=address, mobile_number=mobile_number,
            clinic_address=clinic_address, degree=degree,
            field=field, hospital=hospital,
            pincode=pincode, country_code=country_code
        )
        mp_obj.save()
        return mp_obj
