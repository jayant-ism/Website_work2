# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



#new  

class user_login(models.Model) : 
    id  = models.IntegerField(primary_key=True  , blank = False , auto_created=True ) ,
    first_name = models.CharField(max_length=15 , blank= False ) ,
    last_name = models.CharField(max_length=15 , blank= False ) ,
    email_id =models.CharField(max_length=15 , blank= False ) ,
    pwd = models.CharField(max_length=15 , blank= False ) ,

class class_details(models.Model) : 
    class_id = models.IntegerField(primary_key=True  , auto_created=True)
    student_id = models.IntegerField()
    teacher_id  = models.IntegerField()
    class_details = models.IntegerField()


#lookup tables 

class level(models.Model) : 
    level =  models.CharField(max_length=15 , blank= False ) ,
    id = models.IntegerField(primary_key=True)

class rating(models.Model) : 
    rating =  models.CharField(max_length=15 , blank= False ) ,
    id = models.IntegerField(primary_key=True)

class designation(models.Model) : 
    level =  models.CharField(max_length=15 , blank= False ) ,
    id = models.IntegerField(primary_key=True)


class language_list(models.Model) : 
     
    language = models.CharField(max_length=45, blank=False, )

    class Meta : 
        db_table = 'language_list'


class Country(models.Model):
    country = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

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



class Profile(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    skype_id = models.CharField(max_length=45, blank=True, null=True)
    skill_id = models.IntegerField(blank=True, null=True)
    experience = models.CharField(max_length=45, blank=True, null=True)
    current_position = models.CharField(max_length=45, blank=True, null=True)
    portfolio_link = models.CharField(max_length=100, blank=True, null=True)
    hours_per_week = models.CharField(max_length=45, blank=True, null=True)
    resume_url = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    language = models.CharField(max_length= 45 , default= "English" , blank= False)
    class Meta:
        managed = False
        db_table = 'profile'


class Skill(models.Model):
    skill_name = models.CharField(max_length=45, blank=True, null=True)
    skill_description = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    skills = models.JSONField()

    class Meta:
        managed = False
        db_table = 'skill'


class State(models.Model):
    state = models.CharField(max_length=45, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'

class user(models.Model) : 
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    phone = models.DecimalField( max_digits=10 , decimal_places= 0  )
    address = models.CharField(max_length=15)
    role = models.CharField(max_length=15)
    seek_designation = models.CharField(max_length=15)
    teach_designation = models.CharField(max_length=15)
    seek_skills = models.JSONField()
    teach_skills = models.JSONField()
    country = models.IntegerField()
    rate = models.DecimalField( max_digits = 5 , decimal_places= 4 )
    rating = models.IntegerField()
    level = models.IntegerField()
    image = models.CharField(max_length=15)
