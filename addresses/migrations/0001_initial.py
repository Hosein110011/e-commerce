# Generated by Django 4.2.4 on 2023-08-14 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=125)),
                ('address_line_1', models.CharField(max_length=125)),
                ('address_line_2', models.CharField(blank=True, max_length=125, null=True)),
                ('city', models.CharField(max_length=125)),
                ('country', models.CharField(default='United State of America', max_length=125)),
                ('state', models.CharField(max_length=125)),
                ('postal_code', models.CharField(max_length=125)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.billingprofile')),
            ],
        ),
    ]