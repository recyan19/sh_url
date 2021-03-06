# Generated by Django 2.2.6 on 2019-11-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('url_id', models.SlugField(max_length=7, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=250)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('days_to_expiry', models.IntegerField(default=90)),
            ],
        ),
    ]
