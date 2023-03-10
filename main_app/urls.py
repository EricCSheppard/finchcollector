from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='index'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>', views.finch_detail, name='detail'),
    path('finches/<int:finch_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('finches/<int:finch_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
    path('tags/create', views.TagCreate.as_view(), name='tags_create'),
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
]