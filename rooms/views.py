from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from . import models


class HomeView(ListView):
    """Home View"""

    model = models.Room
    paginate_by = 10
    paginate_orphan = 2
    ordering = "created"


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/room_detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


class RoomDetail(DetailView):

    """Room Detail View"""

    model = models.Room
