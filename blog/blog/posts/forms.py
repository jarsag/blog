


from django import forms

from .models import Post, Commentario


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
		]

class CommentarioForm(forms.ModelForm):
	class Meta:
		model = Commentario
		fields = [
	 	    "commfield",
]