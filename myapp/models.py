from django.db import models

# Create your models here.
class Post(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username


class calci(models.Model):
    n1 = models.IntegerField(max_length=5)
    n2 = models.IntegerField(max_length=5)

    def __str__(self):
        return self.n1

class book(models.Model):
    author = models.CharField(max_length=100)
    # description of the watch
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    created_date = models.CharField(max_length=300)
    published_date = models.CharField(max_length=300)

    def __str__(self):
        return self.author

class books(models.Model):
    author = models.CharField(max_length=100)
    # description of the watch
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    created_date = models.DateField()
    published_date = models.DateField()

    def __str__(self):
        return self.author