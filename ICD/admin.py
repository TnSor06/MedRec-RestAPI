from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.ICDCodes)
admin.site.register(models.ICDSubCodes)
