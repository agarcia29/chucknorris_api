from django.urls import path
from .views import JokeView

urlpatterns = [
    path('jokes/', JokeView.as_view(), name='jokes'),
    path('jokes/create/', JokeView.as_view(), name='create_jokes'),
    path('jokes/update/<int:id>/', JokeView.as_view(), name='update_jokes'),
    path('jokes/delete/<int:id>/', JokeView.as_view(), name='delete_jokes'),
]
