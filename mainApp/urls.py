from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('reachme/',views.reachme,name="Contact"),
    path('resume/',views.resume,name="Resume"),
    path('<int:project_id>', views.projectdetails, name='projectdetail'),
    path('blog/', include('blogs.urls'),name='Blogs')
]