#from basic.models import User
from rest_framework import serializers 
from chat.models import Message 

# start the serializer

class Messageserilizer(serializers.ModelSerializer) :
      class Meta : 
        model = Message 
        fields = ['sender', 'receiver' , 'message' , 'timestamp' , 'id' , 'message_type']

