#from basic.models import User
from rest_framework import serializers 
from basic.models import Message 

# start the serializer

class Messageserilizer(serializers.ModelSerializer) :
      class Meta : 
        model = Message 
        fields = ['sender', 'receiver' , 'message' , 'timestamp' , 'id' , 'message_type' , 'comment' , 'connect_id']

