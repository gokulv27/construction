# Generated by Django 5.1.4 on 2024-12-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
