# Generated by Django 4.2.1 on 2023-05-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ism')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='parol')),
            ],
        ),
    ]
