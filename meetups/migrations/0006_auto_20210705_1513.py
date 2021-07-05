# Generated by Django 3.2.4 on 2021-07-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_rename_locations_meetup_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participant'),
        ),
    ]
