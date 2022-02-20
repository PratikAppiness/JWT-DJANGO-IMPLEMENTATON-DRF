# Generated by Django 3.2.11 on 2022-02-17 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('category', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Product Category')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modefied_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100, verbose_name='Product Title')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modefied_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productcategory', verbose_name='P. Category')),
            ],
        ),
    ]
