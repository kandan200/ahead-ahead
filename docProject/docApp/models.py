from django.db import models
# Create your models here.


gender = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('P', 'Prefer not to say')
)
class UserProfile(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    # date_of_birth = models.DateTimeField(null=True)
    sex = models.CharField(choices=gender, max_length=20)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True)
    mdcn = models.IntegerField(null=False, primary_key=True, default=123)
    state_of_residence = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=100, null=True)
    # year_of_graduation = models.DateTimeField(null=True)
    # certificate = models.FileField(null=True)
    # avatar = models.ImageField(null=True)

    def __str__(self):
        return f"Dr, {self.lastName}, {self.firstName}"

    class Meta:
        db_table = 'User Profile'
    