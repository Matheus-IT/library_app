# Generated by Django 3.1.7 on 2021-03-21 01:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id_book', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('publishing_company', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
