from django.db import models

# Create your models here.


class ICDCodes(models.Model):
    icd_code = models.CharField(primary_key=True, max_length=10)
    common_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'icd_codes'
        verbose_name = 'ICD Code'
        verbose_name_plural = 'ICD Codes'

    def __str__(self):
        return '{}:{}'.format(self.icd_code, self.common_name)


class ICDSubCodes(models.Model):
    icd_sub_code = models.CharField(primary_key=True, max_length=10)
    scientific_name = models.TextField(blank=True, null=True)
    icd_code = models.ForeignKey(
        ICDCodes, models.SET_NULL, db_column='icd_code',
        related_name='icd_sub_codes', blank=True, null=True)

    class Meta:
        db_table = 'icd_sub_codes'
        verbose_name = 'ICD Sub Code'
        verbose_name_plural = 'ICD Sub Codes'

    def __str__(self):
        return '{}:{}'.format(self.icd_code, self.icd_sub_code)
