from .models import Student_Record
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from . import commonresponse,util_time_format
import logging

logger=logging.getLogger('library') #centralized logging mechanism
class student(APIView):
    def get(self,request):
        logger.info("Entered into Student information GET method")
        try:
            authentication_classes = [BasicAuthentication]
            permission_classes = [IsAuthenticated]
            student_info=[]
            user=request.user
            borrowed=request.GET.get('borrowed') #Decides if the student wants to view only borrowed data or whole history
            id=user.id
            #get user id for student specific records
            borrowed_count=0
            query='''
                    select 1 as id,b.id as bookid,b.book_number as book_number,b.book_title as book_title ,b.author as author,sr.renewed as renewed,sr.return_date as return_date,sr.returned as returned,sr.returned_date as returned_date
                    From "Student_Record" sr
                    INNER JOIN "Books" b ON b.id=sr.book_id
                '''
            where_query='''where sr.user_id=%s '''
            group_query='''Group by sr.renewed,b.book_title,b.author,sr.return_date,b.book_number,b.id,sr.returned,sr.returned_date'''
            if borrowed:
                where_query=where_query+''' and sr.returned=FALSE ''' #conditional where query
            student_books=Student_Record.objects.raw(query+where_query+group_query,[id]) #execute raw query
            logger.info("Successfully executed raw query for fetching the student records")
            #read the records one by one
            for i in student_books:
                student_info.append({
                    "book_number":i.book_number,
                    "book_id":i.bookid,
                    "book_title":i.book_title,
                    "book_author":i.author,
                    "renewed":i.renewed,
                    "Returned": i.returned,
                    "Returned_date": util_time_format.custom_strftime(i.returned_date) if i.returned_date else None,
                    "return_date":util_time_format.custom_strftime(i.return_date),
                })
                if not i.returned:
                    borrowed_count=borrowed_count+1 
            #Implemented a macro for the commonresponse function to streamline and enhance code readability.
            logger.info("Book information retrieved successfully!!")
            return commonresponse.success("Books Infomation has been retrieved successfully.",{"Total_books_to_return":borrowed_count,"Books Boorowed":student_info})
        except Exception as e:
            logger.error(f"Entered into global exception method for student information method {str(e)}")
            return commonresponse.error(500,"Failed in fetching student information",None)