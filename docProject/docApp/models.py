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
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    # date_of_birth = models.DateTimeField(null=True)
    sex = models.CharField(choices=gender, max_length=20)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(null=True)
    mdcn = models.IntegerField(null=False, primary_key=True, default=123)
    state_of_residence = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=100, null=True)
    # year_of_graduation = models.DateTimeField(null=True)
    # certificate = models.FileField(null=True)
    # avatar = models.ImageField(null=True)

    def __str__(self):
        return f"Dr {self.lastName} {self.firstName}"

    class Meta:
        db_table ='Doctor Profile'
    

class Research(models.Model):
    id =models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=300)
    start_date = models.DateField()
    doctor = models.ForeignKey(Doctore, on_delete=models.CASCADE)
    # assistant = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    sample_size = models.IntegerField()

    def __str__(self):
        return self.title


class Participants(models.Model):
    id = models.IntegerField(primary_key=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    facility = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(choices=gender, max_length=20)
    education = models.CharField(choices=school, max_length=50)
    occupation = models.CharField(max_length=100)
    tribe = models.CharField(max_length=50)
    presentation_date = models.DateField()
    diagnosis = models.CharField(max_length=200)
    adnission = models.CharField(choices=admitted, max_length=100)

    def __str__(self):
        return f'Participant in {self.research}'