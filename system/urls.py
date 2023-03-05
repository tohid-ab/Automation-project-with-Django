from django.urls import path, include
from .views import *

app_name = 'system'

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    # نامه نگاری
    path('letter-writing/create/', CreateNaame.as_view(), name='namenegari'),
    path('letter-writing/list/', ListNaame.as_view(), name='list-name'),
    path('letter-writing/my-list/', MyListNaame.as_view(), name='my-list-name'),
    path('letter-writing/detail/<slug>', NaameDetail.as_view(), name='detail-naame')
]
