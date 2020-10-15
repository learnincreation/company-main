from . import views
from django.urls import path

from . import views 
from .views import * 

urlpatterns = [
    path('home/', views.home , name = 'report-home' ),
    path('drlist/', views.AllDrList , name = 'drlist' ),
    path('chemistlist/', views.AllChemistList , name = 'chemistlist' ),
    path('directhr/', views.DirectHR, name = 'direct-hr'),
  	path('leavehr/', views.LeaveHR, name = 'leave-hr'),
    path('master-doctor-list/', views.Doctor_Master_List, name = 'masterdrlist'),
    path('chemist-doctor-list/', views.chemist_Master_List, name = 'masterchemlist'),
    path('dailyactivites/', views.dailyactivites, name = 'dailyactivites'),
    path('fieldactivites/', views.FieldActivites, name = 'fieldactivites'),
    path('dailydrcall/', views.DailyDrcallReportview, name = 'dailydrcall'),
    path('dailydrmeetingreport/', views.DailyDrMeetingReportview, name = 'dailydrmeetingreport'),
    path('otheractivites/', views.OthersActivity, name = 'otheractivites'),
     path('otheractivitesview/', views.OthersActivityView, name = 'OthersActivityView'),


    path('meetingactivites/', views.MeetingActivites, name = 'meetingactivites'),
    path('workfromhomeactivites/', views.WorkFromHomeActivites.as_view(), name = 'workfromhomeactivites'),
    path('covidactivites/', views.covidActivites.as_view(), name = 'covidactivites'),
    path('admindayactivites/', views.AdminDayActivites.as_view(), name = 'admindayactivites'),
    
  
 #   path('dailyplan/', views.DailyplanView.as_view() , name = 'dailyplan-report' ),
  # 	path('drvisitreport/', views.DrvisitreportView.as_view() , name = 'drvisitreport-report' ),
   #	path('expensesreport/', views.ExpensesView.as_view() , name = 'expenses-report' ),
   	#path('dailyworkingreport/', views.DailyworkingreportView.as_view() , name = 'dailyworkingreport-report' ),
   	#path('chemistcallreport/', views.ChemistcallreportView.as_view() , name = 'chemistcall-report' ),
   	#path('daysummaryreport/', views.DaysummaryreportView.as_view() , name = 'daysummary-report' ),
   	#path('rcpareport/', views.RcpadetailsView.as_view() , name = 'rcpa-report' ),
   	#path('doctorvisitreport/', views.DoctorvisitView.as_view() , name = 'doctorvisit-report' ),
   	#path('hqlist/', views.HQView.as_view() , name = 'hq-report' ),
   	#path('chemistlist/', views.chemistlist.as_view() , name = 'chemist-list' ),



]


