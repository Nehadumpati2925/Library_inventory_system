from .models import Student_Record,UserProfile,Roles
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from . import commonresponse,util_time_format

class librarianview(APIView):
    def get(self,request):
        try:
            authentication_classes = [BasicAuthentication]
            permission_classes = [IsAuthenticated]
            student_info=[]
            user=request.user
            email=user.email
            id=user.id
            studentid=request.GET.get('student_id')
            roleid=UserProfile.objects.get(user_id=id).roles_id_id
            role=Roles.objects.filter(id=roleid).first()
            where_query=''''''
            if role.name=="Librarian":
                borrowed_count=0
                query='''
                        select 1 as id,b.id as bookid,b.book_number as book_number,b.book_title as book_title ,b.author as author,sr.renewed as renewed,sr.return_date as return_date,sr.returned as returned,sr.returned_date as returned_date,u.email as emailid,sr.user_id as userid
                        From "Student_Record" sr
                        INNER JOIN "Books" b ON b.id=sr.book_id
                        INNER JOIN "auth_user" u ON u.id=sr.user_id
                    '''
                group_query='''Group by sr.renewed,b.book_title,b.author,sr.return_date,b.book_number,b.id,sr.returned,sr.returned_date,u.email,sr.user_id'''
                if studentid:
                    where_query=''' where sr.user_id=%s '''
                student_books=Student_Record.objects.raw(query+where_query+group_query,[studentid])
                for i in student_books:
                    student_info.append({
                        "book_number":i.book_number,
                        "book_id":i.bookid,
                        "book_title":i.book_title,
                        "book_author":i.author,
                        "renewed":i.renewed,
                        "Returned": i.returned,
                        "email":i.emailid,
                        "student_id":i.userid,
                        "Returned_date": util_time_format.custom_strftime(i.returned_date) if i.returned_date else None,
                        "return_date":util_time_format.custom_strftime(i.return_date),
                    })
                    if not i.returned:
                        borrowed_count=borrowed_count+1
                return commonresponse.success("Books Infomation has been retrieved successfully.",{"Total_books_to_return":borrowed_count,"Books Boorowed":student_info})
            else:
                return commonresponse.error(500,"Not Authorized",None)
        except:
            return commonresponse.error(500,"Error in fetching the student information",None)