# Generated by Django 2.0 on 2019-04-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20190420_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalpractitioner',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]