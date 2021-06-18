# Generated by Django 3.0.7 on 2020-06-19 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ban', models.BooleanField(default=False, help_text='Users Bans', verbose_name='Ban')),
                ('user', models.ForeignKey(help_text='Choose Username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User name')),
            ],
            options={
                'verbose_name_plural': 'Ban Management',
                'ordering': ('user',),
            },
        ),
    ]
