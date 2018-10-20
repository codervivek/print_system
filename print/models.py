from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PyPDF2 import PdfFileReader

# Create your models here.
class File(models.Model):

    name=models.CharField(max_length=150 ,help_text="Enter file name")
    user=models.ForeignKey(User, related_name="files", on_delete=models.CASCADE, help_text="a",default=1)
    
    mainFile=models.FileField(upload_to='uploads/item/photos/', help_text="Upload a file", null=True)

    isPrinted=models.BooleanField(default=False)
    noOfPages=models.IntegerField(default=0)

 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.mainFile.url

    def countPages(self):
        pdf = PdfFileReader(open('./'+ self.mainFile.url,'rb'))
        return pdf.getNumPages()