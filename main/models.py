from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(
                            max_length = 100, 
                             help_text= 'Enter the title of the event' 
                             )
    
    begin = models.DateTimeField()
    end   = models.DateTimeField()
    user = models.ForeignKey('Username', on_delete=models.SET_NULL, null= True )
    STATUSES = (
        ('e', 'ended'),
        ('w', 'will still happen'),
        ('c', 'canceled'),
        ('i', 'is happening')
    )
    status = models.CharField(
        max_length= 1,
        choices= STATUSES,
        blank= False,
        default= 'w',
        help_text= 'status of an event'
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('', args = [str(self.id)])


class Username(models.Model):
    name = models.CharField(
                            max_length=50,
                            help_text = 'Enter the user_s name' 
                            )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', args = [str(self.id)])


class Userpass(models.Model):
    passwd = models.CharField(
                            max_length=50,
                            help_text='enter a password'
                            )

class User(models.Model):
    name  = models.ForeignKey('Username', on_delete = models.SET_NULL, null = True)
    passwd =  models.ForeignKey('Userpass', on_delete = models.SET_NULL, null = True)