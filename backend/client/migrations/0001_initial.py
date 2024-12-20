# Generated by Django 5.1.3 on 2024-12-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('customer_tags', models.TextField(blank=True, help_text='Comma-separated tags', null=True)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('name', models.CharField(editable=False, max_length=201, unique=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('name',), name='unique_name_constraint')],
            },
        ),
    ]
