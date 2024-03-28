from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student_Record,Books
from datetime import datetime,timedelta
from . import commonresponse,constants

class renew(APIView):
    def post(self,request):
        try:
            #check basic authentication
            authentication_classes = [BasicAuthentication]
            permission_classes = [IsAuthenticated]
            user=request.user
            email=user.email
            id=user.id
            data=request.data
            bookid=data.get('book_id')
            booknumber=data.get('book_number')
            #get the student record based on data provided
            student_books=Student_Record.objects.filter(book_id=bookid,renewed=False,user_id=id).first()
            student_books.renewed=True
            student_books.return_date=student_books.return_date+timedelta(days=constants.renewal_time)
            student_books.save()
            #update the return time for that particular book
            books=Books.objects.filter(id=bookid,book_number=booknumber).first()
            books.return_date_max=books.return_date_max+timedelta(days=constants.renewal_time)
            books.return_date_min=books.return_date_max+timedelta(days=constants.renewal_time)
            books.save()
            return commonresponse.success("Book Renewed successfully!!",None)
        except:
            return commonresponse.error(500,"Renewing the book failed!!",None)

