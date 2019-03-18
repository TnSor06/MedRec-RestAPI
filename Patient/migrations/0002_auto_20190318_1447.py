# Generated by Django 2.0 on 2019-03-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='icd_code',
            field=models.ForeignKey(blank=True, db_column='icd_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ICD.ICDCodes'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='icd_sub_code',
            field=models.ForeignKey(blank=True, db_column='icd_sub_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ICD.ICDSubCodes'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_cases', to='Patient.Patient'),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_records', to='Patient.PatientCase'),
        ),
    ]
