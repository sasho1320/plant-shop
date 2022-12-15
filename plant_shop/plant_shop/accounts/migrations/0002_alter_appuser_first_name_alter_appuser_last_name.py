# Generated by Django 4.1.3 on 2022-12-15 13:56

import django.core.validators
from django.db import migrations, models
import plant_shop.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), plant_shop.utils.validators.validate_alphabet_characters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), plant_shop.utils.validators.validate_alphabet_characters]),
        ),
    ]
