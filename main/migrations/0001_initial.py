# Generated by Django 5.1 on 2024-09-09 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compname', models.CharField(max_length=30)),
                ('tradNo', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractNo', models.IntegerField()),
                ('startDate', models.DateField()),
                ('peroid', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('ac', 'active'), ('in', 'wating'), ('rj', 'rejected'), ('tr', 'terminated')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], default='male', max_length=1)),
                ('job', models.CharField(choices=[('em', 'administrator'), ('it', 'IT'), ('en', 'Engineer'), ('dr', 'Driver'), ('ac', 'Accountant'), ('wo', 'Worker')], max_length=2)),
                ('inwork', models.BooleanField(default=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.company')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.contract')),
            ],
            options={
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Iqama',
            fields=[
                ('iqama', models.IntegerField(primary_key=True, serialize=False)),
                ('issued', models.DateField()),
                ('exireDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'nationalities',
            },
        ),
        migrations.CreateModel(
            name='WorkLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startfrom', models.DateField()),
                ('peroid', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Saudi',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.employee')),
                ('identity', models.IntegerField()),
                ('bdate', models.DateField()),
            ],
            bases=('main.employee',),
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.nationality'),
        ),
        migrations.CreateModel(
            name='NonSaudi',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.employee')),
                ('bdate', models.DateField()),
                ('passportNo', models.CharField(max_length=20, unique=True)),
                ('iqama', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.iqama')),
                ('workLicense', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.worklicense')),
            ],
            bases=('main.employee',),
        ),
    ]