from django.db import models

# Create your models here.
class FormAuthor(models.Model):
    auth_name = models.CharField(max_length=40)

    def  _str_(self):
        return self.auth_name
class FormBook(models.Model):
    book = models.CharField(max_length=50)
    author = models.ForeignKey(FormAuthor,on_delete=models.CASCADE)
    price = models.IntegerField()
    book_image=models.ImageField(upload_to='book_images/',null=True,blank=True)
    def  _str_(self):
        return self.book


