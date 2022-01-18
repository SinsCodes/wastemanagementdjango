from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


# from mainpro import settings
from .import views

urlpatterns = [
    path('index/', views.index),
    path('rest/', views.rest_base),
    path('add_res/', views.add_res),
    path('add_ngo/', views.add_ngo),
    path('ad_view/', views.admin_view),
    path('view_rest/', views.view_rest),
    path('view_ngo/', views.view_ngo),
    path('list_ngo/', views.list_ngo),
    path('list_rest/', views.list_rest),
    path('del_rest/', views.delete_resdata),
    path('del_ngo/', views.del_ngodata),
    path('index_log/', views.index_login),
    path('logout_res/', views.logout_res),
    path('logout_ngo/', views.logout_ngo),
    path('logout_admin/', views.logout_admin),
    path('employee_add/', views.employee_add),
    path('employee_reg/', views.employee_reg),
    path('employee_list/', views.employee_list),
    path('send_email/',views.send_emailngo),
    path('send_restemail/',views.send_emailrest),
    path('send_emailemp/', views.send_emailemp),
    path('ngo_email/',views.ngo_email),
    path('rest_email/',views.rest_email),
    path('update_email/',views.update_email),
    path('update_ngo/', views.update_ngo),
    path('up_res/', views.update_res),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
