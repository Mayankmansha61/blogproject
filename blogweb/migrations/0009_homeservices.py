# Generated by Django 2.2.3 on 2019-07-18 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogweb', '0008_sliders_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeservices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('readmore', models.CharField(default='', max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
                ('status', models.CharField(default='publish', max_length=30)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
            ],
        ),
    ]