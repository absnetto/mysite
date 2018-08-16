from django.urls import path

# importa o codigo do modulo views no diretório corrente,
# este modulo foi adicionado manualmente
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>', views.vote, name='vote'),
]