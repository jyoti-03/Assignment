from django import forms  
from myapp.models import Login 
  
class LoginForm(forms.ModelForm):  
    class Meta:  
        model = Login  
        fields = "__all__"  

