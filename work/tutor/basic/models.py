
from django.db import models

class user_login(models.Model) : 
    id  = models.IntegerField(primary_key=True  , blank = False , auto_created=True ) 
    first_name = models.CharField(max_length=15 , blank= False ) 
    last_name = models.CharField(max_length=15 , blank= False ) 
    email_id =models.CharField(max_length=15 , blank= False ) 
    pwd = models.CharField(max_length=15 , blank= False ) 

    class Meta:
        db_table = 'user_login'


class class_details(models.Model) : 
    class_id = models.IntegerField(primary_key=True  , auto_created=True)
    student_id = models.IntegerField()
    teacher_id  = models.IntegerField()
    class_details = models.IntegerField()


#lookup tables 

class level(models.Model) : 
    level =  models.CharField(max_length=15 , blank= False ) 
    id = models.IntegerField(primary_key=True)

class rating(models.Model) : 
    rating =  models.CharField(max_length=15 , blank= False ) 
    id = models.IntegerField(primary_key=True)

class designation(models.Model) : 
    level =  models.CharField(max_length=15 , blank= False ) 
    id = models.IntegerField(primary_key=True)


class language_list(models.Model) : 
     
    language = models.CharField(max_length=45, blank=False, )

    class Meta : 
        db_table = 'language_list'


#connect 


class connect_status(models.Model) : 
    id = models.IntegerField(primary_key=True) 
    connect_status = models.CharField(max_length=15)

class connect(models.Model):
    connect_id = models.IntegerField()
    class_id = models.IntegerField()
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()
    connect_status = models.IntegerField()
    connect_seek_rating = models.IntegerField()
    connect_teach_rating = models.IntegerField()
    connect_rate = models.IntegerField()



#main


class country(models.Model):
    country = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'country'
        



# needed





class user_details (models.Model) : 
    id = models.IntegerField(primary_key=True , auto_created=True )
    first_name = models.CharField(max_length=15, default=None , blank= False )
    last_name= models.CharField(max_length=15 , default=None , blank= False  )
    phone = models.DecimalField( max_digits=10 , decimal_places= 0 , default=None  )
    address = models.CharField(max_length=15 , default=None , blank= False )
    role = models.IntegerField( default=0 )
    seek_designation = models.CharField(max_length=15 , default=None , blank= False )
    teach_designation = models.CharField(max_length=15 , default=None , blank= False )
    seek_skills = models.JSONField()
    teach_skills = models.JSONField()
    country = models.CharField(max_length= 45 , default='India' , blank= False  )
    rate = models.DecimalField( max_digits = 5 , decimal_places= 4 , default=1  )
    rating = models.IntegerField( default=1 )
    level = models.IntegerField(default=1)
    image = models.FileField(upload_to='profile_images' , blank =True)
    language  =  models.CharField(blank=True ,max_length= 45)

    class Meta:
        db_table = 'user_details'


class skill(models.Model):
    skill_name = models.CharField(max_length=45, blank=True, null=True)
    skill_description = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(user_details, models.DO_NOTHING, blank=True, null=True)
    skills = models.JSONField()

    class Meta:
        db_table = 'skill'








class Message(models.Model) : 
    sender =models.CharField(max_length= 1200)
    receiver = models.CharField(max_length= 1200)
    message = models.CharField(max_length= 1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read =  models.BooleanField(default=False )
    id = models.AutoField(primary_key=True)
    message_type = models.CharField(default="text" , max_length=10)
    def __str__(self) : 
        return self.message
    class Meta : 
        ordering  = ('timestamp',) 


