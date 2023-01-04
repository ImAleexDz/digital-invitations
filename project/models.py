from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()

    class Meta:
        verbose_name = 'Familia Diana'
        verbose_name_plural = 'Familiares Diana' 

class Bf_Family(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()

    class Meta:
        verbose_name = 'Familia Ernesto'
        verbose_name_plural = 'Familiares Ernesto' 

class Friends(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()

    class Meta:
        verbose_name = 'Amigo'
        verbose_name_plural = 'Amigos' 

class Confirmation(models.Model):
    name = models.CharField(max_length=200)
    tickets = models.IntegerField()
    confirm = models.BooleanField(default=False)
    message = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Confirmación'
        verbose_name_plural = 'Confirmaciones' 