from django import forms
from .models import Task
from .views import contact_manager, add_contact


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


from django import forms
from .models import StudentList


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

class AddContact(forms.ModelForm):
    class Meta:
        model = add_contact
        fields = ['Name','email','phone','address']
