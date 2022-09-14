from .models import Session
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['phone'] and request.POST['service'] and request.POST['date'] and request.POST['time']:
            same_date = Session.objects.filter(date=request.POST['date'])
            if same_date:
                same_time = Session.objects.filter(time=request.POST['time'])
                if same_time:
                    return render(request, 'contact.html', {'error': 'Oops, This date is already booked by someone else.'})
            new_session = Session()
            new_session.name = request.POST['name']
            new_session.email = request.POST['email']
            new_session.phone = request.POST['phone']
            new_session.service = request.POST['service']
            new_session.date = request.POST['date']
            new_session.time = request.POST['time']
            new_session.save()
            return render(request, 'contact.html', {'success': 'Congratulations, Your session was booked successfully.'})
    else:
        return render(request, 'contact.html')
