# Generated by Django 3.2.7 on 2021-09-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('acct_no', models.CharField(max_length=255)),
                ('routine_no', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('apt_unit', models.CharField(max_length=255)),
                ('expiry_date', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcation_type', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('prev_bal', models.CharField(max_length=255)),
                ('bal', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('trans_date', models.CharField(max_length=255)),
            ],
        ),
    ]
