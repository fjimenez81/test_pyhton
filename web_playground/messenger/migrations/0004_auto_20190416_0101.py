# Generated by Django 2.1.7 on 2019-04-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20190415_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='messages',
            field=models.ManyToManyField(to='messenger.Message'),
        ),
    ]