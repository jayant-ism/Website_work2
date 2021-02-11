from django.shortcuts import render
from basic.models import connect
#from basic.models import User
from django.contrib.auth import authenticate, login #Django's inbuilt authentication methods
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from basic.models import Message 
from chat.serializers import Messageserilizer , user_details_serializer
import json
from datetime import date, time, datetime
from basic.models import user_details


from rest_framework.views import APIView

class datashow(APIView) : 
    def get(  self , request , user_id  ):
        
        details = user_details.objects.filter(id=int(user_id)).only( 'first_name' ,  'image' )
        
        serialize = user_details_serializer(details, many=True ) 
        print(serialize.data)
        return  JsonResponse( serialize.data, safe=False )

@csrf_exempt
def message_list(request, sender=None , receiver = None , viewss=None , idst = None ) :
    if request.method == 'GET' : 
        if viewss  : 
            messages = Message.objects.filter(  connect_id = receiver , id__range = [ idst + 1 , idst + 100000 ]   )    
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            Message.objects.filter(sender =  sender , connect_id= receiver ).update(is_read = 1 )
            print(serializer)
            return JsonResponse(serializer.data ,  safe=False )
        else :
            print(sender)
            print(receiver)
            messages = Message.objects.filter(connect_id  = receiver)  
            Message.objects.filter(sender =  sender , connect_id= receiver ).update(is_read = 1 )
            print(messages)
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            print(serializer)
            #Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            return JsonResponse(serializer.data ,  safe=False )
    elif request.method == 'POST' : 
        data = {}
        data["sender"] = request.POST['sender'] 
        data["connect_id"] = request.POST['connect_id'] 
        data ["message"] = request.POST["message"] 
        print(data)
        serializer =  Messageserilizer(data = data)
        if viewss is  None :
            print(data)
            sender = int(data['sender'])
            connect_id = int(data['connect_id'])
            messages = data['message']
            message = Message(message= messages ,  connect_id=connect_id , sender = sender  )
            message.save()
            serializer = Messageserilizer(message , many=False , context = {'request' : request})
            return JsonResponse(serializer.data , safe = False )
        if serializer.is_valid() :
            print("ok") 
            serializer.save()
            return JsonResponse(serializer.data ,  status=201)
        return JsonResponse(serializer.errors , status=400)
   

def chat_view(request):
    if request.method == "GET":
        
        return render(request, 'chat/chat.html',
                      {'users': connect.objects.filter(connect_status=1 , student_id=request.session['userid'] ) | connect.objects.filter(connect_status=1 , teacher_id=request.session['userid']) , 'sender' :  request.session['userid'] ,  'sender' :  request.session['userid'] }  ) 



def uploadfilechat(request) : 
    filename = {}


    file_field=request.FILES['post-text']
    file_name = request.FILES['post-text'].name
    print("sad")
    extension = '' 
    comment = file_name 
    file_name = reversed(file_name)  
    for i in file_name : 
        extension  = i + extension
        if i == '.' : 
            break  


    with open('media/storage/number.json') as json_file:


        data = json.load(json_file)
        asd = data['number']


    asd = int(asd) 
    asd = asd + 1 
    asd = str(  asd )  
    filename = 'media/storage/filenamess' + asd + extension 
    with open( filename ,  'wb+') as destination :   
        for chunk in file_field.chunks():
            destination.write(chunk)

    mydetails = { 'number' :  asd } 
    
    with open('media/storage/number.json' , 'w') as json_file:

        json.dump(mydetails, json_file)





    sender = int(request.POST['sender'])
    connect_id = int(request.POST['connect_id'])
    messages = filename
    message_type = 'file'
    message = Message(message= messages ,  connect_id=connect_id, sender = sender , message_type=message_type , comment=comment)
    message.save()



    serializer = Messageserilizer(message , many=False , context = {'request' : request})
    return JsonResponse(serializer.data , safe = False )    
    
    return  JsonResponse( filename , status =201 )
    
