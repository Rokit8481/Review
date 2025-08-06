from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from django.http import HttpRequest


def review_list(request: HttpRequest):
    reviews = Review.objects.all()

    return render(request, 'reviews/index.html', {
        "reviews": reviews
    })