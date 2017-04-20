from django.shortcuts import render

from .models import Song, Performer


def song_list(request):
    return render(
        request,
        'songs/song_list.html',
        {'songs': Song.objects.all()}
    )


def song_detail(request, pk):
    return render(
        request,
        'songs/song_detail.html',
        {'song': Song.objects.get(pk=pk)}
    )


def performer_detail(request, pk):
    performer = Performer.objects.get(pk=pk)
    return render(
        request,
        'songs/performer_detail.html',
        {'performer': performer,
         'songs': Song.objects.filter(performer=performer)}
    )
