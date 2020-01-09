from django.http import HttpResponse
import os
from twilio.rest import Client
from django.shortcuts import render
from django.utils import timezone
from pages.models import Host
from pages.models import Checkin
from pages.models import Checkout
from pages.models import Exites
from django.shortcuts import render
from django.http import HttpResponse
from trydjango import settings
from django.core.mail import send_mail
#from django.conf.urls.defaults import *
import datetime



# Create your views here
sample_name="abc"
sample_email="xyz"
sample_itime="itime"
def home_view(request):
	Hostinfo = Host.objects.all()
	Exitinfo = Exites.objects.all()
	con=0
	cont=0
	return_host=return_phone=return_email="abc"
	for host in Hostinfo:
		con=con+1
	for host in Hostinfo [::-1]:
		if(host.NAME!=None):
			return_host=host.NAME
			return_phone=host.Phone
			return_email=host.EMAIL
			break
	for exit in Exitinfo:
		cont=cont+1
	context = {'Hostinfo': Hostinfo, 'con': con, 'cont': cont,'return_host':return_host,'return_phone':return_phone,'return_email':return_email}
	return render(request,'pages/index.html',context)

def submit(request):
	return render(request,'pages/indexs.html')

def submita(request):
	return render(request,'pages/indexa.html')

def submitc(request):
	return render(request,'pages/indexc.html')

def submitd(request):
	return render(request,'pages/indexd.html')

def host_view(request):
	if request.method=="POST":
		hname  = request.POST.get('hname')
		hemail = request.POST.get('hemail')
		hphone = "+91"+request.POST.get('hphone')
		hpswd  = request.POST.get('hpswd')
		t = Host(NAME=hname,EMAIL=hemail,Phone=hphone,Pswd=hpswd,itime=datetime.datetime.now())
		t.save()
		return render(request, 'pages/indexa.html')
	return render(request,'pages/indexh.html')


def checkin_view(request):
	Hostinfo = Host.objects.all()
	Exitinfo = Exites.objects.all()
	con = 0
	cont = 0
	for host in Hostinfo:
		con = con + 1
	for exit in Exitinfo:
		cont = cont + 1
	if request.method=="POST":
		vname  = request.POST.get('vname')
		vemail = request.POST.get('vemail')
		vphone = request.POST.get('vphone')
		for_sms="xyz"
		for_email="abc"
		s = Checkin(NAME=vname,EMAIL=vemail,Phone=vphone,itime=datetime.datetime.now())
		s.save()
		for host in Hostinfo[::-1]:
			if (host.NAME != None):
				for_sms = host.Phone
				for_email = host.EMAIL
				break
		account_sid = "ACd6427efe64f0dee1dc399d91a3dede26"
		auth_token = 

		client = Client(account_sid, auth_token)

		client.messages.create(from_="+13347586143",
							   to=for_sms,
							   body="Name\t\t: "+s.NAME+"\n"+"Email\t\t : "+s.EMAIL+"\nPhone\t\t: "+s.Phone+"\nCheckin-time: "+str(s.itime)+" IST",
								   )

		subject="New Visitor Checked In !!!"
		msg=body="Name\t\t: "+s.NAME+"\n"+"Email\t\t : "+s.EMAIL+"\nPhone\t\t: "+s.Phone+"\nCheckin-time: "+str(s.itime)+" IST"
		to=for_email
		res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
		if(res==1):
			msg="Mail Sent"
		else:
			msg="Mail could not be sent"
		return render(request,'pages/indexs.html')
	context = {'con': con, 'cont': cont}
	return render(request,'pages/indexv.html',context)

