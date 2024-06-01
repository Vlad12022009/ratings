from django.contrib import admin
from django.urls import path
from rating.views import (
                        SimpleFormView,
                        RatingListView,            
                        RatingEntryListView,
                        RatingsDetailView,
                        )
from registration.views import RegistarionView, LoginView, ProfileView
from pagination_example.views import pagination_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RatingListView.as_view(), name='main'),
    path('form/', SimpleFormView.as_view()),
    path('entry/<name>/', RatingEntryListView.as_view()),
    path('rating/<int:pk>/', RatingsDetailView.as_view()),
    path('register/', RegistarionView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/profile/', ProfileView.as_view()),
    path('pagination_example/', pagination_view)
]
