# Generated by Django 2.1.2 on 2018-10-15 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('print', '0002_auto_20181015_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='FileOwner',
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(default=1, help_text='a', on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
    ]