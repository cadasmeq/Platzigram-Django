"""Platzigram views"""

# django
from django.shortcuts import redirect


def root(request):
    return redirect('posts:feed')