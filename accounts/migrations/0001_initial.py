# Generated by Django 2.2.5 on 2019-10-02 12:55

import accounts.models
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(default='profile.png', help_text='Profile Picture', upload_to=accounts.models.user_directory_path)),
                ('bio', models.TextField(blank=True, default='ND', max_length=500)),
                ('location', models.CharField(blank=True, default='ND', max_length=30)),
                ('organization', models.CharField(blank=True, default='ND', max_length=100)),
                ('linkedin', models.URLField(blank=True, default='https://www.linkedin.com/in/username/')),
                ('github', models.URLField(blank=True, default='https://github.com/username')),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/username')),
                ('facebook', models.URLField(blank=True, default='https://facebook.com/username')),
                ('instagram', models.URLField(blank=True, default='https://www.instagram.com/user.name/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]