# Generated by Django 4.0.4 on 2022-05-27 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shippingPrice',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='deliveredAt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='isDelivered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='isPaid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paidAt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paymentMethod',
        ),
        migrations.RemoveField(
            model_name='order',
            name='totalPrice',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='image',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
