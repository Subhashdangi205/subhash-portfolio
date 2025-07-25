from django.shortcuts import render,redirect,HttpResponse
from .models import Project, Achievement,Contact,Skill
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def portfolio_home(request):
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    skills = Skill.objects.all()
    return render(request, 'base.html', {'projects': projects, 'achievements': achievements, 'skills': skills})

def contact_view(request):
    
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        contact = Contact(name=name, email=email, message=message)
        contact.save()  

        subject = f'New Contact Form Submission from {name}'
        full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['subhashdangi47@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")
        return render(request, 'base.html', {'success': True})

    return redirect('contact')