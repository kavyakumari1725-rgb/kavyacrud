from django.shortcuts import render,redirect,get_object_or_404
from . models import Tour
from . forms import  TourForm

# Create your views here.
def index(response):
    return render(response,'index.html')
def packages(response):
    return render(response,'packages.html')
def destination(response):
    tours=Tour.objects.all()
    context={'tours':tours}
    return render(response,'destination.html',context)

def tour_create(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination.html')
    else:
        form = TourForm()
    return render(request, 'Tour_form.html', {'form': form})

def tour_update(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    form = TourForm(request.POST or None, instance=tour)
    if form.is_valid():
        form.save()
        return redirect('destination.html')
    return render(request, 'Tour_form.html', {'form': form})

def tour_delete(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        tour.delete()
        return redirect('destination.html')
    return render(request, 'tour_confirm_delete.html', {'tour': tour})

def about_us(response):
    return render(response,'about_us.html')