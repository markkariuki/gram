from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'base.html')

def photos_of_day(request):
    date = dt.date.today()
    return render(request, 'base.html', {"date": date,})


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
