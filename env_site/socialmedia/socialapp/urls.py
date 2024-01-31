from django.urls import path
from socialapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('Sign_up/',views.sign_up,name='Sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_out/',views.sign_out,name='sign_out'),
    path('profile_settings/',views.profile_settings,name='profile_settings'),
    path('add_post/',views.add_post,name='add_post'),
    path('like_post/<int:post_id>/',views.like_post,name='like_post'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('block_user/<int:user_id>/',views.block_user,name='block_user'),
    path('make_admin/<int:user_id>/',views.make_admin,name='make_admin')
]