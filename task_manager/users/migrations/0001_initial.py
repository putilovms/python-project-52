# Generated by Django 5.1.1 on 2024-10-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='User name')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
        ),
    ]
