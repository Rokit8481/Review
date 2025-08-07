from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Review
from django.http import HttpRequest
from .forms import ReviewForm



def review_list(request: HttpRequest):
    reviews = Review.objects.all()

    return render(request, 'reviews/index.html', {
        "reviews": reviews
    })

@login_required
def add_review(request: HttpRequest):
    review = Review(author=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/add_review.html', {
        'form': form,
    })

def login_view(request: HttpRequest):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            return redirect('room_list')
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect('/')

def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('room_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
