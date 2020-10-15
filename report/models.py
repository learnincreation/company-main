from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.

class DirectHR(models.Model):
 
	user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
	message = models.TextField()
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.username


class LeaveHR(models.Model):
	is_approved = models.BooleanField(default = False)
	user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
	reason = models.TextField()
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.username
# Create your models here.


MEETING_PLACE = [
			('DR CLINIC', "DR CLINIC"),
			('HOSPITAL', "HOSPITAL"),
			('RESIDENCE HOME ADDRESS', "RESIDENCE HOME ADDRESS"),
	]


CURRENT_PRESCRIBING_BRAND = [
			('CITOSYN-P', "CITOSYN-P"),
			('CITOSYN 2 ML', "CITOSYN 2 ML"),
			('CEFATRICS – S', "CEFATRICS – S"),
			('ESCITRICS PLUS', "ESCITRICS PLUS"),
			('LEVESYN', "LEVESYN"),
			('MEROTRICS 1 GM', "MEROTRICS 1 GM"),
			('NORISS', "NORISS"),
			('OLATRICS – 10 MG', "OLATRICS – 10 MG"),
			('OLATRICS – 2.5 MG', "OLATRICS – 2.5 MG"),
			('OLATRICS – 5 MG', "OLATRICS – 5 MG"),
			('PODOSYN – CV', "PODOSYN – CV"),
			('REVITRICS', "REVITRICS"),
			('SYNAC MR', "SYNAC MR"),
			('SYNAXONE INJ', "SYNAXONE INJ"),
			('SYNAZID TZ', "SYNAZID TZ"),
			('SYNAZOLE- R', "SYNAZOLE- R"),
			('SYNAZOLE DSR', "SYNAZOLE DSR"),
			('SYNERVE M', "SYNERVE M"),
			('VALSYN CR 300', "VALSYN CR 300"),
			('VALSYN CR 200', "VALSYN CR 200"),
			('VALSYN CR 500', "VALSYN CR 500"),
	]


SPECIALITY = [
			('NEUROLOGIST', "NEUROLOGIST"),
			('NEUROSURGEON', "NEUROSURGEON"),
			('PSYCHIATRIST', "PSYCHIATRIST"),
			('PHYSICIAN', "PHYSICIAN"),
			('GENRAL PHYSICIAN', "GENRAL PHYSICIAN"),
			('GYNAECOLOGIST', "GYNAECOLOGIST"),
			('SURGEON', "SURGEON"),
			('ORTHOLOGIST', "ORTHOLOGIST"),

	]


PLACES = [
			('HALDWANI', "HALDWANI"),
			('DEHRADUN', "DEHRADUN"),
			('MEERUT', "MEERUT"),
			('GAZIABAD', "GAZIABAD"),
			('KANPUR', "KANPUR"),
			('VARANAMSI', "VARANAMSI"),
			('JAMMU 1', "JAMMU 1"),
			('JAMMU 2', "JAMMU 2"),
			('AGRA', "AGRA"),
			('ALIGARH', "ALIGARH"),
			('GWALIOR', "GWALIOR"),
			('SHAHJANPUR', "SHAHJANPUR"),
			('BARIELLY', "BARIELLY"),
	]

MONTHS = [
			('JANUARY', "JANUARY"),
			('FEBURARY', "FEBURARY"),
			('MARCH', "MARCH"),
			('APRIL', "APRIL"),
			('MAY', "MAY"),
			('JUNE', "JUNE"),
			('JULY', "JULY"),
			('AUGUST', "AUGUST"),
			('SEPTEMBER', "SEPTEMBER"),
			('OCTOBER', "OCTUBER"),
			('NOVEMBER', "NOVEMBER"),
			('DECEMBER', "DECEMBER"),
	]


DAY = [
			('MONDAY', "MONDAY"),
			('TUESDAY', "TUESDAY"),
			('WEDNESDAY', "WEDNESDAY"),
			('THRUSDAY', "THRUSDAY"),
			('FRIDAY', "FRIDAY"),
			('SATURDAY', "SATURDAY"),
			('SUNDAY', "SUNDAY"),
			
	]
