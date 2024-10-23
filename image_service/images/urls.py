from django.urls import path
from .views import image_delete, image_list, image_upload, image_view

urlpatterns = [
    path('', image_upload, name='image_upload'),
    path('view/<int:image_id>/', image_view, name='image_view'),
    path('delete/<int:image_id>/', image_delete, name='image_delete'),
    path('list/', image_list, name='image_list'),
]
