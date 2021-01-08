
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('api/messages/<int:sender>/<int:receiver>/<int:idst>/<int:viewss>' , views.message_list  , name="message-details"),  #for viewig messages
 path('api/messages' , views.message_list , name='message-list'),  #for adding messages 
 path('api/users/<int:pk>' ,  views.user_list , name = 'user-details'),
 path('api/users', views.user_list, name='user-list') ,
 path('chat', views.chat_view, name='chats'),
 path('register', views.register_view, name='register'),
 path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

