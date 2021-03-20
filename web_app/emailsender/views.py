from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from email.message import EmailMessage
# Create your views here.
def home(request):
    return render(request,'index.html')


def mailer(to,subject,content,sender_mail=None):
    sender_mail = "no.reply.python.py@gmail.com"   
    password_sender = "qwerty@123"

    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = subject
    message.set_content(content)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return "Success"
    except:
        return "Something Went Wrong"


def sendmail(request):

    # fr_om = request.GET["given_name"]
    to = request.GET["to_mail"]
    subject = request.GET["subject"]
    message = request.GET["mess_age"]

    res_ult = mailer(to,subject,message)


    return render(request, "result.html", {"result":res_ult})