# Generated by Django 3.1.6 on 2021-02-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=11)),
                ('MOBILE', models.IntegerField(max_length=10)),
                ('EMAIL', models.EmailField(max_length=34)),
            ],
        ),
    ]