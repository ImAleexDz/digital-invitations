from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()

    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Families' 

class Confirmation(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()
    confirm = models.BooleanField(default=False)
    message = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Confirmation'
        verbose_name_plural = 'Confirmations' 