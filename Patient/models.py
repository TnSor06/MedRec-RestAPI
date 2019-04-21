from django.db import models
from ICD.models import ICDCodes, ICDSubCodes
# Create your models here.

# User

# Import for User
from django.contrib.auth.models import Permission
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    last_name = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    TYPE_OF_USER = (
        (1, 'Database-Admin'),
        (2, 'Medical-Practitioner')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email'), unique=True)
    user_type = models.IntegerField(
        choices=TYPE_OF_USER,
        default=None,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    objects = CustomUserManager()

    def __str__(self):
        return '{}-{}'.format(self.email, self.user_type)


###

class Country(models.Model):
    country_code = models.BigIntegerField(primary_key=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '{}'.format(self.country_name)


class Region(models.Model):
    pincode = models.BigIntegerField(primary_key=True)
    region = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'region'

    def __str__(self):
        return '{}'.format(self.region)


class Hospital(models.Model):
    hospital_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.ForeignKey(
        Region, models.SET_NULL, db_column='pincode', blank=True, null=True)
    country_code = models.ForeignKey(
        Country, models.SET_NULL, db_column='country_code',
        blank=True, null=True)

    class Meta:
        db_table = 'hospital'

    def __str__(self):
        return '{}'.format(self.name)


class DatabaseAdmin(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='database_admin_profile', on_delete=models.CASCADE)
    da_id = models.BigIntegerField(primary_key=True)

    country_code = models.ForeignKey(
        Country, models.SET_NULL, db_column='country_code',
        blank=True, null=True)

    class Meta:
        db_table = 'database_admin'

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class MedicalPractitioner(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='medical_practitioner_profile', on_delete=models.CASCADE)
    mp_id = models.BigIntegerField(primary_key=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    clinic_address = models.TextField(blank=True, null=True)

    degree = models.CharField(max_length=10, blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    hospital = models.ForeignKey(
        Hospital, models.SET_NULL, blank=True, null=True)
    pincode = models.ForeignKey(
        Region, models.SET_NULL, db_column='pincode', blank=True, null=True)
    country_code = models.ForeignKey(
        Country, models.SET_NULL, db_column='country_code',
        blank=True, null=True)

    class Meta:
        db_table = 'medical_practitioner'
        permissions = (
            ('add_patient', 'Can add patient'),
            ('delete_patient', 'Can delete patient'),
            ('change_patient', 'Can change patient'),
            ('add_patientcase', 'Can add patient case'),
            ('delete_patientcase', 'Can delete patient case'),
            ('change_patientcase', 'Can change patient case'),
            ('add_patientrecord', 'Can add patient record'),
            ('delete_patientrecord', 'Can delete patient record'),
            ('change_patientrecord', 'Can change patient record'),
        )

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Patient(models.Model):
    patient_id = models.BigIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    blood_type = models.CharField(max_length=5, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    pincode = models.ForeignKey(
        Region, models.SET_NULL, db_column='pincode', blank=True, null=True)
    country_code = models.ForeignKey(
        Country, models.SET_NULL, db_column='country_code',
        blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    contact_no_1 = models.BigIntegerField(blank=True, null=True)
    contact_no_2 = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    dhx = models.TextField(db_column='DHx', blank=True, null=True)
    # Field name made lowercase.
    ca = models.IntegerField(db_column='Ca', blank=True, null=True)
    # Field name made lowercase.
    iddm = models.IntegerField(db_column='IDDM', blank=True, null=True)
    # Field name made lowercase.
    niddm = models.IntegerField(db_column='NIDDM', blank=True, null=True)
    # Field name made lowercase.
    mi = models.IntegerField(db_column='MI', blank=True, null=True)
    # Field name made lowercase.
    af = models.IntegerField(db_column='AF', blank=True, null=True)
    registered_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'patient'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PatientCase(models.Model):
    case_id = models.BigIntegerField(primary_key=True)
    patient = models.ForeignKey(
        Patient, models.SET_NULL, related_name='patient_cases',
        blank=True, null=True)
    mp = models.ForeignKey(MedicalPractitioner,
                           models.SET_NULL, blank=True, null=True)
    icd_sub_code = models.ForeignKey(
        ICDSubCodes, models.SET_NULL, db_column='icd_sub_code',
        blank=True, null=True)
    icd_code = models.ForeignKey(
        ICDCodes, models.SET_NULL, db_column='icd_code', blank=True, null=True)
    # Field name made lowercase.
    hpc = models.TextField(db_column='HPC', blank=True, null=True)
    # Field name made lowercase.
    moi = models.TextField(db_column='MoI', blank=True, null=True)
    # Field name made lowercase.
    d_and_v = models.TextField(db_column='D_and_V', blank=True, null=True)

    clinical_note = models.TextField(blank=True, null=True)
    no_of_visits = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'patient_case'
        ordering = ['created_at']

    def __str__(self):
        return '{}:{}'.format(self.case_id, self.patient.__str__)


class PatientRecord(models.Model):
    record_id = models.BigIntegerField(primary_key=True)
    visit_no = models.BigIntegerField(blank=True, null=True)
    on_arrival = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    tx = models.TextField(db_column='Tx', blank=True, null=True)
    report_suggestions = models.TextField(blank=True, null=True)

    medication = models.TextField(blank=True, null=True)
    advice = models.TextField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    case = models.ForeignKey(
        PatientCase, models.SET_NULL, related_name='patient_records',
        blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'patient_record'
        ordering = ['created_at']

    def __str__(self):
        return '{}.{}:{}'.format(
            self.case.id, self.record_id, self.case.patient.__str__)
