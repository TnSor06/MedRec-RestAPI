# Create your views here.
from rest_framework import generics
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework import permissions


class ListCreateUser(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.CustomUser.objects.all().filter(user_type=2)
    serializer_class = serializers.UserSerializer


class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.CustomUser.objects.get_queryset().order_by('id')
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            email=self.kwargs.get('email')
        )


class ListCreateMedicalPractitioner(generics.ListCreateAPIView):
    queryset = models.MedicalPractitioner.objects.get_queryset().order_by('mp_id')
    serializer_class = serializers.MedicalPractitionerSerializer


class RetrieveUpdateDestroyMedicalPractitioner(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MedicalPractitioner.objects.get_queryset().order_by('mp_id')
    serializer_class = serializers.MedicalPractitionerSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            mp_id=self.kwargs.get('pk')
        )


class ListCreatePatients(generics.ListCreateAPIView):
    queryset = models.Patient.objects.get_queryset().order_by('patient_id')
    serializer_class = serializers.PatientSerializer


class RetrieveUpdateDestroyPatients(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Patient.objects.get_queryset().order_by('patient_id')
    serializer_class = serializers.PatientSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            patient_id=self.kwargs.get('pk')
        )


class ListCreatePatientCases(generics.ListCreateAPIView):
    queryset = models.PatientCase.objects.get_queryset().order_by('-created_at')
    serializer_class = serializers.PatientCaseSerializer

    def get_queryset(self):
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        last_many = self.request.query_params.get('last_many', None)
        qs = self.queryset.filter(patient=self.kwargs.get('patient_pk'))
        if from_date is not None and to_date is not None:
            qs = qs.filter(created_at__range=(from_date, to_date))
        elif last_many is not None:
            qs = qs[0:last_many]
        return qs

    def perform_create(self, serializer):
        patient = get_object_or_404(
            models.PatientCase,
            self.kwargs.get('patient_pk'))
        serializer.save(patient=patient)


class RetrieveUpdateDestroyPatientCases(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PatientCase.objects.get_queryset().order_by('-created_at')
    serializer_class = serializers.PatientCaseSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            patient=self.kwargs.get('patient_pk'),
            case_id=self.kwargs.get('pk')
        )


class ListCreatePatientRecords(generics.ListCreateAPIView):
    queryset = models.PatientRecord.objects.get_queryset().order_by('-created_at')
    serializer_class = serializers.PatientRecordSerializer

    def get_queryset(self):
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        last_many = self.request.query_params.get('last_many', None)

        qs = self.queryset.filter(case=self.kwargs.get('patient_case_pk'))
        if from_date is not None and to_date is not None:
            qs = qs.filter(created_at__range=(from_date, to_date))
        elif last_many is not None:
            qs = qs[0:last_many]
        return qs

    def perform_create(self, serializer):
        patient_case = get_object_or_404(
            models.PatientRecord,
            self.kwargs.get('patient_case_pk'))
        serializer.save(case=patient_case)


class RetrieveUpdateDestroyPatientRecords(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PatientRecord.objects.get_queryset().order_by('-created_at')
    serializer_class = serializers.PatientRecordSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            case=self.kwargs.get('patient_case_pk'),
            record_id=self.kwargs.get('pk')
        )
