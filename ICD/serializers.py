from rest_framework import serializers
from . import models


class ICDSubCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ICDSubCodes
        fields = ('icd_sub_code', 'scientific_name', 'icd_code')


class ICDCodesSerializer(serializers.ModelSerializer):
    icd_sub_codes = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
        )

    class Meta:
        model = models.ICDCodes
        fields = ('icd_code', 'common_name', 'icd_sub_codes')
