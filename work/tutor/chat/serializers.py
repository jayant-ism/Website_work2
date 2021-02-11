#from basic.models import User
from rest_framework import serializers 
from basic.models import Message , user_details 

# start the serializer

class Messageserilizer(serializers.ModelSerializer) :
      class Meta : 
        model = Message 
        fields = ['sender', 'receiver' , 'message' , 'timestamp' , 'id' , 'message_type' , 'comment' , 'connect_id']



class user_details_serializer(serializers.ModelSerializer) : 
      class Meta : 
        model = user_details 
        fields = [ 'first_name' ,  'image'] 