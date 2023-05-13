# Generated by Django 4.1.7 on 2023-05-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_category_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Рептилия', 'Рептилия'), ('Собака', 'Собака'), ('Птичка', 'Птичка'), ('Грызун', 'Грызун'), ('', 'Другие'), ('Рыбка', 'Рыбка'), ('Кот', 'Кот')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Владикавказ', 'Владикавказ'), ('Калининград', 'Калининград'), ('Мурманск', 'Мурманск'), ('Сочи', 'Сочи'), ('Когалым', 'Когалым'), ('Грозный', 'Грозный'), ('Набережные Челны', 'Набережные Челны'), ('Южно-Сахалинск', 'Южно-Сахалинск'), ('Москва', 'Москва'), ('Казань', 'Казань'), ('Петропавловск-Камчатский', 'Петропавловск-Камчатский'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Пермь', 'Пермь'), ('Краснодар', 'Краснодар'), ('Астрахань', 'Астрахань'), ('Новый Уренгой', 'Новый Уренгой'), ('Волгоград', 'Волгоград'), ('Альметьевск', 'Альметьевск')], max_length=100),
        ),
    ]
