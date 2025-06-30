from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name
    class Meta:
        verbose_name='Authors'
        verbose_name_plural='Authors'

class Book(models.Model):
    name=models.CharField(max_length=100,null=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField()

    def _str_(self):
        return self.name
    class Meta:
        verbose_name='Books'
        verbose_name_plural='Books'

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=89)