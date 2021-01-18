from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import user_details , country  , language_list
from itertools import chain
import json
from django.core.paginator import Paginator
from django import template
# Create your views here.


def index(request , user_id) : 
    request.session['userid'] = user_id
    return redirect('search')
    return render( request , 'index.html' , {'se' : asd })
def search(request) :
    
    user_id = str(  request.session['userid'] )
    #print(user_id)
    usersd = " select id , role from user_details where id = " + user_id + "  ; "
    print(usersd)
    user_type =  user_details.objects.raw(usersd )
     
    for i in user_type : 
        type_user =  i.role 
        #print(i.role )   

    #we got the user type 

    required_string = " * " 
    tables_used = " user_details "
    condition_string = ""
    #set user type 
    user_type = int( type_user ) 
    user_type = 1 + (user_type )%2  
    user_type  = str(  user_type )
    condition_string = condition_string  + "  role =  " + user_type + " " 

    #we need the details of only user type 

    #set the hourly rate 
    hourly_query = ""
    add_on = 0  
    if  request.GET.get('hourlyrate1')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( rate < 5  )  " 
    
    
    if  request.GET.get('hourlyrate2')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( rate  >=  5 and rate  < 10  )  " 
    
    
    if  request.GET.get('hourlyrate3')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( rate >= 10 and rate  < 100    )  " 
    
    
    if  request.GET.get('hourlyrate4')  :
        if add_on == 1 : 
            hourly_query = hourly_query + " or " 

        add_on = 1  

        hourly_query = hourly_query + " ( rate >= 100  )  " 
    
    


    if len (hourly_query ) : 
        hourly_query =  " and  ( " + hourly_query + " ) " 
    

    #now add the value of the location

    if request.GET.get('location') : 
        condition_string = condition_string + "  and  " + "  country = " + " '" + request.GET.get('location') + "' " 


    #now add the value of the language

    if request.GET.get('language') : 
        condition_string = condition_string + "  and  " + "  language = " + " '" + request.GET.get('language') + "' " 

    #now add the value of the talent 


    talent_query = ""
    add_on = 0  
    if  request.GET.get('Beginner')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( level = 1 )  " 
    
    if  request.GET.get('Intermediate')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( level = 2)  " 
    
    if  request.GET.get('Expert')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( level = 3 )  " 
    if  request.GET.get('Super Expert')  :
        if add_on == 1 : 
            talent_query = talent_query + " or " 

        add_on = 1  

        talent_query = talent_query + " ( level = 4 )  " 
    
    


    if len (talent_query ) : 
        talent_query =  " and  ( " + talent_query + " ) " 
    


    # add the search string 
    fname = request.GET.get('fname')
    if fname is None : 
        fname = '' 
    fname = fname.lower()
    if user_type == 1 : 
        search_string = " and (  LOWER (first_name  ) REGEXP '" + "^" + fname + "' or LOWER (  last_name ) REGEXP '^" + fname +"' "  +   " or LOWER( seek_skills ) REGEXP LOWER ( '" + fname + "' )" + ")" 
    else  :
        search_string = " and (  LOWER (first_name  )  REGEXP '" + "^" + fname + "' or LOWER(  last_name ) REGEXP  '^" + fname +"' "  +   " or LOWER( teach_skills ) REGEXP LOWER ( '" + fname + "' )" + ")" 
        
    # add the skill string 




    if fname == '' :
        search_string = ""

    cla = request.GET.get('section') 
    if cla != None :
        if user_type ==  1 : 
            search_string = search_string   + " and seek_designation = '" + cla + "'"
        else :
            search_string = search_string   + " and teach_designation = '" + cla + "'"


    query_string = " select  " + required_string + "  from  "  +  tables_used + " where  "  + condition_string + hourly_query  + talent_query + search_string + " ; "
    print(query_string)
    bsd =  user_details.objects.raw( query_string )

    pgno = 1
    try : 
        pgno = int(request.GET.get('page') )
    except :
        pgno  = 1 
    data = Paginator(bsd  , 2 )
    asd = data.page(pgno)


    if asd != None : 
        for i in asd : 
            if user_type == 1 : 
                if i.teach_skills == None : 
                    i.skill = {}
                    continue  
                print(i.teach_skills)
                i.skill =  i.teach_skills


    locations = country.objects.all()
    language_list_ht =  language_list.objects.all()


    #inputs


    inputs = {}
    try : 
        inputs['search_bar']   =  fname
    except : 
        inputs['search_bar'] =''
        
    try : 
        if request.GET.get('hourlyrate1') :
            inputs['hourlyrate1']   =  1 
        else : 
            inputs['hourlyrate1'] = 0 
    except : 
        inputs['hourlyrate1'] = 0
    try : 
        if request.GET.get('hourlyrate2') :
            inputs['hourlyrate2']   =  1 
        else : 
            inputs['hourlyrate2'] = 0 
    except : 
        inputs['hourlyrate2'] = 0
    try : 
        if request.GET.get('hourlyrate3') :
            inputs['hourlyrate3']   =  1 
        else : 
            inputs['hourlyrate3'] = 0 
    except : 
        inputs['hourlyrate3'] = 0
    try : 
        if request.GET.get('hourlyrate4') :
            inputs['hourlyrate4']   =  1 
        else : 
            inputs['hourlyrate4'] = 0 
    except : 
        inputs['hourlyrate4'] = 0
    try : 
        if request.GET.get('Beginner') :
            inputs['Beginner']   =  1 
        else : 
            inputs['Beginner'] = 0 
    except : 
        inputs['Beginner'] = 0
    try : 
        if request.GET.get('Intermediate') :
            inputs['Intermediate']   =  1 
        else : 
            inputs['Intermediate'] = 0 
    except : 
        inputs['Intermediate'] = 0
    try : 
        if request.GET.get('Expert') :
            inputs['Expert']   =  1 
        else : 
            inputs['Expert'] = 0 
    except : 
        inputs['Expert'] = 0
    try : 
        if request.GET.get('Super Expert') :
            inputs['Super_Expert']   =  1 
        else : 
            inputs['Super_Expert'] = 0 
    except : 
        inputs['Super_Expert'] = 0
    try : 
         inputs['location'] =  request.GET.get('location')
    except : 
        inputs['location'] =''
    try : 
        inputs['language'] = request.GET.get('language')
    except : 
        inputs['language'] =''
    if inputs['language'] == None : 
        inputs['language'] = '' 
    if inputs['location'] == None : 
        inputs['location'] = ''
    
    try :
        inputs['section'] = request.GET.get('section')
    except :
        inputs['section'] =None
    try : 
        inputs['nextpage'] = int(request.GET.get('page') ) +1

    except :
        inputs['nextpage'] = 2
    
    if asd.has_next() == False  :
        inputs['nextpage'] = None 
    try : 
        inputs['prepage'] = int(request.GET.get('page') ) - 1
         
    except :
        inputs['prepage'] = None
        
    if asd.has_previous() == False  : 
        inputs['prepage'] = None 

    return render( request , 'index.html' , {'inputs':inputs , 'se' : asd , 'type' : type_user , 'locations' : locations , 'language_list_ht' : language_list_ht ,'pre' :   hourly_query  + talent_query + search_string    })

