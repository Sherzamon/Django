# Generated by Django 4.2.1 on 2023-07-12 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fakeuser', '0002_alter_fakeuser_was_born'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakeuser',
            name='was_born',
        ),
    ]
