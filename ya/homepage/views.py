from users.models import Profile
from django.shortcuts import get_object_or_404, render, redirect

from catalog.models import Item


def home(request):
    items = (
        Item.objects.items_queryset()
        .filter(
            is_on_main=True,
        )
        .order_by(Item.name.field.name)
    )
    context = {'items': items}
    template = 'homepage/index.html'
    return render(request, template, context)


def coffee(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(
            Profile.objects.get_queryset().only(
                Profile.coffee_count.field.name,
            ),
            user=request.user.id,
        )

        user_profile.coffee_count += 1
        user_profile.save()

        return redirect('users:profile')

    template = 'homepage/coffee.html'
    return render(request, template, status=418)
