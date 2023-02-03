from django import forms

g=[('male','male'),('female','female')]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(max_value=50)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea())
    gender=forms.ChoiceField(choices=g)