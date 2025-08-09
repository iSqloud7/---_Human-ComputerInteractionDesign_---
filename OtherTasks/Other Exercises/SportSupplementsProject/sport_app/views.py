from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SupplementForm
from .models import Supplement


# Create your views here.
def index(request):
    supplements = Supplement.objects.all()
    context = {"supplements": supplements, "form": SupplementForm}
    return render(request, "index.html", context=context)


def detail(request, supplement_id):
    supplement = get_object_or_404(Supplement, pk=supplement_id)
    # supplement.image=supplement['image']
    return render(request, 'details.html', {'supplement':supplement})


def add(request):
    if request.method == 'POST':
        form_data = SupplementForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            supplement = form_data.save(commit=False)
            supplement.image = form_data.cleaned_data['image']
            supplement.save()
            return HttpResponseRedirect("/")

    return render(request, "add.html", {"form": SupplementForm})
def edit(request, supplement_id):
    supplement_instance=Supplement.objects.filter(id=supplement_id).get()
    if request.method == 'POST':
        supplement=SupplementForm(request.POST, instance=supplement_instance)
        if supplement.is_valid():
            supplement.save()
            return redirect('index')
    else:
        supplement=SupplementForm(instance=supplement_instance)
    return render(request, 'edit.html', {"form": supplement})

def delete(request, supplement_id):
    supplement_instance = Supplement.objects.filter(id=supplement_id).get()
    if request.method=="POST":
        supplement_instance.delete()
        return redirect("index")

    return render(request, "delete.html")

