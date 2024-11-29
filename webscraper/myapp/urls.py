from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape_website, name='scrape_website'),
    path('delete/', views.delete_urls, name="delete") # Define a URL that triggers the scrape_website view)
]