Brand_CHOICES = (
        ('Brand1', 'Brand1'),
        ('Brand2', 'Brand2'),
		('Brand3', 'Brand3'),
		('Brand4', 'Brand4'),
		('Brand5', 'Brand5'),
    )



class DrMasterList(models.Model):
	dr_name 		= models.CharField(max_length = 100)
	city 			= models.CharField(max_length = 100)
	dr_speciality	=  models.CharField(max_length = 100, choices = SPECIALITY )
	user 			= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.dr_name + '-' + self.dr_speciality  



class ChemistMasterList(models.Model):
	chemist_name 		= models.CharField(max_length = 100)
	city 			= models.CharField(max_length = 100)
	mobile = models.CharField(max_length = 10)	
	user 			= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.chemist_name

class DailyActivites(models.Model):
	user 	= models.ForeignKey(User, on_delete= models.CASCADE) 
	is_field = models.BooleanField(default = False)
	is_meeting = models.BooleanField(default = False)
	is_workFromHome = models.BooleanField(default = False)
	is_adminDay = models.BooleanField(default = False)
	is_covid19 = models.BooleanField(default = False)
	is_other = models.BooleanField(default = False)
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.username





class DailyDrcallReport(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	dr_name = models.ForeignKey(DrMasterList,on_delete=models.CASCADE)
	dr_speciality = models.CharField(max_length = 100, choices = SPECIALITY)
	meeting_place = models.CharField(max_length = 100, choices = MEETING_PLACE)
	Date_time = models.DateTimeField(auto_now = True)
	prescrebtionBrand = models.CharField(max_length = 100,choices=Brand_CHOICES)
	user_WorkingPlace = models.CharField(max_length = 100)
	current_month_business = models.IntegerField()
	


	def __str__(self):
		return str(self.user.useername) + '-' + str(self.dr_name)  + '-' + str(self.dr_speciality) + '-' + str(self.meeting_place) 


class DailyDrMeetingReport(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	dr_name = models.ForeignKey(DrMasterList,on_delete=models.CASCADE)
	dr_speciality = models.CharField(max_length = 100, choices = SPECIALITY)
	meeting_place = models.CharField(max_length = 100, choices = MEETING_PLACE)
	Date_time = models.DateTimeField(auto_now = True)
	
	


	def __str__(self):
		return str(self.dr_name) + '-' + str(self.dr_speciality) + '-' + str(self.user.username) 


class Others(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField(max_length=200)




"""class MOnthlyplan(model.Model):
	is_approved = models.BooleanField(default = False)
	is_rejected = models.BooleanField(default = False)
	user 	= models.ForeignKey(User, on_delete= models.CASCADE) 
	doctor_name = models.CharField(max_length= 50)
	plan_date = """

""""
class Dr_visit_report(models.Model):
	user 			= models.ForeignKey(User, on_delete= models.CASCADE)
	dr_name 		= models.CharField(max_length = 100)
	city 			= models.CharField(max_length = 100)
	place 			= models.CharField(max_length = 100)
	dr_speciality 	= models.CharField(max_length = 100, choices = SPECIALITY)
	visit_date 		= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.dr_name + '-' + self.dr_speciality + '-' +self.city 

class Expenses (models.Model):
	user 			= models.ForeignKey(User, on_delete= models.CASCADE)
	date = models.DateTimeField(auto_now = True)
	working_place = models.CharField(max_length = 100)
	calls_made = models.IntegerField()
	chemist_meeting = models.IntegerField()
	travelling_from = models.CharField(max_length = 100)
	travelling_to = models.CharField(max_length = 100)
	distance_travelled = models.IntegerField()
	total_appointment = models.IntegerField()
	daily_allowance = models.IntegerField()
	telephone_internet_expenses = models.IntegerField()
	total = models.IntegerField()

	def __str__(self):
		return self.user.username  




class chemist_call_report(models.Model) : 
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	chemist_name = models.CharField(max_length = 100)
	business_outcomes_chemist_visit = models.IntegerField()
	date_of_visit 	=  models.DateTimeField(auto_now = True)


	def __str__(self):
		return self.chemist_name 


class day_summary (models.Model) :
	user 							   = models.ForeignKey(User, on_delete= models.CASCADE)
	total_calls 					   = models.IntegerField()
	business_outcomes_of_total_calls   = models.IntegerField()
	total_chemist_meeting              = models.IntegerField()
	business_outcomes_of_total_metting = models.IntegerField()
	report_submission 				   = models.DateTimeField(auto_now_add = True)
	delayed_submission 				   = models.CharField(max_length = 100 , null=True, blank = True)

	def __str__(self):
		return self.user.username """

"""
class RCPA_details(models.Model):
	user 				= models.ForeignKey(User, on_delete= models.CASCADE)
	date_of_visit 		=  models.DateTimeField(auto_now_add = True)
	brand_name 			= models.CharField(max_length = 100)
	competitor_name1 	= models.CharField(max_length = 100, null=  True, blank = True)
	competitor_name2 	= models.CharField(max_length = 100, null=  True, blank = True)
	competitor_name3 	= models.CharField(max_length = 100,  null=  True, blank = True) 
	competitor_name4 	= models.CharField(max_length = 100,  null=  True, blank = True)
	competitor_name5	= models.CharField(max_length = 100,  null=  True, blank = True)
	competitor_name6	= models.CharField(max_length = 100,  null=  True, blank = True)
	competitor_name7 	= models.CharField(max_length = 100,  null=  True, blank = True)

	def __str__(self):
		return self.brand_name + '-' + self.competitor_name1 


class doctor_visit_report(models.Model):
	user 			=  models.ForeignKey(User, on_delete= models.CASCADE)
	doctor_name 	=  models.CharField(max_length = 100)
	city 			=  models.CharField(max_length = 100)
	dr_speciality 	=  models.CharField(max_length = 100 , choices = SPECIALITY)
	date_of_visit 	=  models.DateTimeField(auto_now_add = True)
	month 			=  models.CharField(max_length = 20,choices = MONTHS)


	def __str__(self):
		return self.doctor_name + '-' + self.dr_speciality + '-' +self.month + '-' +self.city 

class HQ_List(models.Model):
	dr_name 		= models.CharField(max_length = 100, null = True , blank = True)# remove later null and blank
	city 			= models.CharField(max_length = 100 ,null = True , blank = True)# remove later null and blank
	dr_speciality	=  models.CharField(max_length = 100 , choices = SPECIALITY)# remove later null and blank
	date 			= models.DateTimeField(auto_now = True)
	place 			=  models.CharField(max_length = 20,choices = PLACES)
	current_doctor_business   = models.FloatField(max_length = 100 , null = True , blank = True) # remove later null and blank
	current_prescribing_brand = models.CharField(max_length = 400 , choices = CURRENT_PRESCRIBING_BRAND)# remove later null and blank
	brand_name1 = models.CharField(max_length = 400 ,null = True , blank = True)
	brand_name2 = models.CharField(max_length = 400, null = True , blank = True)
	brand_name3 = models.CharField(max_length = 400, null = True , blank = True)
	brand_name4 = models.CharField(max_length = 400 , null = True , blank = True)
	brand_name5 = models.CharField(max_length = 400, null = True , blank = True) 
	user 		= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.dr_name + '-' + self.dr_speciality + '-' +self.place 


class chemistlist(models.Model):
	chemist_name 		= models.CharField(max_length = 100, null = True , blank = True)# remove later null and blank
	contact	=  models.IntegerField( null = True , blank = True)# remove later null and blank
	date 			= models.DateTimeField(auto_now = True)
	place 			=  models.CharField(max_length = 20,choices = PLACES)
	POB_Collection_status   = models.FloatField(max_length = 100 , null = True , blank = True) # remove later null and blank
	ABM_Approach_Status = models.CharField(max_length = 400 , null = True , blank = True)# remove later null and blank
	brand_name1 = models.CharField(max_length = 400 ,null = True , blank = True)
	brand_name2 = models.CharField(max_length = 400, null = True , blank = True)
	brand_name3 = models.CharField(max_length = 400, null = True , blank = True)
	user 		= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.chemist_name + '-' + self.contact + '-' +self.place 


"""