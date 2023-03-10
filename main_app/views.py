from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Tag
from .forms import SightingForm

# finches = [
#     {'genus': 'Mycerobas', 'scientific_name': 'Mycerobas affinis', 'common_name': 'Collared grosbeak', 'distribution': 'Bhutan, India, Myanmar, Nepal and Thailand'},
#     {'genus': 'Mycerobas', 'scientific_name': 'Mycerobas carnipes', 'common_name': 'White-winged grosbeak', 'distribution': 'Afghanistan, Bhutan, China, India, Iran, Myanmar, Nepal, Pakistan, Russia, Tajikistan, Turkmenistan, and Uzbekistan'}
# ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    # just like we passed data to our templates in express
    # we pass data to our templates trough our view functions
    # we can gather relations from SQL using our model methods
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.tag.all().values_list('id')
    tags_finch_doesnt_have = Tag.objects.exclude(id__in=id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'sighting_form': sighting_form, 'tags': tags_finch_doesnt_have })


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_sighting(request, finch_id):
    # create a ModelForm instance from the data in request.POST
    form = SightingForm(request.POST)
    # we need to validate the form, that means 'does it match our data?'
    if form.is_valid():
        # we don't want to save the form to the db until it has the cat id
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_tag(request, finch_id, tag_id):
    Finch.objects.get(id=finch_id).tag.add(tag_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_tag(request, finch_id, tag_id):
    Finch.objects.get(id=finch_id).tag.remove(tag_id)
    return redirect('detail', finch_id=finch_id)

class TagList(ListView):
    model = Tag
    template_name = '/tags/index.html'

class TagDetail(DetailView):
    model = Tag
    template_name = '/tags/detail.html'

class TagCreate(CreateView):
    model = Tag
    fields = ['color']

    def form_valid(self, form):
        return super().form_valid(form)
    
class TagUpdate(UpdateView):
    model = Tag
    fields = ['color']

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'