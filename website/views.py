from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attorney, PracticeArea, FAQ, Testimonial
from .forms import ContactForm

def home(request):
    attorneys = Attorney.objects.all()
    practice_areas = PracticeArea.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    
    context = {
        'attorneys': attorneys,
        'practice_areas': practice_areas,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def services(request):
    practice_areas = PracticeArea.objects.all()
    context = {
        'practice_areas': practice_areas,
    }
    return render(request, 'services.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('website:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)

def faq(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'faq.html', context)