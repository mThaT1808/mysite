# Generated by Django 4.1.7 on 2023-04-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('card_number', models.CharField(max_length=16)),
                ('pin', models.IntegerField(max_length=4)),
            ],
        ),
    ]