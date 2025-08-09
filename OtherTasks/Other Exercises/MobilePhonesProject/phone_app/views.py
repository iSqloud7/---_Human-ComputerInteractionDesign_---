from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from .forms import PhoneForm
# Create your views here.

def index(request):
    phone = Phone.objects.all()
    context={"phones":phone, "form":PhoneForm}
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        form_data=PhoneForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            phone=form_data.save(commit=False)
            phone.user=request.user
            phone.image=form_data.cleaned_data['image']
            phone.save()
            return HttpResponseRedirect("/")

    return render(request, "create.html", context={"form": PhoneForm})

def detail(request, phone_id):
    phone=get_object_or_404(Phone, pk=phone_id)
    return render(request, 'detail.html', {'phone':phone})

def delete(request, phone_id):
    phone_instance=Phone.objects.filter(id=phone_id).get()
    if request.method=='POST':
        phone_instance.delete()
        return redirect("index")

    return render(request, "delete.html")

def edit(request, phone_id):
    phone_instance=Phone.objects.filter(id=phone_id).get()
    if request.method=='POST':
        phone=PhoneForm(request.POST, instance=phone_instance)
        if phone.is_valid():
            phone.save()
        return redirect("index")
    else:
        phone=PhoneForm(instance=phone_instance)

    return render(request, "edit.html", {"form": phone})