def checkout_view(request):
	hcin = 0
	hcout = 0
	aout=0
	bout=0
	for entry in Checkin.objects.all():
		hcin = hcin + 1
	for exit in Checkout.objects.all():
		hcout = hcout + 1
	if request.method=="POST":
		ophone = request.POST.get('ophone')
		s = Checkout(Phone=ophone,otime=datetime.datetime.now())
		for entry in Checkin.objects.all():
			if(ophone==entry.Phone):
				aout=aout+1
		for exit in Checkout.objects.all():
			if(ophone==exit.Phone):
				bout=bout+1
		if(bout<aout):
			s.save()
			for_sms = "xyz"
			for_email = "abc"
			for_name = "name"
			Hostinfo = Host.objects.all()
			for host in Hostinfo[::-1]:
				if (host.NAME != None):
					for_name = host.NAME
					for_sms = host.Phone
					for_email = host.EMAIL
					break
			Visinfo = Checkin.objects.all()
			for visitor in Visinfo[::-1]:
				if (visitor.Phone == s.Phone):
					sample_name = visitor.NAME
					sample_email = visitor.EMAIL
					sample_itime = str(visitor.itime)
					break

			account_sid = "ACd6427efe64f0dee1dc399d91a3dede26"
			auth_token = 

			client = Client(account_sid, auth_token)

			client.messages.create(from_="+13347586143",
								   to=for_sms,
								   body="Name\t\t: " + sample_name + "\n" + "Email\t\t : " + sample_email + "\nPhone\t\t: " + s.Phone + "\nCheckin-time: " + sample_itime + " IST" + "\nCheckout-time:  " + str(
									   s.otime) + " IST" + "\n Host Details:\nHost Name  :" + for_name + "\n Phone  :" + for_sms
								   )

			subject = "A Visitor Checked Out !!!"
			msg = body = "Name\t\t: " + sample_name + "\n" + "Email\t\t : " + sample_email + "\nPhone\t\t: " + s.Phone + "\nCheckin-time: " + sample_itime + "\nCheckout-time:  " + str(
				s.otime) + "\n Host Details:\nHost Name  :" + for_name + "\n Phone  :" + for_sms
			to = for_email
			res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
			if (res == 1):
				msg = "Mail Sent"
			else:
				msg = "Mail could not be sent"

			subject = "Thank You for Visiting our center"
			msg = body = "Thank You for Visiting our Cener\n Name\t\t: " + sample_name + "\n" + "Email\t\t : " + sample_email + "\nPhone\t\t: " + s.Phone + "\nCheckin-time: " + sample_itime + " IST" + "\nCheckout-time:  " + str(
				s.otime) + " IST" + "\n Host Details:\nHost Name  :" + for_name + "\n Phone  	:" + for_sms + "\n Please Visit again !"
			to = sample_email
			res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
			if (res == 1):
				msg = "Mail Sent"
			else:
				msg = "Mail could not be sent"
			return render(request,'pages/indexd.html')
		else:
			return render(request,'pages/errorb.html')
	context={'hcin':hcin,'hcout':hcout}
	return render(request,'pages/indexo.html',context)

def exit_view(request):
	hcin = 0
	hcout = 0
	aout=0
	bout=0
	Hostinfo = Host.objects.all()
	Exitinfo = Exites.objects.all()
	for host in Hostinfo:
		hcin = hcin + 1
	for exit in Exitinfo:
		hcout = hcout + 1
	if request.method=="POST":
		ephone = "+91"+request.POST.get('ephone')
		epswd  = request.POST.get('epswd')
		s = Exites(Phone=ephone,Pswd=epswd,otime=datetime.datetime.now())
		for host in Hostinfo:
			if(ephone==host.Phone):
				aout=aout+1
		for exit in Exitinfo:
			if(ephone==exit.Phone):
				bout=bout+1
		if(bout<aout):
			s.save()
			return render(request,'pages/indexc.html')
		else:
			return render(request,'pages/errora.html')
	context = {'hcin':hcin, 'hcout':hcout,'aout':aout,'bout':bout}
	return render(request,'pages/indexe.html',context)

def errora(request):
	return render(request,'pages/errora.html')

def errorb(request):
	return render(request,'pages/errorb.html')
