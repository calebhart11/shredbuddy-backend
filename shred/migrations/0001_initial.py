# Generated by Django 4.1.7 on 2023-02-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('mountain', models.CharField(max_length=100)),
                ('goals', models.CharField(max_length=400)),
            ],
        ),
    ]
