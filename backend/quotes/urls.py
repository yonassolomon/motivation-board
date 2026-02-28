from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
urlpatterns=[
    path('quotes/',views.quote_list,name='quote_list'),
    path('quotes/<int:pk>/',views.quote_detail,name='quote_detail'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]