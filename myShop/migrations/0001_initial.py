# Generated by Django 3.2.17 on 2023-02-23 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=None)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bar_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_discount', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myShop.clothescategory')),
                ('company_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myShop.company')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50)),
                ('supplier_address', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_company_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(default=0)),
                ('discount_amount', models.PositiveIntegerField(default=None)),
                ('payment_type', models.CharField(choices=[('CASH', 'CASH'), ('CARD', 'CARD'), ('MOBILE_BANKING', 'MOBILE_BANKING')], default='CASH', max_length=20)),
                ('received_amount', models.FloatField(default=0)),
                ('change_amount', models.FloatField(default=0)),
                ('reference_code', models.CharField(blank=True, max_length=20, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myShop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=None)),
                ('buying_price', models.FloatField(default=0)),
                ('selling_price', models.FloatField(default=0)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myShop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buying_price', models.FloatField(default=0)),
                ('selling_price', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myShop.product')),
            ],
            options={
                'db_table': 'product_update',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('total_price', models.PositiveIntegerField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attached_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]