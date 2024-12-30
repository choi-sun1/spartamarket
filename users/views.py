from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from products.models import Product

def users(request):
    pass

@login_required
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)

    like_products = member.like_product.all()
    my_products = Product.objects.filter(author=member)
    is_following = request.user.follows.filter(pk=member.pk).exists()

    context = {
        "member":member,
        "like_products" : like_products,
        "my_products" : my_products,
        "is_following" : is_following,

    }
    return render(request, 'users/profile.html', context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(),  pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect('users:profile', username=member.username)
    return redirect('login')