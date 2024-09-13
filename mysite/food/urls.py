

from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    # index-page
    path('',views.IndexClassView.as_view(),name = 'index'),

    path('item/',views.item,name="item"),
    # details-page
    path('detail/<int:pk>/',views.FoodDetail.as_view() , name="detail"),
    # add items
    path('add',views.CreateItem.as_view(),name ="create_item"),
    # edit item
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>/',views.delete_item,name = "delete_item"),
]