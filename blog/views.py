from django.shortcuts import render
from .models import Blog
#모델의 Blog를 끌어온다.

def home(request):
    blogs = Blog.objects#블로그안에있는 객체를 blogs라는 변수에 담아준다.
    #쿼리셋-> 객체들의 목록을 전달받을 수 있다(.objects)#메소드(쿼리셋을 정렬할 수 있게하거나 기능하게 해주는 방법중 하나)
    return render(request, 'home.html', {'blogs': blogs})

    #쿼리셋과 메소드의 형식
    #모델.쿼리셋(objects).메소드