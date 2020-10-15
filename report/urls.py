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
    path('daily-activites/', views.dailyactivites, name = 'dailyactivites'),
    path('field-activites/', views.FieldActivites, name = 'fieldactivites'),
    path('daily-dr-call/', views.DailyDrcallReportview, name = 'dailydrcall'),
    path('daily-dr-meeting-report/', views.DailyDrMeetingReportview, name = 'dailydrmeetingreport'),
    path('daily-chemist-callReport-view/', views.DailyChemistcallReportview, name = 'dailychemistmeetingreport'),
    path('otheractivites/', views.OthersActivity, name = 'otheractivites'),
     path('otheractivitesview/', views.OthersActivityView, name = 'OthersActivityView'),


    path('meetingactivites/', views.MeetingActivites, name = 'meetingactivites'),
    path('workfromhomeactivites/', views.WorkFromHomeActivites.as_view(), name = 'workfromhomeactivites'),
    path('covidactivites/', views.covidActivites.as_view(), name = 'covidactivites'),
    path('admindayactivites/', views.AdminDayActivites.as_view(), name = 'admindayactivites'),
    path('expensesreport/', views.ExpensesView , name = 'expenses-report' )
  
 #   path('dailyplan/', views.DailyplanView.as_view() , name = 'dailyplan-report' ),
  # 	path('drvisitreport/', views.DrvisitreportView.as_view() , name = 'drvisitreport-report' ),
   	
   	#path('dailyworkingreport/', views.DailyworkingreportView.as_view() , name = 'dailyworkingreport-report' ),
   	#path('chemistcallreport/', views.ChemistcallreportView.as_view() , name = 'chemistcall-report' ),
   	#path('daysummaryreport/', views.DaysummaryreportView.as_view() , name = 'daysummary-report' ),
   	#path('rcpareport/', views.RcpadetailsView.as_view() , name = 'rcpa-report' ),
   	#path('doctorvisitreport/', views.DoctorvisitView.as_view() , name = 'doctorvisit-report' ),
   	#path('hqlist/', views.HQView.as_view() , name = 'hq-report' ),
   	#path('chemistlist/', views.chemistlist.as_view() , name = 'chemist-list' ),



]


