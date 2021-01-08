from django.shortcuts import render

from basic.models import User

from django.contrib.auth import authenticate, login #Django's inbuilt authentication methods
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from chat.models import Message 
from chat.serializers import Messageserilizer, Userserializer

import json
from datetime import date, time, datetime

@csrf_exempt
def user_list(request, pk=None )  :
    if request.method == 'GET' : 
        if pk :
            users = User.objects.filter(id=pk)
        else :
            users = User.objects.all()
        serializer  =  Userserializer(users, many=True , context = {'request' :  request })
        return JsonResponse(serializer.data, safe=False )
    elif request.method == 'POST' : 
        data = JSONParser().parse(request) 
        print("sd")
        serializer = Userserializer(data=data )
        print(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors , status = 400)
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
 #           Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            return JsonResponse(serializer.data ,  safe=False )
    elif request.method == 'POST' : 

        data = JSONParser().parse(request) 
        serializer =  Messageserilizer(data = data)
        print(data)


        if viewss is  None :
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
   

def index(request):
    if request.user.is_authenticated: #If the user is authenticated then redirect to the chat console
        return redirect('chats')
    if request.method == 'GET':
        return render(request, 'chat/index.html', {})
    if request.method == "POST": #Authentication of user
        username, password = request.POST['username'], request.POST['password'] #Retrieving username and password from the POST data.
        print(username )
        print(password)
        user = User.objects.filter(username=username, password=password ).exists()

        return redirect('chats')


        if user is not None:
            login(request, User)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('chats')


# Simply render the template
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'chat/register.html', {})

def chat_view(request):
    if request.method == "GET":
        return render(request, 'chat/chat.html',
                      {'users': User.objects.exclude(id=request.session['userid'] ), 'sender' : request.session['userid'] , 'receiver' : request.GET.get('receiver')  }) #Returning context for all users except the current logged-in user



#Takes arguments 'sender' and 'receiver' to identify the message list to return
def message_view(request, sender, receiver): 
    """Render the template with required context variables"""
#    if not request.user.is_authenticated:
#        return redirect('index')
    print("DS")
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username), #List of users
                       'receiver': User.objects.get(id=receiver), # Receiver context user object for using in template
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}) # Return context with message objects where users are either sender or receiver.
    if request.method == "POSt" :
        print("ok")  
        
        return  JsonResponse(Status = 200 )

@csrf_exempt 
def makeread(request , sender ,  receiver  ) :
    print("SAD")