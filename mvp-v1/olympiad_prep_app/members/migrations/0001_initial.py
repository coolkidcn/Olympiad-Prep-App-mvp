# Generated by Django 5.1.6 on 2025-02-16 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('userId', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('authuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(null=True, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentId', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('creatorId', models.BigIntegerField()),
                ('text', models.TextField()),
                ('viewers', models.ManyToManyField(blank=True, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Mindmap',
            fields=[
                ('mapid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('creatorId', models.BigIntegerField()),
                ('map', models.TextField()),
                ('viewers', models.ManyToManyField(blank=True, to='members.member')),
            ],
        ),
    ]
