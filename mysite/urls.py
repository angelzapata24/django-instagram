from django.urls import path
from . import views

app_name = "mysite"

urlpatterns = [
    path("add/", views.AddPicture.as_view(), name="add"),
    path("feed/", views.PicView.as_view(), name="feed"),
    path('delete/<image_id>', views.DeletePic.as_view(), name='delete'),
    path('comment/<image_id>', views.InsertComment.as_view(), name='comment'),
    path('filter/<image_id>', views.AddFilter.as_view(), name='filter'),
    path('filter/blue_filter/<image_id>', views.blue_filter, name='blue')
]
