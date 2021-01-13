import xml.etree.ElementTree as ET
from models import Schedule_extract

def doi(root  , modelname , past )  :
    #get the tag of the root 
    tagname =   root.tag  
    attr = root.attrib  
    # add the past data to this list 
    if past is not None : 
        for i in past.keys() : 
            attr[i] = past[i]
    #check if the it is the destination 
    leng = len(modelname ) +1
    last_n =  tagname[-leng :] 
    if last_n == "}" + modelname  :
        return [ attr ]  
    ans = [] 
    for child in root : 
        ans =  ans +  doi(child ,  modelname , attr ) 
    return  ans  

    
def retdic(modelname ,   file_url)  : 
    tree = ET.parse(file_url)
    ans = []
    root = tree.getroot() 
    if root  is None  : 
        return ans
    ans = doi(root , modelname , {} )
    return ans  



data =  retdic('Schedule' , 'testori.xml' ) 
refine = []
for i in data :
    obj =  Schedule_extract.objects.create()
    obj.Version	= i['Version']
    obj.SourceSystem	= i['SourceSystem'] 
    obj.CreateDate	= i['CreateDate']
    obj.MarketStatus	= i['MarketStatus']
    obj.Region	= i['Region']
    obj.MarketParticipant	= i['MarketParticipant']
    obj.MarketStage	= i['MarketStage']
    obj.FirstIntervalBegin	=i['FirstIntervalBegin'] 
    obj.LastIntervalEnd	= i['LastIntervalEnd']
    obj.IntervalLength	= i['IntervalLength']
    obj.TransactionType	= i['TransactionType']
    obj.Location	= i['Location']
    obj.ProductType	= i['ProductType']
    obj.FromInterval = i['FromInterval']
    obj.MW	= i['MW']
    obj.Status	=  i['Status']
    obj.Message = i['Message']
    obj.save()

