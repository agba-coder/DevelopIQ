from django.db import models

# Create your models here.


class Testimonial(models.Model):
	company_logo = models.ImageField(blank=False, upload_to="uploads/")
	company_name = models.CharField(max_length=50)
	name_or_title = models.CharField(max_length=70)
	testimony = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.company_name}'s Testimonial"

	class Meta:
		ordering = ('-date_created',)
		verbose_name_plural = 'Testimonials'


class Quote(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	contact = models.CharField(max_length=14)
	country = models.CharField(max_length=10)
	approximated_budget = models.CharField(max_length=20)
	whatsapp_number = models.CharField(max_length=14)
	details = models.TextField()
	service_type = models.CharField(max_length=20)
	start_date = models.CharField(max_length=20)
	company_name = models.CharField(max_length=50)
	postion = models.CharField(max_length=15)
	how_did_you_know_us = models.CharField(max_length=15)
	file = models.FileField(upload_to="uploadFiles/")
	date_created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.company_name}'s Quote"


	class Meta:
		ordering = ('-date_created',)
		verbose_name_plural = 'Quotes'

