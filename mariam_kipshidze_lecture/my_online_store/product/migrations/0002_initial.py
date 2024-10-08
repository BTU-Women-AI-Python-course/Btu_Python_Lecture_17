# Generated by Django 5.1 on 2024-09-23 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.category', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.tag', verbose_name='Tags'),
        ),
    ]
