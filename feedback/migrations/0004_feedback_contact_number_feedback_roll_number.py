# Generated by Django 5.1.5 on 2025-02-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='contact_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='roll_number',
            field=models.IntegerField(null=True),
        ),
    ]
