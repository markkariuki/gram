from django.http  import HttpResponse,Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import NewPostForm , CommentForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.shortcuts import render
from . models import Post, Profile, Editor
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from friendship.models import FriendshipRequest


@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(id=id)
    images = Post.objects.all()
    return render(request, 'profile.html', {'images':images, 'profile':profile, 'user':current_user})


@login_required(login_url='/accounts/login/')
def photos_of_day(request):
    date = dt.date.today()
    posts = Post.objects.all()
    form = NewPostForm()
    if request.method =='POST':
        if form.is_valid():
            posts = form.save(commit=False)
            post.user= requet.user.id
            post.save()
        else:
            form = NewPostForm()
    return render(request, 'home.html', {"date": date,"posts":posts, "form":form,})

    # image = models.ImageField(upload_to = 'photos/', null = True)
    # name = models.CharField(max_length=60, null=True)
    # caption = HTMLField(null=True)
    # likes = models.IntegerField(null =True)
    # date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    # user = models.ForeignKey(User)
    # pub_date
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
            return redirect('photosToday')


    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('photosToday')
    else:
        form = CommentForm()
    return render(request, 'new-comment.html', {'form': form})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_username = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"username": searched_username})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def friends(request):
    other_user = User.objects.get(pk=1)
    Friend.objects.add_friend(
    request.user,                               # The sender
    other_user,                                 # The recipient
    message='Hi! I would like to add you')

    friend_request = FriendshipRequest.objects.get(pk=1)
    friend_request.accept()
# or friend_request.reject()     # This message is optional
