from django.shortcuts import render

# Create your views here.

from form.forms import ContactForm

# add to your views
def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import json

from .active import add_contact

# Client.contacts.view_contact(ID)

# Client.deals.get_deals()

def fill(request):
    return render(request, 'auto_form.html')

def test(request):
    return render(request, 'test_page.html')

def send_email(message, to='maged@deemalab.com', subject = 'Training Results'):
    '''
    Sends email with results to the given email address.
    '''
    msg = MIMEMultipart()
    # message = "hi how's it going?"
    msg['From'] = "dlc.ai.bot@gmail.com"
    password = "!randompassforaitesting!"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to {}".format(msg['To']))    
    add_contact(to)
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            send_email(content, to=contact_email, subject='activecampaign')
            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "Your website" +'',
            #     ['maged@deemalab.com'],
            #     headers = {'Reply-To': contact_email }
            # )
            # email.send()
            # create_contact(contact_email)
            return render(request, 'submitted.html', {})

    return render(request, 'contact.html', {
        'form': form_class,
    })
