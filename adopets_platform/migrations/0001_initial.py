# Generated by Django 4.2.16 on 2024-10-09 21:16

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
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='pet_photos/')),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
