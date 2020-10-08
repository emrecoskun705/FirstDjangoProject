from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import (
    HomePageView, 
    ColumnFormView, 
   
    account_profile, 
    column_list, 
    post_list, 
    post_detail,
    subscribe,
    post_create_in_column
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/<int:id>/', account_profile, name='account-profile'),
    path('columns/<int:id>/', column_list, name='column-list'),
    path('columns/create/', ColumnFormView.as_view(), name='column-create'),
    path('columns/column/<int:column_id>/', post_list, name='post-list'),
    path('post/create/<int:column_id>/', post_create_in_column, name='post-create'),
    path('posts/post/<int:post_id>/', post_detail, name='post-detail'),
    path('subscribe/<int:column_id>/', subscribe, name='subscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
