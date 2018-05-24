from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm


def users(request):

    return render(request, 'users.html', {
        'users': User.objects.all()
    })


def user(request, user_id):

    return render(request, 'user.html', {
        'user': get_object_or_404(User, pk=user_id)
    })


def delete_user(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('/')


def edit_user(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            user.profile.birthday = form.cleaned_data.get('birthday')
            user.save()
            return redirect('/user/{}/'.format(user.id))
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})


def create_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthday = form.cleaned_data.get('birthday')
            user.save()
            return redirect('users')
    else:
        form = SignUpForm()
    return render(request, 'create_user.html', {'form': form})
