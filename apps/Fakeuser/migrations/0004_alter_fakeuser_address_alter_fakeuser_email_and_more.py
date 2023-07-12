# Generated by Django 4.2.1 on 2023-07-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fakeuser', '0003_remove_fakeuser_was_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='email',
            field=models.EmailField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='job',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='language',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='latutude',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='live_city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='longitude',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='phone',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
