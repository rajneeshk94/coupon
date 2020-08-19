from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (CouponSU, CouponAdmin, ReferralforMember)
# Register your models here.


class SuperUserAdmin(UserAdmin):
    list_display = ('code', 'category', 'valid_from', 'valid_till')
    search_fields = ('category', )
    readonly_fields = ('valid_from', 'valid_till')

    ordering = ('code',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(CouponSU, SuperUserAdmin)
admin.site.register((CouponAdmin, ReferralforMember))

