from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']

from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']

# from django import forms
# from .models import Marks

from django import forms
from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']