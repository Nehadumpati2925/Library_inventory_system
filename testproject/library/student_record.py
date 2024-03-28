from .models import Student_Record,UserProfile,Roles
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student_Record,Books
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from . import commonresponse
import uuid
import logging

logger=logging.getLogger('library') #centralized logging mechanism
class studentrecord(APIView):
    def post(self,request):
        logger.info("Entered into Student Record update POST method")
        try:
            authentication_classes = [BasicAuthentication]
            permission_classes = [IsAuthenticated]
            #read inputs from payload
            data=request.data
            user=request.user
            id=user.id
            email=data.get('email_id')
            book_id=data.get('book_id')
            book_number=data.get('book_number')
            borrowed_returned=data.get('borrowed/returned')
            
            roleid=UserProfile.objects.get(user_id=id).roles_id_id
            role=Roles.objects.filter(id=roleid).first()
            if role.name=="Librarian": #check if the person is authorized for student record update
                try:
                    userid=User.objects.get(email=email)
                except:
                    return commonresponse.error(500,"No User data found!!",None)
                #borrowed method
                if borrowed_returned=="borrowed":
                    bookid=Books.objects.filter(id=book_id,status=True,book_number=book_number).first()
                    if not bookid:
                        return commonresponse.error(500,"Book not available!!",None)
                    try:

                        currentstatus=Student_Record.objects.filter(user_id=userid.id).order_by('-borrowed_date').first() #check the total number of books based on the latest data updated
                        numberofbooks=currentstatus.number_of_books
                    except:
                        numberofbooks=0
                    #Update the student record with book details
                    studentrecord=Student_Record(id=uuid.uuid4(),user_id=userid,book_id=bookid,borrowed_date=datetime.now(),return_date=datetime.now()+timedelta(days=30),renewed=False,number_of_books=numberofbooks+1,returned=False)
                    studentrecord.save()
                    #update the allocated book as availability False
                    Books.objects.filter(id=bookid.id).update(status=False,return_date_min=datetime.now()+timedelta(days=30),return_date_max=datetime.now()+timedelta(days=60))
                elif borrowed_returned=="returned": #returned method
                    try:
                        #Update the student record with return status
                        currentstatus=Student_Record.objects.filter(user_id=userid.id,returned=False,book_id=book_id).first() #check the total number of books based on the latest data updated
                        currentstatus.number_of_books=currentstatus.number_of_books-1
                        currentstatus.returned=True
                        currentstatus.returned_date=datetime.now()
                        currentstatus.save()
                    except Exception as e:
                        return commonresponse.error(500,"Error in updating return status!!",None)
                    #update the allocated book as availability False
                    Books.objects.filter(id=book_id,book_number=book_number).update(status=True)
                logger.info("Student record updated successfully!!")
                return commonresponse.success("Student record has been saved successfully",None)
            else:
                return commonresponse.error(500,"Not Authorized",None)
        except Exception as e:
            logger.error(f"Entered global exception method for student record update {str(e)}")
            return commonresponse.error(500,"Failed in updating student record",None)

