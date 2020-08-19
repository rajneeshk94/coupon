from django.shortcuts import render, redirect
from .models import (CouponAdmin, 
    CouponSU, 
    ReferralforMember
)
from .forms import (Coupon_code_SU, 
    Coupon_code_Admin, 
    Referral_code_Members
)
from django.contrib import messages



def homepage(request):
    context = {}
    return render(request, 'Coupons/home.html', context)

def create_SU_coupon(request):

    context = {}
    # code = CouponSU.objects.get(id=pk)
    form_su = Coupon_code_SU(request.POST)
    if request.method == 'POST':
        if form_su.is_valid():
            form_su.save()
            code = form_su.cleaned_data.get('code')
            messages.success(request, 'Coupon Code is generated successfully!')
            
            # This line can be use to redirect after the code generation
            # return redirect('homepage') 
    
    else:
        form_su = Coupon_code_SU()

    context['form_su'] = form_su

    return render(request, 'Coupons/CouponSUGeneration.html', context)


def create_Admin_coupon(request):

    context = {}
    # code = CouponAdmin.objects.get(id=pk)
    
    if request.method == 'POST':
        form_admin = Coupon_code_Admin(request.POST)
        if form_admin.is_valid():
            form_admin.save()
            code = form_admin.cleaned_data.get('code')
            messages.success(request, 'Coupon Code generated successfully!')
            return redirect('AdminCoupon')
            # This line can be use to redirect after the code generation
            # return redirect('homepage') 

    else:
        form_admin = Coupon_code_Admin()
        
    context['form_admin'] = form_admin

    return render(request, 'Coupons/CouponAdminGeneration.html', context)

def create_Member_referral(request):

    context = {}
    # code = ReferralforMember.objects.get(id=pk)
    form_member = Referral_code_Members(request.POST)
    if request.method == 'POST':
        if form_member.is_valid():
            form_member.save()
            code = form_member.cleaned_data.get('code')
            messages.success(request, 'Referral Code is generated successfully!')
            
            # This line can be use to redirect after the code generation
            # return redirect('homepage') 
    
    else:
        form_member = Referral_code_Members()
    context['form_member'] = form_member

    return render(request, 'Coupons/ReferralMemberGeneration.html', context)


def Coupons(request):
    coupons = CouponSU.objects.all()
    return render(request, 'Coupons/Coupons.html', {'coupons':coupons})
