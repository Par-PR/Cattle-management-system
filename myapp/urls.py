
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contactus, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.userlogout, name='logout'),
    path('addcattledata', views.addcattledata, name='addcattledata'),
    path('cattledatashow', views.cattledatashow, name='cattledatashow'),
    path('cattledatashowbuyer', views.cattledatashowbuyer, name='cattledatashowbuyer'),
    path('aboutbuyer', views.aboutbuyer, name='aboutbuyer'),
    path('contactbuyer', views.contactusbuyer, name='contactbuyer'),
    path('indexbuyer', views.indexbuyer, name='indexbuyer'),
    path('cattledetail/<int:stid>', views.cattledetail, name='cattledetail'),
    path('cattledetailbuyer/<int:stid>', views.cattledetailbuyer, name='cattledetailbuyer'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('newpassword', views.newpassword, name='newpassword'),
    path('registrationcheck', views.registrationcheck, name='registrationcheck'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    
]