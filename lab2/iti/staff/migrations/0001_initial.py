# Generated by Django 4.2 on 2023-05-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('Password', models.CharField(default='default_password', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
