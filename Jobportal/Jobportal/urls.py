"""Jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import   the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.http import HttpResponseNotFound
from job.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('admin_login', admin_login,name="admin_login"),
    path('user_login', user_login,name="user_login"),
    path('recruiter_login', recruiter_login,name="recruiter_login"),
    path('recruiter_signup', recruiter_signup,name="recruiter_signup"),
    path('user_signup', user_signup,name="user_signup"),
    path('admin_home', admin_home,name="admin_home"),
    path('user_home', user_home,name="user_home"),
    path('recruiter_home', recruiter_home,name="recruiter_home"),
    path('delete_user<int:pid>', delete_user,name="delete_user"),
    path('change_status<int:pid>', change_status,name="change_status"),
    path('Logout', Logout,name="Logout"),
    path('recruiter_panding', recruiter_panding,name="recruiter_panding"),
    path('recruiter_rejected', recruiter_rejected,name="recruiter_rejected"),
    path('recruiter_accepted', recruiter_accepted,name="recruiter_accepted"),
    path('recruiter_all', recruiter_all,name="recruiter_all"),
    path('view_users', view_users,name="view_users"),
    path('add_job', add_job,name="add_job"),
    path('delete_recruiter/<int:pid>', delete_recruiter,name="delete_recruiter"),
    path('edit_jobdetail/<int:pid>', edit_jobdetail,name="edit_jobdetail"),
    path('change_passwordadmin', change_passwordadmin,name="change_passwordadmin"),
    path('change_passworduser', change_passworduser,name="change_passworduser"),
    path('change_passwordrecruiter', change_passwordrecruiter,name="change_passwordrecruiter"),
    path('change_companylogo/<int:pid>', change_companylogo, name="change_companylogo"),
    path('job_list', job_list,name="job_list"),
    path('contactus', contactus, name="contactus"),
    path('aboutus', aboutus, name="aboutus"),
    path('learning', learning, name="learning"),
    path('myportfolio', myportfolio, name="myportfolio"),
    path('latest_job', latest_jobs, name="latest_job"),
    path('applied_jobs', applied_jobs, name="applied_jobs"),
    path('user_latestjobs', user_latestjobs, name="user_latestjobs"),
path('job_detail/<int:pid>', job_detail, name="job_detail"),
path('applyforjob/<int:pid>', applyforjob, name="applyforjob"),
re_path(r'^.*/$', lambda request: HttpResponseNotFound('<script>alert("Page not found"); window.location.href="/";</script>')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



















