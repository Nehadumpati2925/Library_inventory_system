from django.contrib.auth.models import User
from . import commonresponse
from rest_framework.views import APIView
import uuid
from .models import Roles,UserProfile
from datetime import datetime
import logging

logger=logging.getLogger('library') #centralized logging mechanism
class createuser(APIView):
    def post(self,request):
        logger.info("Entered into user creation POST method")
        try: #Global try exception method
            data=request.data
            email=data.get('email')
            password=data.get('password')
            firstname=data.get('firstname')
            lastname=data.get('lastname')
            role=data.get('role')
            try:
                roles_obj=Roles.objects.get(name=str(role).capitalize()) #Checking if the role provided existsin the DB
            except:
                roles_obj=None
            user = User.objects.create_user(email=email, username=email,password=password,first_name=firstname,last_name=lastname,last_login=datetime.now()) #using django default basic authentication method to create user with role
            user.save()
            #adding role to the UserProfile which has one to one relation with the User method
            user_id=User.objects.get(email=email).id
            role=UserProfile(roles_id=roles_obj,user_id=user_id) 
            role.save()
            userdata={
                "user_id":user_id,
                "email":email,
                "username":email
            }
            logger.info(f"User Created Successfully for {userdata}")
            return commonresponse.success("User Created Successfully!!",{"userdata":userdata})
        except Exception as e:
            logger.error(f"Error in creating a user {str(e)}")
            return commonresponse.error("Failed in onboarding user",None)
