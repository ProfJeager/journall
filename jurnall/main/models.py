from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=550)
    owner = models.CharField('Owner', max_length=250)
    datenow = models.DateField("Published")
    c_name = models.CharField('Enter certificate name', max_length=2048)
    file_name = models.CharField("File name", max_length=550)

    articlesnumber = models.CharField("Articles number", max_length=1024)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
class Certificate(models.Model):

    certificate_file = models.FileField(upload_to='certificates/')

class UploadFile(models.Model):
    file = models.FileField(upload_to='')
