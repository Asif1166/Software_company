
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def hom(request):
    diction = {'title':'RozSoft.Tech'}
    return render(request, 'home/home.html', context=diction)

def layout(request):
    diction = {'title':'layout'}
    return render(request, 'layout/layout.html', context=diction)

def price(request):
    diction = {'title':'pricing'}
    return render(request, 'home/price.html', context=diction)

def technology(request):
    diction = {'title':'technology'}
    return render(request, 'home/technology.html', context=diction)

def job(request):
    diction = {'title':'job opportunity'}
    return render(request, 'home/job.html', context=diction)

def service(request):
    diction = {'title':'services'}
    return render(request, 'home/service.html', context=diction)

def contact(request):
    diction = {'title':'contacts'}
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New Message: {}
        
        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['cont.rozsoft.tech@gmail.com'])
        
        # return HttpResponse('Thank you For Massege Us, We will be in touch soon')
        # return render(request, 'home/contact.html', context=diction)
        
    return render(request, 'home/contact.html', context=diction)

def about(request):
    diction = {'title':'about us'}
    return render(request, 'home/about.html', context=diction)

def project(request):
    diction = {'title':'portfolio'}
    return render(request, 'home/project.html', context=diction)

def index(request):
    diction = {'title':'index'}
    return render(request, 'home/index1.html', context=diction)

def layout1(request):
    diction = {'title':'layout1'}
    return render(request, 'layout/layout1.html', context=diction)



