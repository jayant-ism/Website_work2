from django.db import models
from basic.models import User

class Message(models.Model) : 
    sender =models.CharField(max_length= 1200)
    receiver = models.CharField(max_length= 1200)
    message = models.CharField(max_length= 1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read =  models.BooleanField(default=False )
    id = models.AutoField(primary_key=True)
    def __str__(self) : 
        return self.message
    class Meta : 
        ordering  = ('timestamp',) 
