# Generated by Django 5.1.3 on 2024-12-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0005_vendortype'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaborSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
