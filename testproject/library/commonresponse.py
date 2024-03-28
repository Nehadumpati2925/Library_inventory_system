from django.http import HttpResponse, JsonResponse
from rest_framework import status

#A macro for the JSONresponse function to streamline and enhance code readability.
def success(message, data):
    return JsonResponse(
        {
             "status": status.HTTP_200_OK, 
             "message": message, 
              "data": data
        },
        status=status.HTTP_200_OK
    )

def error(status_code, message, data):
    return JsonResponse(
        {
             "status": status_code, 
             "message": message, 
              "data": data
        },
        status=status_code
    )    