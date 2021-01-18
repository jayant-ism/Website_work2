from django.contrib import admin
#from .models import image
from .models import user_details  , user_login  , level ,  rating , designation  , language_list  , connect_status  , connect ,  skill 


# Register your models here.
#admin.site.register(image)

admin.site.register(user_login)
admin.site.register(user_details)
