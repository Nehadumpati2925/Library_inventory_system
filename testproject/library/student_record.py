from .models import Student_Record
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student_Record,Books
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from . import commonresponse
import uuid

class studentrecord(APIView):
    def post(self,request):
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]
        data=request.data
        email=data.get('email_id')
        book_id=data.get('book_id')
        book_number=data.get('book_number')
        borrowed_returned=data.get('borrowed/returned')
        try:
            userid=User.objects.get(email=email)
        except:
            return commonresponse.error(500,"No User data found!!",None)
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
        elif borrowed_returned=="returned":
            try:
                
                # books_available=list(Books.objects.filter(book_id=book_id,status=False))  #get the book id for the book_id provided 
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
        return commonresponse.success("Student record has been saved successfully",None)


