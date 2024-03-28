from django.db import migrations
from library.models import Books
from django.contrib.auth.models import User



class Migration(migrations.Migration):
    dependencies = [
        ('library', 'roles'),
    ]
    
    def insertData(apps, schema_editor):
        # INsert the data which is required for subscriptions
        bulk_mgr = [] 
        default_user=User.objects.get(id='1')
        bulk_mgr.append(Books(id = 'b242b762-cc66-402c-91f1-13d98a672a7f' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '0b74a9b8-92af-4f0a-aa71-88c054b2cfdc' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'd7245322-e5ba-4b2b-92f8-9a0a3ac09a4a' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'd352d736-a765-472f-bf2b-d7fd76e2f478' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'cb8b3e52-c4e6-40d2-859b-c14be008571a' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '2e78410f-0915-4716-ae68-211a52d56ed7' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '34cb1a99-ac16-4b22-9d36-e9e8a898d69b' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '3039846f-b31e-4436-9335-d7dc603bb038' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'd8f3c16a-31c9-4665-a489-50438aca8ef3' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '73f4c5bc-1e8b-4bb7-b98d-240eb6c1c4c8' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '9e52a49a-1f34-45bc-9d83-6987f293f98a' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'a1545dbc-e4e1-4d54-8a53-10f23b74583b' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '85030277-9aa6-41b0-a44f-2aa24668c0f9' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'c2a52a15-6567-49fe-a582-4ae85f9f40f6' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'ca5a507c-0d5f-4b8d-bf42-058d5bff517a' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '2753601b-21b5-45a7-881e-adb92b18e92f' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '32b2aaf4-d9bf-4388-8c5f-2aa56e3cc907' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '57abf4d5-fe57-44f7-87ff-966ad90074ee' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '80b7d446-f33e-40e2-8c93-d549fe3f4a25' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'e739c984-1f5b-445d-be21-453abee0723e' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '6c86be4f-fb04-4eaf-af9f-2dd69435dc34' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'a846cf1c-4176-4a99-b134-b94d6fdf4391' ,book_title = "Computer Networking: A Top-Down Approach", book_number=2,author="James F. Kurose",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '7863d225-4bd4-430d-bdac-ecb0ad4ac1be' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '427f3d72-e150-4233-9ad7-384f4c4d7948' ,book_title = "Database System Concepts",book_number=4,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '2dfc5c01-a3d8-49a6-ab96-0142c166d1e8' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '8ffc5d84-b264-4c9d-bce0-c3c69f3f34a1' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'dafde276-c393-44cc-9de2-5af9aac0bdca' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '48b41e4e-9c3c-4467-be25-f8a08a3fa5b9' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '9324bf43-3caa-4064-b116-213383de070a' ,book_title = "Introduction to Algorithms", book_number=1,author="Thomas H. Cormen",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'cf53a96d-52b7-4407-ab44-a47bd59245e3' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = 'a38867f1-c50c-4db5-89f5-56c5199fa217' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))
        bulk_mgr.append(Books(id = '4f4f44c6-2081-4717-97ab-d68b6c79928b' ,book_title = "Operating System Concepts", book_number=3,author="Abraham Silberschatz",added_by=default_user,last_modified_by=default_user,status=True))

        Books.objects.bulk_create(bulk_mgr)

    operations = [
        migrations.RunPython(insertData),
    ]
