from django.urls import path,include
from . import create_users, student_info, views,book_availability,student_record,renew_books,librarian_view

urlpatterns = [
    path('', views.healthCheck),
    path('create-user',create_users.createuser.as_view()),
    path('books-available',book_availability.bookavailable.as_view()),
    path('student-info',student_info.student.as_view()),
    path('student-record',student_record.studentrecord.as_view()),
    path('renew',renew_books.renew.as_view()),
    path('librarian-view',librarian_view.librarianview.as_view())]
