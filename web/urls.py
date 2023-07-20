from django.urls import path
from . import views

urlpatterns = [
	
	path("", views.homepage, name="home"),
	path('about-us/', views.about, name="about"),
	path('our-services/', views.services, name="services"),
	path('contact-us/', views.contact, name="contact"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('get-a-quote/', views.getQuote, name="getQuote"),
]
