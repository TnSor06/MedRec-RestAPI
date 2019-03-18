# Generated by Django 2.0 on 2019-03-11 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IcdCodes',
            fields=[
                ('icd_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('common_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'icd_codes',
            },
        ),
        migrations.CreateModel(
            name='IcdSubCodes',
            fields=[
                ('icd_sub_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('scientific_name', models.TextField(blank=True, null=True)),
                ('icd_code', models.ForeignKey(blank=True, db_column='icd_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ICD.IcdCodes')),
            ],
            options={
                'db_table': 'icd_sub_codes',
            },
        ),
    ]