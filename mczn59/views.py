# ~*~ coding: utf-8 ~*~

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from mczn59.models import User, EditForm


def index(request):
    latest_users_list = User.objects.order_by('-invite_date')[:5]
    context = {'latest_users_list': latest_users_list}
    return render(request, 'index.html', context)

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'detail.html', {'user': user})
# TODO: 404 and 500 views
def edit(request, user_id):
    user = User.objects.get(pk=user_id)
    form = EditForm(instance=user)
    return render(request, 'edit.html', form)

def save(request, user_id):
    return HttpResponse("You're save user %s." % user_id)