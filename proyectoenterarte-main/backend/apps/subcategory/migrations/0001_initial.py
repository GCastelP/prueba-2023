# Generated by Django 4.2 on 2023-06-10 02:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default=uuid.uuid4, max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
    ]