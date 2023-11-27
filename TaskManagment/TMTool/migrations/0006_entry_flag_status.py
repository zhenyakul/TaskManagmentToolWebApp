# Generated by Django 4.2.7 on 2023-11-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMTool', '0005_remove_entry_owner_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='flag_status',
            field=models.CharField(choices=[('status1', 'created'), ('status2', 'In progress'), ('status3', 'suspended'), ('status4', 'done')], default='status1', max_length=10),
        ),
    ]
