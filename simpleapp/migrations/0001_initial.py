# Generated by Django 4.0.3 on 2022-04-25 11:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simpleapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_thru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.material')),
                ('product_thru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='mats',
            field=models.ManyToManyField(through='simpleapp.ProductMaterial', to='simpleapp.material'),
        ),
    ]
