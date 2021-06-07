from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserOrder)
admin.site.register(GuestOrder)
admin.site.register(Refund)
admin.site.register(Coupon)
admin.site.register(Payment)
