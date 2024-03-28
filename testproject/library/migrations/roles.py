from django.db import migrations
from library.models import Roles
import datetime

class Migration(migrations.Migration):
    dependencies = [
        ('library', '0001_initial'),
    ]
    
    def insertData(apps, schema_editor):
        # INsert the data which is required for subscriptions
        bulk_mgr = [] 
        bulk_mgr.append(Roles(id = '76fa9d1a-07e9-4d3c-9dbb-b75c7e2d36db' ,name = "Librarian", status=True))
        bulk_mgr.append(Roles(id = 'e46a92c3-f53d-406c-a94b-c732af88650d' ,name = "Student", status=True))
        bulk_mgr.append(Roles(id = '8c3bc852-d66f-4fb6-8d80-e1db407c27b0' ,name = "Anonymous", status=True))
        Roles.objects.bulk_create(bulk_mgr)

    operations = [
        migrations.RunPython(insertData),
    ]
