# Generated by Django 3.2.4 on 2021-06-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sregistr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=150)),
                ('usn', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Sregistration',
        ),
    ]
