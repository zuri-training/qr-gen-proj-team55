from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

def dashboard3view(request):


