# Generated by Django 5.1.3 on 2024-11-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_remove_employeetype_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeetype',
            options={},
        ),
        migrations.RemoveField(
            model_name='employeetype',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='employeetype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='employeetype',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]