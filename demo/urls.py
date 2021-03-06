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
    post_create_in_column,
    post_list_for_user,
    add_worker_for_column,
    post_approve,
    post_reject
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/<int:id>/', account_profile, name='account-profile'),
    path('accounts/profile/post-list/<int:id>' , post_list_for_user, name='post-list-user'),
    path('columns/<int:id>/', column_list, name='column-list'),
    path('columns/create/', ColumnFormView.as_view(), name='column-create'),
    path('columns/column/<int:column_id>/', post_list, name='post-list'),
    path('columns/column/workers/add/<int:column_id>/', add_worker_for_column, name='add-worker'),
    path('post/create/<int:column_id>/', post_create_in_column, name='post-create'),
    path('posts/post/<int:post_id>/', post_detail, name='post-detail'),
    path('posts/post/approve/<int:post_id>/', post_approve, name='post-approve'),
    path('posts/post/reject/<int:post_id>/', post_reject, name='post-reject'),
    path('subscribe/<int:column_id>/', subscribe, name='subscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
