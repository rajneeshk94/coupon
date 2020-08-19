from django.urls import path
from Coupons import views



urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('coupons/', views.Coupons, name="Coupons"),
    path('superuser_couponcode/', views.create_SU_coupon, name='SuCoupon'),
    path('admin_couponcode/', views.create_Admin_coupon, name='AdminCoupon'),
    path('Member_Referralcode/', views.create_Member_referral, name='MemberReferral'),

]
