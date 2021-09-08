from django.urls import path
from .views import CookieStandList, CookieStanddetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="CookieStandList"),
    path("<int:pk>/", CookieStanddetail.as_view(), name="CookieStanddetail"),
]
