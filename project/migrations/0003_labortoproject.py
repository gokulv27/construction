# Generated by Django 5.1.4 on 2024-12-21 08:49

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour_management', '0002_labormanagement_salary_adhocemployee_and_more'),
        ('project', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaborToProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('daily_wages', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('ad_hoc_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labor_to_projects', to='labour_management.adhocemployee')),
                ('labor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_assignments', to='labour_management.labormanagement')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labor_assignments', to='project.project')),
            ],
        ),
    ]