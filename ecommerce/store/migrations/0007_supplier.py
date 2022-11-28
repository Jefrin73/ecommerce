# Generated by Django 4.0.4 on 2022-07-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]