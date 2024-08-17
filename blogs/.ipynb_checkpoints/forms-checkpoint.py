from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # 包含 title 和 text 字段
        fields = ['title','text']
        # 可以根据需要设置标签 
        labels = {
            'title':'Title',
            'text':'Content',
        }
        #设置颜色以西表格大小
        widgets = {'text':forms.Textarea(attrs={'cols':80,'rows': 10})}
