from django.urls import path
from django.contrib import admin
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio_home, name='portfolio_home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/submit/', views.submit_contact, name='submit_contact'),

 ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)