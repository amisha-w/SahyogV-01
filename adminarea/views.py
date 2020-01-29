from django.shortcuts import render
import pymongo
import os
from dotenv import load_dotenv





# from twilio.rest import Client


# Create your views here.
client = pymongo.MongoClient("mongodb+srv://"+str(os.getenv("USER"))+":"+str(os.getenv("PASSWORD"))+"@devcluster-qbbgy.mongodb.net/Sahyog?retryWrites=true&w=majority")
db = client.Sahyog
validateDB = db.Validate




def admindashboard(request):
    

    return render(request,'adminarea/index.html')


def validators(request):
   
    if request.method == "POST":
        print("POST HITTED")
        location = request.POST.get('Location')
        print(location)
        validations = list(validateDB.find({'location':location}))
        print(validations)
        return render(request,'adminarea/validators.html',status=200,context={'context':validations})

    else:
        return redirect('admindashboard')





    
    
    


    
         
    


        
    

# def makeCall(request):
    
#     # Your Account Sid and Auth Token from twilio.com/console
#     # DANGER! This is insecure. See http://twil.io/secure
#     account_sid = 'ACc4b67eb6c1d521f75d927122e60e1719'
#     auth_token = 'b541bf5e349b93c95d0e1556bc77b2ba'
#     client = Client(account_sid, auth_token)

#     call = client.calls.create(
#                             url='http://demo.twilio.com/docs/voice.xml',
#                             to=,
#                             from_='+15017122661'
#                         )

#     print(call.sid)
#     return 

