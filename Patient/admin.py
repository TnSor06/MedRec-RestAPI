from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Country)
admin.site.register(models.Region)
admin.site.register(models.Hospital)
admin.site.register(models.MedicalPractitioner)
admin.site.register(models.DatabaseAdmin)
admin.site.register(models.Patient)
admin.site.register(models.PatientCase)
admin.site.register(models.PatientRecord)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'email', 'first_name', 'middle_name',
                    'last_name', 'user_type', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('id', 'email', 'first_name', 'middle_name',
                   'last_name', 'user_type', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'first_name',
                           'middle_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'user_type', 'password1', 'password2', 'is_staff', 'is_active', 'date_joined')}
         ),
    )
    search_fields = ('email', 'user_type')
    ordering = ('email', 'user_type')


admin.site.register(CustomUser, CustomUserAdmin)
