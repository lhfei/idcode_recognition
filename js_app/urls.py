from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from js_app.views import IDCodeList, IDcodeDetail

urlpatterns = [
    path('idcodes/', IDCodeList.as_view()),
    path('idcodes/<int:pk>/', IDcodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)