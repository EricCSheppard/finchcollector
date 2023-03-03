from django.shortcuts import render
from .models import Finch
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
    return render(request, 'finches/detail.html', { 'finch': finch})