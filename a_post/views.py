from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'a_post/post_list.html')


def post_detail(request, pk):
    return render(request, 'a_post/post_detail.html', {'pk': pk})
