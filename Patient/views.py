from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import response
from . import models
from . import serializers


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

    @detail_route(methods=['get'])
    def patient_cases(self, request, pk=None):
        self.pagination_class.page_size = 1
        patient_cases = models.PatientCase.objects.filter(patient=pk)
        page = self.paginate_queryset(patient_cases)
        if page is not None:
            serializer = serializers.PatientCaseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializers.PatientCaseSerializer(
            patient_cases, many=True)
        return response.Response(serializer.data)


class PatientCaseViewSet(viewsets.ModelViewSet):
    queryset = models.PatientCase.objects.all()
    serializer_class = serializers.PatientCaseSerializer

    @detail_route(methods=['get'])
    def patient_records(self, request, pk=None):
        self.pagination_class.page_size = 4
        patient_records = models.PatientRecord.objects.filter(case=pk)
        page = self.paginate_queryset(patient_records)
        if page is not None:
            serializer = serializers.PatientRecordSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializers.PatientRecordSerializer(
            patient_records, many=True)
        return response.Response(serializer.data)


class PatientRecordViewSet(viewsets.ModelViewSet):
    queryset = models.PatientRecord.objects.all()
    serializer_class = serializers.PatientRecordSerializer
