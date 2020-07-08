from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .forms import EmailForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View

global mes
global cnt
mes='hello'
cnt=0
# Create your views here.
class Mainview(TemplateView):
    template_name='index.html'

class Contactview(TemplateView):
    template_name='contact.html'



class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'email_form': form})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)


        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            phone = str(form.cleaned_data['phone'])
            message = form.cleaned_data['message']
            Hemail = ['nowreshraj.s@gmail.com']
            files = request.FILES.getlist('attach')
            he="\n\n\n"
            subject= company+" -Request service"
            message= "name :"+name+"\n email :"+email+"\n contact :"+phone+he+message
            
            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER,Hemail)
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'success_message': 'Sent email to Jashan Technology','email_form': form})
                
                
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        
        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
    
    