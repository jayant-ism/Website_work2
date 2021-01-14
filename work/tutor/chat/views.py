from django.shortcuts import render
#from basic.models import User
from django.contrib.auth import authenticate, login #Django's inbuilt authentication methods
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from chat.models import Message 
from chat.serializers import Messageserilizer
import json
from datetime import date, time, datetime




@csrf_exempt
def message_list(request, sender=None , receiver = None , viewss=None , idst = None ) :
    if request.method == 'GET' : 
        if viewss  : 
            messages = Message.objects.filter(sender = sender ,  receiver = receiver , id__range = [ idst + 1 , idst + 100000 ]   )  | Message.objects.filter(sender = receiver ,  receiver =  sender, id__range = [ idst + 1 , idst + 100000 ]   )  
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            print(serializer)
            return JsonResponse(serializer.data ,  safe=False )
        else :
            print(sender)
            print(receiver)
            messages = Message.objects.filter(sender = sender ,  receiver = receiver) | Message.objects.filter(sender = receiver , receiver= sender ) 
            Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            print(messages)
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            print(serializer)
            #Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            return JsonResponse(serializer.data ,  safe=False )
    elif request.method == 'POST' : 
        data = JSONParser().parse(request) 
        print("sad")
        print(data)

        serializer =  Messageserilizer(data = data)
        if viewss is  None :
            print(data)
            sender = int(data['sender'])
            receiver = int(data['receiver'])
            messages = data['message']
            message = Message(message= messages ,  receiver = receiver , sender = sender  )
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
                      {'users': User.objects.exclude(id=request.session['userid'] ), 'sender' : request.session['userid'] , 'receiver' : request.GET.get('receiver')  }) #Returning context for all users except the current logged-in user



def uploadfilechat(request) : 
    filename = {}
#    return  JsonResponse( filename , status =201 )
    

    file_field=request.FILES['post-text']
    with open('media/storage/number.json') as json_file:


        data = json.load(json_file)
        asd = data['number']


    asd = int(asd) 
    asd = asd + 1 
    asd = str(  asd )  
    filename = 'media/storage/filenamess' + asd + '.py' 
    with open( filename ,  'wb+') as destination :   
        for chunk in file_field.chunks():
            destination.write(chunk)

    mydetails = { 'number' :  asd } 
    
    with open('media/storage/number.json' , 'w') as json_file:

        json.dump(mydetails, json_file)





    sender = int(request.POST['sender'])
    receiver = int(request.POST['receive'])
    messages = filename
    message_type = 'file'
    message = Message(message= messages ,  receiver = receiver , sender = sender , message_type=message_type )
    message.save()


    
    filename = {'url' : filename}
    return  JsonResponse( filename , status =201 )
    
