# Generated by Django 4.0.3 on 2022-11-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copilot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('textarea_old', models.TextField(blank=True, max_length=1000, null=True)),
                ('textarea_new', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
