from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	text = forms.CharField(max_length=50, 
		widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Enter todo e.g. Delete junk files',
		'aria-label':'Todo', 'aria-describedby':'add-btn'}))

	class Meta:
		model = Todo
		fields = ['text']