# Generated by Django 3.0.4 on 2020-06-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]