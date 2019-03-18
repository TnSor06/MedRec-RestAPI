from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Country)
admin.site.register(models.Region)
admin.site.register(models.Hospital)
admin.site.register(models.MedicalPractitioner)
admin.site.register(models.Patient)
admin.site.register(models.PatientCase)
admin.site.register(models.PatientRecord)
