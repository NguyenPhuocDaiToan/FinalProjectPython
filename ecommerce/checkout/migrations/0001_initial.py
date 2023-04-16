# Generated by Django 3.1.7 on 2023-04-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(help_text='Bắt buộc', max_length=255, verbose_name='Tên vận chuyển:')),
                ('delivery_price', models.DecimalField(decimal_places=0, error_messages={'name': {'max_length': 'Giá phải nằm trong khoảng từ 0 đến 999.999đ'}}, help_text='Tối đa 999.999đ', max_digits=8, verbose_name='Giá')),
                ('delivery_method', models.CharField(choices=[('standard-shipping', 'Standard Shipping'), ('express-shipping', 'Express Shipping'), ('same-day-delivery', 'Same-day delivery'), ('in-store-pickup', 'In-store pickup'), ('digital-delivery', 'Digital delivery')], help_text='Bắt buộc', max_length=255, verbose_name='Phương thức vận chuyển')),
                ('delivery_time', models.CharField(help_text='Bắt buộc', max_length=255, verbose_name='Thời gian vận chuyển')),
                ('order', models.IntegerField(default=0, help_text='Bắt buộc', verbose_name='Thứ tự ưu tiên:')),
                ('is_active', models.BooleanField(default=True, verbose_name='Trạng thái hoạt động')),
            ],
            options={
                'verbose_name': 'Delivery Option',
                'verbose_name_plural': 'Delivery Options',
            },
        ),
        migrations.CreateModel(
            name='PaymentSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Bắt buộc', max_length=255, verbose_name='name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Selection',
                'verbose_name_plural': 'Payment Selections',
            },
        ),
    ]
