# Generated by Django 5.1.1 on 2024-10-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0008_alter_tasks_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.LabelsTasks', to='labels.labels', verbose_name='Labels'),
        ),
    ]