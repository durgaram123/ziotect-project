
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
   
    path('about/', views.about,name='about'),
    path('service/', views.service,name='service'),
    path('news/', views.news,name='news'),
    path('contact/', views.contact,name='contact'),
    path('card/', views.card, name='card'),
    path('sub/', views.sub, name='sub'),

  
   
    path('contact1/', views.contact1,name='contact1'),
    path('dashboard_2/', views.dashboard_2,name='dashboard_2'),
    path('dashboard/', views.dashboard,name='dashboard'),
    
    path('plutonews/', views.plutonews,name='plutonews'),
    path('edit_1/<int:id>',views.edit_1, name='edit_1' ), 
    path('delete_1/<int:id>',views.delete_1, name='delete_1' ),
    path('add_1/',views.add_1,name='add_1'),

    path('plutotest/', views.plutotest,name='plutotest'),
    path('edit/<int:id>',views.edit, name='edit'), 
    path('delete_2/<int:id>',views.delete_2, name='delete_2' ),
    path('add_2/',views.add_2,name='add_2'),
    
    path('index1/', views.index1,name='index1'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('settings/', views.settings,name='settings'),
   
    path('subscribe/', views.subscribe, name='subscribe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
