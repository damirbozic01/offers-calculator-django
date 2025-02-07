# Generated by Django 5.1.5 on 2025-02-07 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('valid_until', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='offers.offer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.product')),
                ('raw_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.rawmaterial')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.service')),
            ],
        ),
    ]
