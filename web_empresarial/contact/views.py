from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):

    contact_form= ContactForm()

    if request.method=="POST":

        contact_form= ContactForm(data= request.POST)

        if contact_form.is_valid():

            name= request.POST.get("name","")
            email= request.POST.get("email","")
            content= request.POST.get("content","")
            #Enviamos el email y redireccionamos

            email= EmailMessage(

                "La caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "No contestar@inbox.mailtrap.io",
                ["artemolcb@gmail.com"],
                reply_to=[email]

            )
            try:
                email.send()
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse("contact")+"?OK")

            except:
                #Algo no ha ido bien , redireccionamos a FAIL
                return redirect(reverse("contact")+"?FAIL")

    return render(request,'contact/contact.html',{'form': contact_form})