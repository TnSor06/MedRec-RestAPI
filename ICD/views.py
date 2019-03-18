# Create your views here.
from rest_framework import generics
from django.shortcuts import get_object_or_404
from . import models
from . import serializers


class ListCreateICDCodes(generics.ListCreateAPIView):
    queryset = models.ICDCodes.objects.all()
    serializer_class = serializers.ICDCodesSerializer


class RetrieveUpdateDestroyICDCodes(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ICDCodes.objects.all()
    serializer_class = serializers.ICDCodesSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            icd_code=self.kwargs.get('pk')
        )


class ListCreateICDSubCodes(generics.ListCreateAPIView):
    queryset = models.ICDSubCodes.objects.all()
    serializer_class = serializers.ICDSubCodesSerializer

    def get_queryset(self):
        return self.queryset.filter(icd_code=self.kwargs.get('icd_code_pk'))

    def perform_create(self, serializer):
        icd_code = get_object_or_404(
            models.ICDCodes,
            self.kwargs.get('icd_code_pk'))
        serializer.save(icd_code=icd_code)


class RetrieveUpdateDestroyICDSubCodes(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ICDSubCodes.objects.all()
    serializer_class = serializers.ICDSubCodesSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            icd_code=self.kwargs.get('icd_code_pk'),
            icd_sub_code=self.kwargs.get('pk')
        )
