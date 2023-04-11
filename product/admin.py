from django.contrib import admin
from product.models import *


admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Review)