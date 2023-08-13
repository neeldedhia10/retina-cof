# Generated by Django 4.2.4 on 2023-08-04 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('width', models.IntegerField(default='0')),
                ('height', models.IntegerField(default='0')),
                ('od_x', models.IntegerField(default='0')),
                ('od_y', models.IntegerField(default='0')),
                ('cf_x', models.IntegerField(null=True)),
                ('cf_y', models.IntegerField(null=True)),
                ('ma_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('ma_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('ma_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('rh_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('rh_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('rh_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('he_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('he_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('he_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('cws_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('cws_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('cws_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nve_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nve_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nve_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nvd_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nvd_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('nvd_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('sh_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('sh_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('sh_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('vh_x', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('vh_y', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('vh_r', models.CharField(default='0', max_length=100, validators=[django.core.validators.int_list_validator])),
                ('comment', models.CharField(max_length=500, null=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('under_process', models.BooleanField(default=False)),
            ],
        ),
    ]