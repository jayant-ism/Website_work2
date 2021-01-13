
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('api/messages/<int:sender>/<int:receiver>/<int:idst>/<int:viewss>' , views.message_list  , name="message-details"),  #for viewig messages
 path('api/messages' , views.message_list , name='message-list'),  #for adding messages 
 path('chat', views.chat_view, name='chats'),
 path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
 path('uploadfilechat', views.uploadfilechat, name='uploadfilechat'),
 #path('api/files', views.FileUploadView.as_view()),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

