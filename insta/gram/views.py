from django.http  import HttpResponse,Http404
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.shortcuts import render
from . models import Post

@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'base.html')

def photos_of_day(request):
    date = dt.date.today()
    posts = Post.objects.all()
    return render(request, 'home.html', {"date": date,"posts":posts})


def past_days_photos(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
