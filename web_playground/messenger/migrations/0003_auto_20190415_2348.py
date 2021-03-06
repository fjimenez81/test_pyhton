# Generated by Django 2.1.7 on 2019-04-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20190415_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='messages',
            field=models.ManyToManyField(to='messenger.Message'),
        ),
    ]
