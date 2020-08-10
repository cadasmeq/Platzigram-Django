# django
from django.shortcuts import render
from datetime import datetime

posts = [
    {   
        'title': 'My dear Fenrir',
        'user':{
            'name':'@cadasmeq',
            'picture':'https://picsum.photos/60/60/?image=1009',
        },
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'photo': 'https://picsum.photos/200/200/?image=237',
    },

    {   'title': 'SoRomantinc~',
        'user':{
            'name':'@MyQueen',
            'picture':'https://picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'photo': 'https://picsum.photos/200/200/?image=1004',
    },

    {   'title': 'Awww deer<3',
        'user':{
            'name':'@TwistedMind',
            'picture':'https://picsum.photos/60/60/?image=1011', 
        },
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'photo': 'https://picsum.photos/200/200/?image=237',
    }
]

# Create your views here.
def list_posts(request):
        
    return render(request, 'feed.html', {"posts":posts}) 