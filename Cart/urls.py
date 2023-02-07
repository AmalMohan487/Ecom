from django.urls import path
from .import views

urlpatterns = [
    path("CartView",views.CartView, name="CartView"),
    path("AddCart/<int:pk>",views.AddCart, name="AddCart"),
    path("Dele/<int:pk>",views.Dele,name="Dele")

]
