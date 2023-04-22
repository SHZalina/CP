# Generated by Django 4.1.7 on 2023-04-22 14:56

import datetime
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
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Собака', 'Собака'), ('Рептилия', 'Рептилия'), ('', 'Другие'), ('Грызун', 'Грызун'), ('Рыбка', 'Рыбка'), ('Кот', 'Кот'), ('Птичка', 'Птичка')], max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(choices=[('Южно-Сахалинск', 'Южно-Сахалинск'), ('Москва', 'Москва'), ('Волгоград', 'Волгоград'), ('Петропавловск-Камчатский', 'Петропавловск-Камчатский'), ('Калининград', 'Калининград'), ('Мурманск', 'Мурманск'), ('Владикавказ', 'Владикавказ'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Пермь', 'Пермь'), ('Когалым', 'Когалым'), ('Астрахань', 'Астрахань'), ('Новый Уренгой', 'Новый Уренгой'), ('Краснодар', 'Краснодар'), ('Сочи', 'Сочи'), ('Грозный', 'Грозный'), ('Альметьевск', 'Альметьевск'), ('Набережные Челны', 'Набережные Челны'), ('Казань', 'Казань')], max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(default=datetime.datetime.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
