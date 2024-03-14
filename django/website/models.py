from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import models, User

class RegisterForm(UserCreationForm):
    email=models.EmailField()
    
    class Meta:
        model = User
        # to connect the user in the model
        fields=['username','email','password1','password2']
        # fields='__all__'


class Students(models.Model):
    s_name=models.CharField(max_length=100,null=True, blank=True) 
    # null =False this is for database, blank frontend
    s_email=models.EmailField(max_length=100,null=True, blank=True)
    s_phone=models.BigIntegerField(null=True, blank=True)
    s_entry_date=models.DateTimeField(auto_now_add=True)
    manager=models.Manager()
