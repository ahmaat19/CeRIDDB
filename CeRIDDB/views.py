from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages




def AboutView(request):
    return render(request, 'about.html')

def ContactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        from_email =  request.POST.get('email')
        message = request.POST.get('message')

        if number and name and message:
            send_mail(
                'New message sent by ' + name + ' using contact form at eCommerce',
                message+'. <'+ from_email +'> <'+ number +'>',
                ' ' + name + '  <from_email>',
                ['ahmaat19@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for getting in touch!')
            messages.success(request, ' I appreciate you contacting me. I will get back in touch with you soon!')
            messages.success(request, ' I check my email box twice a day so you should get a reply within 12-24 hours. If not, re-send your question.')
            return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'contact.html')


