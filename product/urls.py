from django.urls import path
from product import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


path('login/',views.login,name = "loginpage"),
path('register/',views.register,name="registerpage"),
path('',views.index,name ="indexpage"),
path('logout/',views.logout,name="logoutpage"),
path('products/',views.product,name="productpage"),
path('final/',views.finals,name="finalpage"),
path('cart/', views.cart_view, name="cart_new"),
 




]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)