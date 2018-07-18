from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(
        template_name = 'polls/list.html'
        ), name='index'),
    path('<int:pk>/', views.DetailView.as_view(
        template_name = 'polls/detail.html'
        ), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(
        template_name = 'polls/results.html'
        ), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
