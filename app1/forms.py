from django import forms
from app1.models import *
class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)

    def __str__(self):
        return str(self.topicname)

class WebpageForm(forms.Form):#
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()

    def __str__(self):
        return str(self.name)

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()

    def __str__(self):
        return str(self.data)