# Generated by Django 4.2.5 on 2023-11-23 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctore',
            fields=[
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to say')], max_length=20, verbose_name='Sex')),
                ('specialty', models.CharField(max_length=100, verbose_name='Specialty')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('mdcn', models.IntegerField(default=123, primary_key=True, serialize=False, verbose_name='MDCN Folio Number')),
                ('state_of_residence', models.CharField(max_length=30, verbose_name='State of Residence')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('confirm_password', models.CharField(max_length=100, verbose_name='Password')),
            ],
            options={
                'db_table': 'Doctor Profile',
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Research ID')),
                ('title', models.CharField(max_length=300, verbose_name='Research Title')),
                ('start_date', models.DateField(verbose_name='Research Start Date')),
                ('sample_size', models.IntegerField(verbose_name='Research Sample Size')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docApp.doctore')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Participant ID')),
                ('facility', models.CharField(max_length=200, verbose_name='Healthcare Facility')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to say')], max_length=20, verbose_name='Sex')),
                ('education', models.CharField(choices=[('N', 'None'), ('P', 'Primary'), ('S', 'Secondary'), ('T', 'Tertiary')], max_length=50, verbose_name='Level of Education')),
                ('occupation', models.CharField(max_length=100, verbose_name='Occupation')),
                ('tribe', models.CharField(max_length=50, verbose_name='Tribe')),
                ('presentation_date', models.DateField(verbose_name='Date of Presentation')),
                ('diagnosis', models.CharField(max_length=200, verbose_name='Diagnosis')),
                ('adnission', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=100, verbose_name='Admission Status')),
                ('research', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docApp.research')),
            ],
        ),
    ]
