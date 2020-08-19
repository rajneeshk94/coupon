from django.db import models
import random, datetime


# This function below will create a random Coupon code
def get_promo_code(num_chars):
     code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     code = ''
     for i in range(0, num_chars):
         slice_start = random.randint(0, len(code_chars) - 1)
         code += code_chars[slice_start: slice_start + 1]
     return code


# This is the model created for Coupon code which is 8 characters long
class CouponSU(models.Model):

    CATEGORY = (
        ('Admin', 'Admin'),
        ('Member', 'Member')
    )


    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    code = models.CharField(max_length=10, unique=True, null=False)
    description = models.TextField(default=None, blank=True, null=True)
    valid_from = models.DateField(default=datetime.date.today)
    valid_till = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class CouponAdmin(models.Model):

    code = models.CharField(default=get_promo_code(8), max_length=8, unique=True, null=False)
    description = models.TextField(default=None, blank=True)
    valid_from = models.DateField(default=datetime.date.today)
    valid_till = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.code

class ReferralforMember(models.Model):
    code = models.CharField(default=get_promo_code(6), max_length=6, unique=True, null=False)
    description = models.TextField(default=None)
    valid_from = models.DateField(default=datetime.date.today)
    valid_till = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.code
