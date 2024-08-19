"""
URL configuration for vegetables project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from vapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BASEE',views.BASEE),
    path('base',views.base),
    path('adbase',views.adbase),
    path('frbase',views.frbase),
    path('usrbase',views.usrbase),
    path('',views.index1),
    path('frreg',views.frreg),
    path('usrreg',views.usrreg),
    path('contact',views.contact),
    path('adcon',views.adcon),
    path('adrply/<int:id>',views.adrply,name='adrply'),
    path('inbox',views.inbox,name='inbox'),
    path('adlog',views.adlog),
    path('adfmview',views.adfmview,name='adfmview'),
    path('usrview',views.usrview,name='usrview'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('adlogout',views.adlogout),
    path('farmlog',views.farmlog),
    path('forgotfarm',views.forgotfarm,name='forgotfarm'),
    path('forgotusr',views.forgotusr,name='forgotusr'),
    path('addpro',views.addpro),
    path('mngpro',views.mngpro),
    path('mycart',views.mycart,name='mycart'),
    path('minuscart/<int:id>',views.minuscart),
    path('pluscart/<int:id>',views.pluscart),
    path('delete_c/<int:id>',views.delete_c),
    path('addtocart/<int:id>',views.addtocart),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
    path('frlogout',views.frlogout),
    path('usrlog',views.usrlog),
    path('usrlogout',views.usrlogout),
    path('usrdisplay',views.usrdisplay,name='usrdisplay'),
    path('Usrdisplayy2/<int:id>',views.Usrdisplayy2,name='Usrdisplayy2'),
    path('msg',views.msg,name='msg'),
    path('admsg',views.admsg,name='admsg'),
    path('search',views.search),
    path('index',views.index),
    path('adindex',views.adindex),
    path('frindex',views.frindex),
    path('usrindex',views.usrindex,name='usrindex'),
    path('gallery',views.gallery),
    path('account',views.account,name='account'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout),
    path('myacc',views.myacc,name='myacc'),
    path('EDT/<int:id>',views.EDT,name='EDT'),
    path('order',views.order,name='order'),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('plusbuy/<int:id>',views.plusbuy),
    path('minusbuy/<int:id>',views.minusbuy),
    path('mybuy/<int:id>',views.mybuy,name='mybuy'),
    path('prodisp',views.prodisp,name='prodisp'),
    path('fmsg',views.fmsg,name='fmsg'),
    path('adpay',views.adpay,name='adpay'),
    path('empty',views.empty,name='empty'),
    path('fpay',views.fpay,name='fpay'),
    path('adshare/<int:id>',views.adshare,name='adshare'),
    path('create/',views.create_payment,name='create_payment'),
    path('success',views.success,name='success'),
    # path('callback/',views.payment_callback,name='payment_callback'),
    path('cart_payment',views.cart_payment,name='cart_payment'),
    path('csuccess',views.csuccess,name='csuccess'),
    path('resetuser/<token>',views.reset_passworduser,name='reset_passworduser'),
    path('resetfarm/<token>',views.reset_passwordfarm,name='reset_passwordfarm'),
    path('delivery/<int:id>',views.delivery,name='delivery'),
    path('deliveries/<int:id>',views.deliveries,name='deliveries'),






    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

