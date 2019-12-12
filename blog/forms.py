from django import forms
from blog.models import Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title",'description','created_date']

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title",'description']