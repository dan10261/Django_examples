from django.shortcuts import render
from django.http import HttpResponse
from .models import Publisher
from .models import User
from django.db import models
from django.views.generic import View


# create your views here
def home(request):
    return render(None, 'home.html', {'body_title': 'welcome home page', 'page_body': 'welcome to my first variables '
                                                                                      'in django.'})


def first_view(request, user_id=0):
    data = 'Hello this is a new view. User ID is: ' + user_id.__str__()
    return HttpResponse(data)


def list_publishers(request):
    all_publishers = Publisher.objects.all()
    print(all_publishers)
    return render(request, 'list_publishers.html', {'publishers': all_publishers})


def new_publisher(request):
    return render(request, 'new_publisher.html')


def list_users(request):
    all_users = User.objects.all()
    return render(request, 'list_users.html', {'users': all_users})


def new_user(request):
    template_name = 'new_user.html'
    # user = User.objects.all()[:1]
    try:
        user = User.objects.filter(name='user2')
        print(user[0].name)
        return render(request, template_name, {'user': user[0]})
    except ValueError:
        print('User Value invalid')
    except IndexError:
        print('User Does not exist')

    return render(request, template_name, {'user': {'username': '', 'name': ''}})
