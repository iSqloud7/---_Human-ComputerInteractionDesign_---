from django.shortcuts import render, redirect

from car_app.forms import SheduledRepairForm
from car_app.models import ScheduledRepair


def index(request):

    return render(request, 'index.html')


def repairs(request):
    repairs = ScheduledRepair.objects.all()
    if request.method == 'POST':
        form = SheduledRepairForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.problem_image = form.cleaned_data['problem_image']

            repair.save()
            return redirect('repairs')

    else:
        form = SheduledRepairForm()

    return render(request, 'repairs.html', {'repairs': repairs, 'form': form})
