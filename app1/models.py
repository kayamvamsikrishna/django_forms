from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return str(self.topic_name)


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=False)
    url=models.URLField(max_length=50,unique=True)

    def __str__(self):
        return str(self.name)

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()


    def __str__(self):
        return str(self.name)


