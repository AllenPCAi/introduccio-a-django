from django.urls import path
from .views import Bloglistview, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView


app_name="blog"

urlpatterns = [
    path('inicio/',Bloglistview.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")

]
