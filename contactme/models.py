from django.db import models

# Create your models here.

class contactdetails(models.Model):
    sendername = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    class Meta:
        db_table = 'contactdetails'

