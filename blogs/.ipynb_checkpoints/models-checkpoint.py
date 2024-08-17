from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """创建BlogPost模型"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
#管理界面的显示
    def __str__(self):
        """返回模型的字符串显示"""
        if len(self.title) < 50:
            title_str = self.title
        else:
           title_str = self.title[:50]+"..."
       
        return f"{title_str} by {self.owner.username}"