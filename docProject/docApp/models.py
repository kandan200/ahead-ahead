from django.db import models
# Create your models here.


gender = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('P', 'Prefer not to say')
)

school =(
    ('N', 'None'),
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('T', 'Tertiary')
)

admitted = (
    ('Y', 'Yes'),
    ('N', 'No')
)
class Doctore(models.Model):
    firstName = models.CharField(max_length=100, verbose_name='First Name')
    lastName = models.CharField(max_length=100, verbose_name='Last Name')
    # date_of_birth = models.DateTimeField(null=True)
    sex = models.CharField(choices=gender, max_length=20, verbose_name='Sex')
    specialty = models.CharField(max_length=100, verbose_name='Specialty')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=11, verbose_name='Phone Number')
    mdcn = models.IntegerField(null=False, primary_key=True, default=123, verbose_name='MDCN Folio Number')
    state_of_residence = models.CharField(max_length=30, verbose_name='State of Residence')
    password = models.CharField(max_length=100, verbose_name='Password')
    confirm_password = models.CharField(max_length=100, verbose_name='Password')

    # year_of_graduation = models.DateTimeField(null=True)
    # certificate = models.FileField(null=True)
    # avatar = models.ImageField(null=True)

    def __str__(self):
        return f"Dr {self.lastName} {self.firstName}"

    class Meta:
        db_table ='Doctor Profile'
    

class Research(models.Model):
    id =models.CharField(max_length=100, primary_key=True, verbose_name='Research ID')
    title = models.CharField(max_length=300, verbose_name='Research Title')
    start_date = models.DateField(verbose_name='Research Start Date')
    doctor = models.ForeignKey(Doctore, on_delete=models.CASCADE, null=True)
    # assistant = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    sample_size = models.IntegerField(verbose_name='Research Sample Size')

    def __str__(self):
        return self.title


class Participants(models.Model):
    id = models.CharField(primary_key=True, verbose_name='Participant ID', max_length=200)
    research = models.ForeignKey(Research, on_delete=models.CASCADE, null=True)
    facility = models.CharField(max_length=200, verbose_name='Healthcare Facility')
    age = models.IntegerField(verbose_name='Age')
    sex = models.CharField(choices=gender, max_length=20, verbose_name='Sex')
    education = models.CharField(choices=school, max_length=50, verbose_name='Level of Education')
    occupation = models.CharField(max_length=100, verbose_name='Occupation')
    tribe = models.CharField(max_length=50, verbose_name='Tribe')
    presentation_date = models.DateField(verbose_name='Date of Presentation')
    diagnosis = models.CharField(max_length=200, verbose_name='Diagnosis')
    adnission = models.CharField(choices=admitted, max_length=100, verbose_name='Admission Status')

    def __str__(self):
        return f'Participant in {self.research}'