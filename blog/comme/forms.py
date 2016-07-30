
from django import forms

from .models import Commentario

class CommentarioForm(forms.ModelForm):
    class Meta:
	model = Commentario
	fields = [
	 	    "commfield",
]