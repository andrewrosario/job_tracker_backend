from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    tech_stack = models.TextField()
    
def __str__(self):
    return '%s %s' % (self.name, self.tech_stack)
