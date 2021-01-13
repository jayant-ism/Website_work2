import pandas as pd
from django.conf import settings
from django.db import models



 #models when the csv files will be extracted

class Schedule_extract(models.Model) :
    Version	= models.DecimalField(max_digits=12, decimal_places=6)
    SourceSystem	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CreateDate	= models.DateTimeField()
    MarketStatus	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Region	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketParticipant	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketStage	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FirstIntervalBegin	= models.DateTimeField()
    LastIntervalEnd	= models.DateTimeField()
    IntervalLength	= models.CharField(max_length=32, default=None, null=True, blank=True)
    TransactionType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Location	= models.CharField(max_length=32, default=None, null=True, blank=True)
    ProductType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FromInterval = models.IntegerField() #this is to be changed
    MW	= models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)
    Status	= models.CharField(max_length=32, default=None, null=True, blank=True) 
    Message = models.CharField()

class Curvepoint_extract(models.Model) : 
    
    Version	= models.DecimalField(max_digits=12, decimal_places=6)
    SourceSystem	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CreateDate	= models.DateTimeField()
    MarketStatus	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Region	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketParticipant	= models.CharField(max_length=32 ,blank= True)
    MarketStage	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FirstIntervalBegin	= models.DateTimeField()
    LastIntervalEnd	= models.DateTimeField()
    IntervalLength	= models.CharField(max_length=32, default=None, null=True, blank=True)
    TransactionType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Location	= models.CharField(max_length=32, default=None, null=True, blank=True)
    ProductType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FromInterval = models.IntegerField() #this is to be changed
    MW	= models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)
    Status	= models.CharField(max_length=32, default=None, null=True, blank=True) 
    Message = models.CharField(max_length=32, default=None, null=True, blank=True)
    BidName	= models.CharField(max_length=32, default=None, null=True, blank=True)
    LinkedOfferID	= models.IntegerField(blank=True)
    CurveType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CooptimizedWithAS = models.BooleanField(blank=True)
    Price = models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)


# final models that will be saved 
 
class Shedule(models.Model) :  
    Version	= models.DecimalField(max_digits=12, decimal_places=6)
    SourceSystem	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CreateDate	= models.DateTimeField()
    MarketStatus	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Region	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketParticipant	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketStage	= models.CharField(max_length=32, default=None, null=True, blank=True)
    IntervalBegin	= models.DateTimeField()
    IntervalEnd	= models.DateTimeField()
    IntervalLength	= models.CharField(max_length=32, default=None, null=True, blank=True)
    TransactionType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Location	= models.CharField(max_length=32, default=None, null=True, blank=True)
    ProductType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FromInterval = models.IntegerField() #this is to be changed
    MW	= models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)
    Status	= models.CharField(max_length=32, default=None, null=True, blank=True) 
    Message = models.CharField()

class Curvepoint_extract(models.Model) : 
    
    Version	= models.DecimalField(max_digits=12, decimal_places=6)
    SourceSystem	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CreateDate	= models.DateTimeField()
    MarketStatus	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Region	= models.CharField(max_length=32, default=None, null=True, blank=True)
    MarketParticipant	= models.CharField(max_length=32 ,blank= True)
    MarketStage	= models.CharField(max_length=32, default=None, null=True, blank=True)
    IntervalBegin	= models.DateTimeField()
    IntervalEnd	= models.DateTimeField()
    IntervalLength	= models.CharField(max_length=32, default=None, null=True, blank=True)
    TransactionType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    Location	= models.CharField(max_length=32, default=None, null=True, blank=True)
    ProductType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    FromInterval = models.IntegerField() #this is to be changed
    MW	= models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)
    Status	= models.CharField(max_length=32, default=None, null=True, blank=True) 
    Message = models.CharField(max_length=32, default=None, null=True, blank=True)
    BidName	= models.CharField(max_length=32, default=None, null=True, blank=True)
    LinkedOfferID	= models.IntegerField(blank=True)
    CurveType	= models.CharField(max_length=32, default=None, null=True, blank=True)
    CooptimizedWithAS = models.BooleanField(blank=True)
    Price = models.DecimalField(max_digits=12, decimal_places=6, default=None, null=True, blank=True)


class data_model(models.Model) : 
    