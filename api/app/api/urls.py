from django.urls import path, re_path
from .views import UserRudView, UserAllView, RecordAllView, RecordRudView, UserCreateView, RecordCreateView, UserLookupView

urlpatterns = [
    path('users/create', UserCreateView.as_view(), name='user-post'),
    path('users/by-id/<pk>', UserRudView.as_view(), name='user-rud'),
    path('users/all', UserAllView.as_view({'get': 'list'}), name='users'),
    path('users/lookup/', UserLookupView.as_view({'get': 'list'}), name='user-lookup'),
    path('records/create', RecordCreateView.as_view(), name='record-post'),
    path('records/all', RecordAllView.as_view({'get': 'list'}), name='records'),
    path('records/by-id/<pk>', RecordRudView.as_view(), name='record-rud')
]
