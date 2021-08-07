# Generated by Django 3.2.5 on 2021-08-05 03:42

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('js_app', '0006_alter_idcode_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcode',
            name='content',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=8), max_length=48, size=4),
        ),
    ]