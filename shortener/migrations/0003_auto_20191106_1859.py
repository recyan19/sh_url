# Generated by Django 2.2.6 on 2019-11-06 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_url_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='short_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL),
        ),
    ]
