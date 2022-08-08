from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import authentication.models as User

user = User.objects.get(id=id)

@login_required
def dashboard3view(request,pk):
    user = User.objects.get(pk=id)
    if request.method =='POST':
        company_name = request.POST.get('company_name', None)
        about = request.POST.get('about', None)
        opening_hours = request.POST.get('opening_hours', None)
        contact_details = request.POST.get('contact_details', None)
        web_url = request.POST.get('web_url', None)

        return redirect ('dashborard?', pk=user.id)

    return render(request, 'qr_gen_app/dashboard3.html')
