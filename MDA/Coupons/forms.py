from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import (CouponSU, CouponAdmin, ReferralforMember)


# Form generation for Super User level coupon code
class Coupon_code_SU(ModelForm):
    class Meta:
        model = CouponSU
        fields = "__all__"


# Form generation for Admin level coupon code
class Coupon_code_Admin(ModelForm):
    class Meta:
        model = CouponAdmin
        fields = "__all__"


# Form generation for Member level Referral code
class Referral_code_Members(ModelForm):
    class Meta:
        model = ReferralforMember
        fields = "__all__"