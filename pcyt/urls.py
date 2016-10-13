from django.conf.urls import url
from django.contrib import admin
from posts import views 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
    url(r'^noticias/', views.NotiView.as_view(), name="noti"),
    url(r'^pcyt/', views.ListView.as_view(), name="con"),
    url(r'^planta/', views.List2View.as_view(), name="planta"),
    url(r'^contacto/', views.List3View.as_view(), name="contacto"),
    url(r'^organigrama/', views.List4View.as_view(), name="organi"),
    url(r'^manuale_de_opereacion/', views.List5View.as_view(), name="ope"),
    url(r'^manual_de_procedimiento/', views.List6View.as_view(), name="pro"),
    url(r'^matriz_de_identificacion/', views.List7View.as_view(), name="idef"),
    url(r'^antecedentes/', views.AntecedenteView.as_view(), name="antecedentes"),
    url(r'^funciones/', views.FuncionesView.as_view(), name="funciones"),
    url(r'^mision_y_vision/', views.MisionView.as_view(), name="mision"),
    url(r'^objetivo/', views.ObjetivoView.as_view(), name="objetivo"),
    
]
