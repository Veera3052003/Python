# Generated by Django 4.2.10 on 2024-03-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_students_s_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='s_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='s_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
