from django.forms import ModelForm
from .models import Blogs
from .serializers import BlogSerializer


class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'blog_content']



