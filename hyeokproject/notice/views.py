from django.shortcuts import redirect, render
from.models import Notice
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def hello(request):
    return render(request, "hello.html")

def home(request):
    notices = Notice.objects

    notice_list = Notice.objects.all()
    paginator = Paginator(notice_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'notices':notices, 'posts':posts})

def detail(request, notice_id):
    notice_detail = Notice.objects.get(id = notice_id)
    return render(request, 'detail.html', {'notice' : notice_detail})

def new(request):
    return render(request, 'new.html')

def delete(request, notice_id):
    Notice.objects.get(id = notice_id).delete()
    return redirect('/')

def edit(request, notice_id):
    notice = Notice.objects.get(id = notice_id)
    return render(request, 'edit.html', {'notice':notice})

def update(request, notice_id):
    notice = Notice.objects.get(id = notice_id)
    notice.title = request.POST.get('title')
    notice.body = request.POST.get('body')
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/notice/' + str(notice.id))

def create(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.writer = request.GET['writer']
    notice.number = request.GET['number']
    notice.pub_date = timezone.datetime.now()
    notice.body = request.GET['body']
    notice.save()
    return redirect('/notice/' + str(notice.id))

def aboutme(request):
    return render(request, "aboutme.html")