# Generated by Django 3.1.6 on 2021-02-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('s_usn', models.CharField(editable=False, max_length=11, primary_key=True, serialize=False)),
                ('s_mobile', models.IntegerField(editable=False)),
                ('s_email', models.EmailField(default='', editable=False, max_length=32)),
            ],
        ),
    ]