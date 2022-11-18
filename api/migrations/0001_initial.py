# Generated by Django 4.1.3 on 2022-11-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnSaleItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('seller', models.CharField(max_length=30)),
                ('condition', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('negotiable', models.BooleanField(blank=True, default=False, null=True)),
                ('sold', models.BooleanField(blank=True, default=False, null=True)),
                ('img', models.CharField(max_length=300)),
            ],
        ),
    ]
