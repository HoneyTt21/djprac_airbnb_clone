from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse
from . import models


class HomeView(ListView):
    """Home View"""

    model = models.Room
    paginate_by = 10
    paginate_orphan = 2
    ordering = "created"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
