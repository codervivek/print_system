# Generated by Django 2.1.2 on 2018-10-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='FileOwner',
            field=models.CharField(default='ADMIN', help_text='username', max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='isPrinted',
            field=models.BooleanField(default=False),
        ),
    ]
