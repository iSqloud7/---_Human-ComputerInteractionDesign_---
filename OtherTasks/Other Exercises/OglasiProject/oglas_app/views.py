from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Oglas
from .forms import OglasForm
# Create your views here.

def index(request):
    queryset = Oglas.objects.all()
    context={"oglasi": queryset, "form": OglasForm}
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        form_data=OglasForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            oglas=form_data.save(commit=False)
            oglas.user=request.user
            oglas.image=form_data.cleaned_data['image']
            oglas.save()
            return HttpResponseRedirect("/")

    return render(request, "create.html", context={"form": OglasForm})
def edit(request, oglas_id):
    oglas_instance = get_object_or_404(Oglas, id=oglas_id)
    if request.method == "POST":
        form = OglasForm(request.POST, instance=oglas_instance)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = OglasForm(instance=oglas_instance)

    return render(request, "edit.html", {"form": form})

def delete(request, oglas_id):
    oglas_instance = get_object_or_404(Oglas, id=oglas_id)
    if request.method == "POST":
        oglas_instance.delete()
        return redirect("index")
    return render(request, "delete.html", {"oglas": oglas_instance})
def detail(request, oglas_id):
    oglas=get_object_or_404(Oglas, pk=oglas_id)
    return render(request, "detail.html", {'oglas': oglas})