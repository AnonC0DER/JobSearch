from django.shortcuts import render


def SearchPageView(request):
    '''Search page view'''
    return render(request, 'search_page.html')


def LoginViwe(request):
    '''Login view'''
    return render(request, 'login.html')


def RegisterViwe(request):
    '''Register view'''
    return render(request, 'register.html')