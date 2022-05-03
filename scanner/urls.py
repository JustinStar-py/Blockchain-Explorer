from scanner.views import home, scanner
from django.urls import path


app_name = "scan"

urlpatterns = [
    path('',home,name="scanner"),
    path('scan',scanner.as_view(),name="detail_account_address"),
    path('scan/<slug:search>',scanner.as_view(),name="detail_account_address")
]
