# Generated by Django 5.0.6 on 2024-05-30 20:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0002_alter_category_options_item'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='item.item')),
                ('members', models.ManyToManyField(related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_msgs', to=settings.AUTH_USER_MODEL)),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='messaging.messages')),
            ],
        ),
    ]
