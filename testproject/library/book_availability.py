from .models import Books
from rest_framework.views import APIView
from . import commonresponse,util_time_format
from django.db.models import Count,Case, When, IntegerField,Max,Min
import logging

logger=logging.getLogger('library') #centralized logging mechanism
class bookavailable(APIView):
    def get(self,request):
        logger.info("Entered into available books GET method")
        try: #Implemented a global try-except block to gracefully handle any unforeseen errors that may impede the performance of the code.
            books_obj=[]
            books_grouped = Books.objects.values('book_number','book_title','author').annotate(total=Count('book_number'),
                                            status_true_count=Count(Case(When(status=True, then=1), output_field=IntegerField())),
                                            min_return_date=Min('return_date_min'),
                                            max_return_date=Max('return_date_max'))
            logger.info("returned data from ORM query for books available method")
            for i in books_grouped:
                if i.get('status_true_count'):
                    books_obj.append({
                        'id':i.get('book_number'),
                        'name':i.get('book_title'),
                        'author':i.get('author'),
                        'total_number_of_copies':i.get('total'),
                        'number_of_copies_available':i.get('status_true_count'),
                        
                    })
                else:
                    books_obj.append({
                        'id':i.get('book_number'),
                        'name':i.get('book_title'),
                        'author':i.get('author'),
                        'total_number_of_copies':i.get('total'),
                        'number_of_copies_available':i.get('status_true_count'),
                        'min_availability_date':util_time_format.custom_strftime(i.get('min_return_date')),
                        'max_availability_date':util_time_format.custom_strftime(i.get('max_return_date'))
                    })
            logger.info("Successfully fetched the books data") 
            return commonresponse.success("Books Available in the Library",{"books_information":books_obj})
        except Exception as e:
            logger.error(f"Entered into global exception method for books available method {str(e)}")
            return commonresponse.error(500,"Failed in retrieving available books",None)