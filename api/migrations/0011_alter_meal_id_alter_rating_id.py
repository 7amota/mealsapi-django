# Generated by Django 4.1.5 on 2023-01-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_meal_id_alter_rating_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]