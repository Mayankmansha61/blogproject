# Generated by Django 2.2.3 on 2019-07-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogweb', '0005_auto_20190717_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
