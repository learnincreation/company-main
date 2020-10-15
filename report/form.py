from django import forms
from django.forms import ModelForm
from django.db import transaction
from company import settings

from report.models import *

class DirectHRForm(forms.ModelForm):
	class Meta :
		model = DirectHR  
		fields = [ "message"]


class LeaveHRForm(forms.ModelForm):
	class Meta :
		model = LeaveHR  
		fields = [ "reason"]


class DrMasterListForm(forms.ModelForm):
	class Meta :
		model = DrMasterList  
		fields = [ 'dr_name' , 'dr_speciality', 'city' ]


class chemistListForm(forms.ModelForm):
	class Meta :
		model = ChemistMasterList  
		fields = [ 'chemist_name' , 'mobile', 'city' ]


class FieldForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = [ 'is_field']

class DailyDrcallReportForm(forms.ModelForm):
    class Meta:
        model = DailyDrcallReport
        fields = [ 'dr_name','dr_speciality', 'Place',  'workwith' ,  'current_prescribing_brand','brand_name1','brand_name2','brand_name3','brand_name4','brand_name5','current_month_business']

class DailyChemistcallReportForm(forms.ModelForm):
    class Meta:
        model = DailyChemistcallReport
        fields = [ 'chemist_name', 'Place','brand_name1','brand_name2', 'brand_name3' , "mobile"]


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = [ 'calls_made', 
    'chemist_meeting',
     'travelling_from', 'travelling_to' , 
     'distance_travelled' , 'total_appointment' , 
     'daily_allowance' ,'telephone_internet_expenses' , 'total'] 



class DailyDrMeetingReportForm(forms.ModelForm):
    class Meta:
        model = DailyDrMeetingReport
        fields = [ 'dr_name','dr_speciality','meeting_place']
    
    
    

class MeetingForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = ['is_meeting']



class DailyDrMeetingReportForm(forms.ModelForm):
    class Meta:
        model = DailyDrMeetingReport
        fields = ['dr_name','dr_speciality','meeting_place']


class OtherForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = ['is_other']
    



class OtherViewForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = ['text']
    



  
    
    
    

class CovidForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = ['is_covid19']
    
    @transaction.atomic
    def save(self):
      
        user.is_covid19 = True
        user.save()
        return user


class WorkFromHomeForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = ['is_workFromHome']
    
    @transaction.atomic
    def save(self):
      
        user.is_workFromHome = True
        user.save()
        return user





class AdminDayForm(forms.ModelForm):
    class Meta:
        model = DailyActivites
        fields = ['is_adminDay']
    
    @transaction.atomic
    def save(self):
        
        user.is_adminDay = True
        user.save()
        return user