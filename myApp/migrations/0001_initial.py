# Generated by Django 3.2.10 on 2022-06-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateTimeField()),
                ('rbuilding', models.CharField(max_length=20)),
                ('rfloor', models.CharField(max_length=20)),
                ('rcat', models.CharField(max_length=20)),
                ('rphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('isDelete', models.BooleanField(default=False)),
                ('isHandle', models.BooleanField(default=False)),
            ],
        ),
    ]
