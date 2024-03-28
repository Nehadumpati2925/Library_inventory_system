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
        try:
            data=request.data
            email=data.get('email')
            password=data.get('password')
            firstname=data.get('firstname')
            lastname=data.get('lastname')
            role=data.get('role')
            try:
                roles_obj=Roles.objects.get(name=str(role).capitalize())
            except:
                roles_obj=None
            user = User.objects.create_user(email=email, username=email,password=password,first_name=firstname,last_name=lastname,last_login=datetime.now())
            user.save()
            user_id=User.objects.get(email=email).id
            role=UserProfile(roles_id=roles_obj,user_id=user_id)
            role.save()
            return commonresponse.success("User Created Successfully!!",None)
        except:
            return commonresponse.error("Failed in onboarding user",None)
