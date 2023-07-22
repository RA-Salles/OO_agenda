from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(
                            max_length = 100, 
                             help_text= 'Enter the title of the event' 
                             )
    
    begin = models.DateField()
    end   = models.DateField()
    user = models.CharField(
                            max_length=50,
                            help_text = 'Enter the user_s name' 
                            )
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
        return reverse('event-detail', args = [str(self.id)])

class User(models.Model):
    name = models.CharField(
                            max_length=50,
                            help_text = 'Enter the user_s name' 
                            )
    passwd = models.CharField(
                            max_length=50,
                            help_text='enter a password'
                            )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user-detail', args = [str(self.id)])