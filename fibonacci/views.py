from django.shortcuts import render
from django.http import HttpResponse
from math import sqrt

# Create your views here.

def get_number(request,number):
	try:
		n= int(number)
		if n < 2:
			return HttpResponse("<h1>{}</h1>" % (n))
		else:
			u = ((1+sqrt(5))/2)
			j = ((u**n-(1-u)**n)/sqrt(5))
			return HttpResponse("<h1>Result: {}</h1>".format(round(j)))
	except ValueError:
		return HttpResponse("<h1>{} is not a number</h1>" % (n))