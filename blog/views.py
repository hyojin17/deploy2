from django.shortcuts import render, get_object_or_404
from .models import Blog
#모델의 Blog를 끌어온다.

def home(request):
    blogs = Blog.objects#블로그안에있는 객체를 blogs라는 변수에 담아준다.
    #쿼리셋-> 객체들의 목록을 전달받을 수 있다(.objects)#메소드(쿼리셋을 정렬할 수 있게하거나 기능하게 해주는 방법중 하나)
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)#blog_id번째 블로그 객체
    #첫번째 객체는 클래스이름, 두번째객체는 pk값
    return render(request, 'detail.html', {'blog':blog_detail})