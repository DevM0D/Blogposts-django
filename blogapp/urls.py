from django.urls import path
from blogapp import views

from .views import Homeview , ArticleDetailsview , Addarticle , Editarticle , deletepostarticle , AddComment, Addcatagory ,LikeView 


urlpatterns = [
    path('', Homeview.as_view(), name='home' ),

    path('article/<int:pk>',ArticleDetailsview.as_view() , name="article"),
    path('catagoriesview/',views.catagoriesview , name='catagoriesview'),
    path('add_post/' , Addarticle.as_view() , name="add"),
    path('article/edit/<int:pk>' , Editarticle.as_view() , name="edit"),
    path('article/<int:pk>/remove/' , deletepostarticle.as_view() , name="delete-post"),


    path('add_catagory/' , Addcatagory.as_view() , name="add-catagory"),
    path('catagories/<str:cats>', views.CatagoryView , name="catagories"),
   
    #authentcation
    path('sign/' ,views.register , name= 'sign' ),
    path('login/' ,views.logins , name= 'login' ),
    path('logout' ,views.logouts , name= 'logout' ),


    path('admin_redirect' ,views.admin_redirect , name= 'admin_redirect' ),

    
    path('like/<int:pk>', LikeView , name='like_post'),
    # path('dislike/<int:pk>', DislikeView , name='dislike_post'),
    path('article/<int:pk>/coment>', AddComment.as_view() , name='add_comments'),


]  
