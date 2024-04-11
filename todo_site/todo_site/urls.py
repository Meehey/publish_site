from django.contrib import admin
from django.urls import path,  include
from todo import views

urlpatterns = [
	
	path('', views.index, name="todo"),
	path('del/<str:item_id>', views.remove, name="del"),
	path('admin/', admin.site.urls),
    path('edit/<str:item_id>', views.edit, name="edit"),
    path('auth/', include('user.urls'))
]
