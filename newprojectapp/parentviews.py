from newprojectapp.models import  hostel,attendance,fee,staff,notification,payment,booking
from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout


@login_required(login_url='log')
def view_par_hostel(request):
    data = hostel.objects.all()
    return render(request, 'viewparhostel.html', {'data': data})

@login_required(login_url='log')
def view_par_attendance(request):
    data = attendance.objects.all()
    return render(request, 'viewparatt.html', {'data': data})

@login_required(login_url='log')
def view_par_fee(request):
    data = fee.objects.all()
    return render(request, 'viewparfee.html', {'data': data})

@login_required(login_url='log')
def view_par_staff(request):
    data = staff.objects.all()
    return render(request, 'viewparstaff.html', {'data': data})

@login_required(login_url='log')
def view_par_notification(request):
    data = notification.objects.all()
    return render(request, 'viewparnoti.html', {'data': data})

@login_required(login_url='log')
def view_par_pay(request):
    data = payment.objects.all()
    return render(request, 'viewparpay.html', {'data': data})

@login_required(login_url='log')
def view_par_booking(request):
    data = booking.objects.all()
    return render(request, 'viewparbooking.html', {'data': data})



def logout_view(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def delete_profile_parent(request):
    user =request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'Your Account Deleted Successfully')
        return redirect('log')
    return render(request,'parentdelete_profile.html')

