from django.db import models
from django.utils import timezone
# Create your models here.

class SignUp(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(default=timezone.now, null=True)
    sex = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True)
    mdcn_folio_number = models.IntegerField(null=False)
    state_of_residence = models.CharField(max_length=30, null=True)
    year_of_graduation = models.DateTimeField(null=True)
    certificate = models.FileField(null=True)

    def __str__(self):
        return '%s' %('Dr ', self.firstName )
    