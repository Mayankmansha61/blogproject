from adminpanel.models import *
import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from blogweb.models import *
from adminpanel.configuration import *
from django.core.paginator import Paginator 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage