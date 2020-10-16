from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .models import *
from .models import DirectHR ,DailyDrcallReport
from django.urls import reverse_lazy 
from .form import *

# Create your views here.

def home (request):
	return render(request, 'report/dashboard.html')


def AllDrList(request):
	drlist = DrMasterList.objects.filter( user = request.user)
	return render(request,"../templates/report/AllDrlist.html",{"drlist":drlist})

def MonthlyplanList(request):
	monthlyplan = Monthlyplan.objects.filter( user = request.user)
	return render(request,"../templates/report/monthlyplanlist.html",{"monthlyplan":monthlyplan})



def AllChemistList(request):
	chemistlist = ChemistMasterList.objects.filter( user = request.user)
	return render(request,"../templates/report/allchemistlist.html",{"chemistlist":chemistlist})



def Monthlyplanview(request):
	if request.method == "POST":
		    form = MonthlyPlanForm(request.POST)
		    if form.is_valid():
		    	monthplan = form.save(commit=False)
		    	monthplan.user = request.user
		    	monthplan.save()
		    	return redirect('month-planlist')
	else:
		form = MonthlyPlanForm()
		return render(request, 'report/monthlyplan.html', {'form': form})





def monthlyplan(request):
	if request.method == "POST":
		    form = LeaveHRForm(request.POST)
		    if form.is_valid():
		    	leavehr = form.save(commit=False)
		    	leavehr.user = request.user
		    	leavehr.save()
		    	return redirect('report-home')
	else:
		form = LeaveHRForm()
		return render(request, 'report/LeaveHR.html', {'form': form})




def DirectHR(request):
	if request.method == "POST":
		    form = DirectHRForm(request.POST)
		    if form.is_valid():
		    	directhr = form.save(commit=False)
		    	directhr.user = request.user
		    	directhr.save()
		    	return redirect('report-home')
	else:
		form = DirectHRForm()
		return render(request, 'report/DirectHR.html', {'form': form})		    	
"""class DirectHRView(CreateView):
	model = DirectHR
	fields = [ 'user' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')"""



def LeaveHR(request):
	if request.method == "POST":
		    form = LeaveHRForm(request.POST)
		    if form.is_valid():
		    	leavehr = form.save(commit=False)
		    	leavehr.user = request.user
		    	leavehr.save()
		    	return redirect('report-home')
	else:
		form = LeaveHRForm()
		return render(request, 'report/LeaveHR.html', {'form': form})	


def leave_list (request):
	leave = LeaveHR.objects.all()
	return render(request, 'report/LeaveHR.html',{"leave":leave})




def Doctor_Master_List(request):
	if request.method == "POST":
		    form = DrMasterListForm(request.POST)
		    if form.is_valid():
		    	masterDoctorList = form.save(commit=False)
		    	masterDoctorList.user = request.user
		    	masterDoctorList.save()
		    	return redirect('drlist')
	else:
		form = DrMasterListForm()
		return render(request, 'report/doctormasterlist.html', {'form': form})	



def chemist_Master_List(request):
	if request.method == "POST":
		    form = chemistListForm(request.POST)
		    if form.is_valid():
		    	masterchemistList = form.save(commit=False)
		    	masterchemistList.user = request.user
		    	masterchemistList.save()
		    	return redirect('chemistlist')
	else:
		form = chemistListForm()
		return render(request, 'report/chemistmasterlist.html', {'form': form})	

def dailyactivites (request):
	return render(request, 'report/dailyactivites.html')


def FieldActivites(request):
	if request.method == "POST":
		form = FieldForm(request.POST)
		if form.is_valid():
			fieldactivites = form.save(commit=False)
			fieldactivites.user = request.user
			fieldactivites.save()
			return redirect('dailydrcall')
	else:
		form = FieldForm()
	return render(request,  '../templates/report/fieldactivites.html', {'form': form})	


def DailyDrcallReportview(request):
	if request.method == "POST":
		form = DailyDrcallReportForm(request.POST)
		if form.is_valid():
			drlist = DrMasterList.objects.all().first()
			dailycallreport = form.save(commit=False)
			dailycallreport.user = request.user
			dailycallreport.dr_name = drlist
			dailycallreport.save()
			return redirect('dailychemistmeetingreport')
	else:
		form = DailyDrcallReportForm()
	return render(request,  '../templates/report/DailyDrcallReport.html', {'form': form})	




def DailyChemistcallReportview(request):
	if request.method == "POST":
		form = DailyChemistcallReportForm(request.POST)
		if form.is_valid():
			chrlist = ChemistMasterList.objects.all().first()
			dailycallreport = form.save(commit=False)
			dailycallreport.user = request.user
			dailycallreport.chemist_name = chrlist
			dailycallreport.save()
			return redirect('expenses-report')
	else:
		form = DailyChemistcallReportForm()
	return render(request,  '../templates/report/dailychemistcallreport.html', {'form': form})






def ExpensesView(request):
	if request.method == "POST":
		form = ExpensesForm(request.POST)
		if form.is_valid():
			expenseslist = Expenses.objects.all()
			expenseslist = form.save(commit=False)
			expenseslist.user = request.user
			
			expenseslist.save()
			return redirect('report-home')
	else:
		form = ExpensesForm()
	return render(request,  '../templates/report/Expenses.html', {'form': form})




def MeetingActivites(request):
	if request.method == "POST":
		form = MeetingForm(request.POST)
		if form.is_valid():
			meetingactivites = form.save(commit=False)
			meetingactivites.user = request.user
			meetingactivites.save()
			return redirect('dailydrmeetingreport')
	else:
		form = MeetingForm()
	return render(request,  '../templates/report/meetingactivites.html', {'form': form})	



def DailyDrMeetingReportview(request):
	if request.method == "POST":
		form = DailyDrMeetingReportForm(request.POST)
		if form.is_valid():
			drlist = DrMasterList.objects.all().first()
			dailycallreport = form.save(commit=False)
			dailycallreport.user = request.user
			dailycallreport.dr_name = drlist
			dailycallreport.save()
			return redirect('report-home')
	else:
		form = DailyDrMeetingReportForm()
	return render(request,  '../templates/report/DailyDrMeetingReport.html', {'form': form})	



def OthersActivity(request):
	if request.method == "POST":
		form = OtherForm(request.POST)
		if form.is_valid():
			otherctivites = form.save(commit=False)
			otherctivites.user = request.user
			otherctivites.save()
			return redirect('OthersActivityView')
	else:
		form = OtherForm()
	return render(request,  '../templates/report/otheractivites.html', {'form': form})



def OthersActivityView(request):
	if request.method == "POST":
		form = OtherViewForm(request.POST)
		if form.is_valid():
			otherctivitesview = form.save(commit=False)
			otherctivitesview.user = request.user
			otherctivitesview.save()
			return redirect('report-home')
	else:
		form = OtherViewForm()
	return render(request,  '../templates/report/otheractivitesview.html', {'form': form})


class WorkFromHomeActivites(CreateView):
    model = DailyActivites
    form_class = WorkFromHomeForm
    template_name = '../templates/report/workfromhomeactivites.html'

    def form_valid(self,form):
        user = form.save()
        user.is_workFromHome = form.save()
        return redirect('report-home')



class covidActivites(CreateView):
    model = DailyActivites
    form_class = CovidForm
    template_name = '../templates/report/covidactivites.html'

    def form_valid(self,form):
        user = form.save()
        user.is_covid19 = form.save()
        return redirect('report-home')

class AdminDayActivites(CreateView):
    model = DailyActivites
    form_class = AdminDayForm
    template_name = '../templates/report/admindayactivites.html'

    def form_valid(self,form):
        user = form.save()
        user.is_adminDay = form.save()
        return redirect('report-home')

"""class DrVisitView(CreateView):
	model = Dr_Visit
	fields = ['user','dr_name',
	'city' , 'dr_speciality' , 'month' ,
	 'business' ] #describe the field need to create 
	success_url = reverse_lazy('home')"""
"""
class DailyplanView(CreateView):
	model = Daily_plan
	fields = ['day', 'user' , ] #describe the field need to create 
	success_url = reverse_lazy('home')

class DrvisitreportView(CreateView):
	model = Dr_visit_report
	fields = ['dr_name', 
	'user' , 'city', 
	'place', 'dr_speciality'] #describe the field need to create 
	success_url = reverse_lazy('home')

class ExpensesView(CreateView):
	model = Expenses
	fields = ['working_place', 'user' , 
	'calls_made', 
	'chemist_meeting',
	 'travelling_from', 'travelling_to' , 
	 'distance_travelled' , 'total_appointment' , 
	 'daily_allowance' ,'telephone_internet_expenses' , 'total'] #describe the field need to create 
	success_url = reverse_lazy('home')

class DailyworkingreportView(CreateView):
	model = DailyWorkingReport
	fields = ['dr_name', 'user' , 
	'meeting_place',
	 'prescrebtionBrand',
	  'dr_speciality', 'user_WorkingPlace', 
	  'current_month_business',
	  'Daily_business_outcomes'] #describe the field need to create 
	success_url = reverse_lazy('home')


class ChemistcallreportView(CreateView):
	model = chemist_call_report
	fields = ['chemist_name', 'user' ,
	'business_outcomes_chemist_visit'] #describe the field need to create 
	success_url = reverse_lazy('home')


class DaysummaryreportView(CreateView):
	model = day_summary
	fields = ['user', 'total_calls' ,
	 'business_outcomes_of_total_calls',
	  'total_chemist_meeting',
	   'business_outcomes_of_total_metting', 'delayed_submission'] #describe the field need to create 
	success_url = reverse_lazy('home')



class RcpadetailsView(CreateView):
	model = RCPA_details
	fields = ['brand_name', 'user' ,
	 'competitor_name1', 
	 'competitor_name2', 'competitor_name3' , 'competitor_name4', 'competitor_name5' ,
	  'competitor_name6', 'competitor_name7'] #describe the field need to create 
	success_url = reverse_lazy('home')



class DoctorvisitView(CreateView):
	model = doctor_visit_report
	fields = ['doctor_name', 'user' , 'city',
	 'month', 'dr_speciality'] #describe the field need to create 
	success_url = reverse_lazy('home')

class HQView(CreateView):
	model = HQ_List
	fields = ['user','dr_name',
	'city' , 'dr_speciality' , 'place' ,
	 'current_doctor_business', 'current_prescribing_brand',
	  'brand_name1','brand_name2','brand_name3',
	  'brand_name4', 'brand_name5' ] #describe the field need to create 
	success_url = reverse_lazy('home')

class chemistlist(CreateView):
	model = chemistlist
	fields = ['user', 'chemist_name', 'place', 'contact',
	 'POB_Collection_status','ABM_Approach_Status', 'brand_name1', 'brand_name2' ,
	  'brand_name3' ] #describe the field need to create 
	success_url = reverse_lazy('home')"""