# Generated by Django 4.1.4 on 2023-01-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(null=True, to='events.myclubuser'),
        ),
    ]
