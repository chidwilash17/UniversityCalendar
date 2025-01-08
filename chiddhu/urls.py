"""
URL configuration for chiddhu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include,path
from lily import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login_view', views.login_view, name='login'),
    path('calander/', views.calander, name='calander'),
    path('tables/', views.tables, name='tables'),
    path('tables2/', views.tables2, name='tables2'),
    path('tables3/', views.tables3, name='tables3'),
    path('tables4/', views.tables4, name='tables4'),
    path('christmas/', views.christmas, name='christmas'),
    path('newyear/', views.newyear, name='newyear'),
    path('guru/', views.guru, name='guru'),
    path('bhogi/', views.bhogi, name='bhogi'),
    path('sankranti/', views.sankranti, name='sankranti'),
    path('kanuma/', views.kanuma, name='kanuma'),
    path('swami/', views.swami, name='swami'),
    path('bosee/', views.bosee, name='bosee'),
    path('republic/', views.republic, name='republic'),
    path('valentine/', views.valentine, name='valentine'),
    path('shivaji/', views.shivaji, name='shivaji'),
    path('shiva/', views.shiva, name='shiva'),
    path('holi/', views.holi, name='holi'),
    path('ugadi/', views.ugadi, name='ugadi'),
    path('ramzan/', views.ramzan, name='ramzan'),
    path('ram/', views.ram, name='ram'),
    path('mahavir/', views.mahavir, name='mahavir'),
    path('ambedkar/', views.ambedkar, name='ambedkar'),
    path('gfriday/', views.gfriday, name='gfriday'),
    path('easter/', views.easter, name='easter'),
    path('tagore/', views.tagore, name='tagore'),
    path('mother/', views.mother, name='mother'),
    path('buddha/', views.buddha, name='buddha'),
    path('bakrid/', views.bakrid, name='bakrid'),
    path('lily/', include('lily.urls')),
    
]

