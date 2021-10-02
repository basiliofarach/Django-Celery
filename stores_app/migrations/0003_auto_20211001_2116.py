# Generated by Django 3.2.5 on 2021-10-01 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores_app', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='email',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='username',
            field=models.TextField(),
        ),
    ]