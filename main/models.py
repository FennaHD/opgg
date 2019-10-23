from django.db import models

# Create your models here.


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    def __str__(self):
        return self.tutorial_title



class ChampData(models.Model):
    champId = models.CharField(max_length=200)
    champName = models.CharField(max_length=200)
    champIconPath = models.CharField(max_length=200)

    def getChampId(self):
        return self.champId

    def getChampName(self):
        return self.champName

    def getChampIconPath(self):
        return self.champIconPath
