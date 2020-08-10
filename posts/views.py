# django
from django.http import HttpResponse
import time
from datetime import datetime

posts = [
    {
        'user':'Cristopher Adasme',
        'title': 'My dear Fenrir',
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'picture': 'https://picsum.photos/200/200/?image=237',
    },
    {
        'user':'@MyQueen',
        'title': 'SoRomantinc~',
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'picture': 'https://picsum.photos/200/200/?image=1004',
    },
    {
        'user':'@TwistedMind',
        'title': 'Awww deer<3',
        'timestamp': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'picture': 'https://picsum.photos/200/200/?image=1003',
    }
]

# Create your views here.
def list_posts(request):
    content = []
    for post in posts:
        content.append("""
        <p><strong>{title}</strong></p>
        <p><small>{user}</small></p>
        <p><i>{timestamp}</i></p>
        <figure><img src="{picture}" /></figure><br>
        """.format(**post))
        
    return HttpResponse(content) 