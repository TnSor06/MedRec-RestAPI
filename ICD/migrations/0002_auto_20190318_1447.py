# Generated by Django 2.0 on 2019-03-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ICD', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icdcodes',
            options={'verbose_name': 'ICD Code', 'verbose_name_plural': 'ICD Codes'},
        ),
        migrations.AlterModelOptions(
            name='icdsubcodes',
            options={'verbose_name': 'ICD Sub Code', 'verbose_name_plural': 'ICD Sub Codes'},
        ),
        migrations.AlterField(
            model_name='icdsubcodes',
            name='icd_code',
            field=models.ForeignKey(blank=True, db_column='icd_code', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icd_sub_codes', to='ICD.ICDCodes'),
        ),
    ]
