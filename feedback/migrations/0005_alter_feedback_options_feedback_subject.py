# Generated by Django 5.1.5 on 2025-02-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_contact_number_feedback_roll_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'get_latest_by': 'created_at', 'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
