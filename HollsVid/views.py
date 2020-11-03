import os
import requests
from urllib.parse import urlparse,parse_qs,quote
from django.shortcuts import render,redirect ,Http404
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.forms.utils import ErrorList
from django.contrib import messages
from . import models as holls_molde
from .forms import VideoFrom,SearchForm




# Create your views here.


class CreateHolls(generic.CreateView):
    model = holls_molde.Holl
    fields = ['title']
    template_name = "hollvid/create_holl.html"
    success_url = reverse_lazy('Holls-auth:dashbord')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHolls,self).form_valid(form)
        return redirect('Holls-auth:index')


class detailHoll(generic.DetailView):
    model = holls_molde.Holl
    template_name = "hollvid/detelis_holl.html"


class UpdatelHoll(generic.UpdateView):
    model = holls_molde.Holl
    fields = ['title']
    template_name = "hollvid/UpdatelHoll.html"
    success_url = reverse_lazy('Holls-auth:dashbord')


class DeleteHolls(generic.DeleteView):
    model = holls_molde.Holl
    fields = ['title']
    template_name = "hollvid/DeletelHoll.html"
    success_url = reverse_lazy('Holls-auth:dashbord')


def AddVideos(request,pk):
    form = VideoFrom()
    search_form = SearchForm()
    hall = holls_molde.Holl.objects.get(pk=pk)
    if not request.user == hall.user:
        raise Http404
    if request.method == 'POST':
        form = VideoFrom(request.POST)
        if form.is_valid():
            form_url = form.cleaned_data.get('url')
            form_url_parse = urlparse(form_url)
            if form_url_parse.netloc != 'www.youtube.com':
                messages.error(request,'This is not youtube URL')
                return redirect(reverse('HollsVid:add-videos',kwargs={'pk':pk}))
            form_url_query = parse_qs(form_url_parse.query).get('v')[0]
            google_yuotube_api=f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={form_url_query}&key={os.environ.get("Youtube_Key_API")}'
            response = requests.get(google_yuotube_api)
            response_json = response.json()
            title = response_json['items'][0]['snippet']['title']
            if form_url_query:
                video = holls_molde.video.objects.create(
                    title= title,
                    youtube_id=form_url_query,
                    url=form_url,
                    holl=hall
                )
                video.save()
                return redirect(reverse('HollsVid:detailHoll',kwargs={'pk':pk}))
        else:
            error = form._errors.setdefault('url',ErrorList())
            error.append('Need to be a YouTube URL')


    context = {
        'form': form,
        'search_form': search_form,
        'hall':hall
    }
    return render(request, 'hollvid/add_videos.html',context)


def search_videos(request):
    search_from = SearchForm(request.GET)
    if search_from.is_valid():
        from_data = search_from.cleaned_data['search_tram']
        encode_serch = quote(from_data)
        youTube_serach_API = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&type=video&q={encode_serch}&key={os.environ.get("Youtube_Key_API")}'
        search_request = requests.get(youTube_serach_API)
        search_json= search_request.json()
        return JsonResponse(search_json)
    return JsonResponse({'errors':'Not able to validate form '})

