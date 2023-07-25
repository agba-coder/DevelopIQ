from django.contrib import admin
from .models import Testimonial, Quote, Mail

# Register your models here.

admin.site.register(Testimonial)
admin.site.register(Quote)
admin.site.register(Mail)