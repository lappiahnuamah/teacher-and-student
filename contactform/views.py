from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'fname': fname,
            'lname': lname,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['sandratb2121@gmail.com'])

    return render(request, 'contact.html',{})