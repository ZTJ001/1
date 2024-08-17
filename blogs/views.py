from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import BlogPost
from .forms import BlogForm

def index(request):
    """主页内容"""
    return render(request,'blogs/index.html')

def blogs(request):
    """显示所有blog标题"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request,'blogs/blogs.html',context)

def blog(request,blog_id):
    """显示每个blog的内容，并检查用户是否可以编辑它"""
    blog = get_object_or_404(BlogPost,id=blog_id)
    text = blog.text
    # 检查当前用户是否可以编辑这个博客  
    can_edit = request.user.is_authenticated and request.user == blog.owner
    context= {'blog':blog,'text':text,'can_edit': can_edit}
    return render(request,'blogs/blog.html',context)

#登陆才能发表博客
@login_required
def new_blog(request):
    """添加新Blog"""
    if request.method != 'POST':
        #创建新表单
        form = BlogForm()
    else:
        #Post提交数据进行处理
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:blogs'))
    context = {'form':form}
    return render(request,'blogs/new_blog.html',context)

@login_required
def edit_blog(request,blog_id):
    """编辑现有Blog"""
    blog = get_object_or_404(BlogPost,id=blog_id)
    #只能处理用户自己发表的博客
    if blog.owner != request.user:
        raise Http404
        
    if request.method != 'POST':
        #创建新表单
        form = BlogForm(instance=blog)
    else:
        #Post提交数据进行处理
        form = BlogForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog',args=[blog.id]))
    context = {'blog':blog,'form':form}
    return render(request,'blogs/edit_blog.html',context)