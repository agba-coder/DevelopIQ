from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.conf import settings

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError

from .models import Testimonial, Quote, Mail

# Create your views here.


def homepage(request):

    testimony = Testimonial.objects.all()
    context = {'testimonies': testimony }
    return render(request, "index.html", context)

	# return render (request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')


# request function for portfolio ==> portfolio view
def portfolio(request):
    testimony = Testimonial.objects.all()
    context = {'testimonies': testimony }

    return render(request, "portfolio.html", context)
    

# request function for contact page and functionalities
def contact(request):

    # if HTTP Request is POST
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["email"]
        message = request.POST["message"]

        mail = Mail.objects.create(name=name, email=email, subject=subject, message=message)
        mail.save()
        
        subject = "✅ Hi DevelopIQ, you've a new message from your Website!"
        message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        print(message)
        from_email = settings.EMAIL_HOST_USER
        receipient = [email]

        try:
            send_mail(subject, message, from_email, receipient, fail_silently=False)
            print("sent")
            messages.success(request, "Your Message Has Been Receieved ✅!")
            return redirect("contact")

        except BadHeaderError:
            message.error(request, "❌ Oops, An Error Occurred. Please Try Again!")
            return render(request, "contact.html")


    return render(request, "contact.html")


def getQuote(request):

    # if HTTP Request ==> POST
    if request.method == "POST":

        # extracting data from the input fields in quote.html
        file = request.FILES.get("document")
        print(file)
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        country = request.POST["country"]
        budget = request.POST["budget"]
        whatsAppNumber = request.POST["whatsAppNumber"]
        details = request.POST["details"]
        service = request.POST["service"]
        startDate = request.POST["startDate"]
        company_name = request.POST["company"]
        postion = request.POST["position"]
        ad = request.POST["ad"]
        print(ad)

        if Quote.objects.filter(email=email).exists():
            print('Records already exist')
            messages.error(request, 'Records registered with that email already exist!')
            return render(request, 'quote.html')

        elif Quote.objects.filter(company_name=company_name).exists():
            print('Records already exist')
            messages.error(request, 'Records registered with that company name already exist!')
            return render(request, 'quote.html')

        else:
            quote = Quote.objects.create(name=name,
                email=email,
                contact=contact,
                country=country,
                approximated_budget=budget,
                whatsapp_number=whatsAppNumber,
                details=details,
                service_type=service,
                start_date=startDate,
                company_name=company_name,
                postion=postion,
                how_did_you_know_us=ad,
                file=file)

            # save data to database
            quote.save()

        # message alert and redirect user back to the page
        messages.success(request, "Your request has been received and processed successfully. Please check your mail for more info")
        return redirect("getQuote")



    return render(request, "quote.html")