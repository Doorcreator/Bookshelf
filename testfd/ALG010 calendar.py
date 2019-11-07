class Calendar():
	def __init__(self):
		pass
	def leap_year(self,year): # year format: 'YYYY'
		if year%4 == 0:
			flag = 1
		else:
			flag = 0
		return flag
	def past_and_left_days(self,date): # date format: 'YYYY/MM/DD'
		pure_year = date.split('/')
		if self.leap_year(int(pure_year[0]))==1:
			year_days = [31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			year_days = [31,28,31,30,31,30,31,31,30,31,30,31]
		month_days = sum(year_days[:int(pure_year[1])-1])
		direct_days = int(pure_year[2])
		past_days = month_days + direct_days
		left_days = sum(year_days) - month_days - direct_days
		return past_days,left_days
	def day_interval(self,date1,date2): # date format: 'YYYY/MM/DD'
		y1 = int(date1.split('/')[0])
		y2 = int(date2.split('/')[0])
		if y2-y1==0:
			d1 = self.past_and_left_days(date1)[0]
			d2 = self.past_and_left_days(date2)[0]
			total_day = d2 - d1
		elif y2-y1>0:
			total_day = 0
			for y in range(y1+1,y2):
				if self.leap_year(y)==1:
					total_day += 366
				else:
					total_day += 365
			total_day += self.past_and_left_days(date1)[1] + self.past_and_left_days(date2)[0]
		else:
			total_day = self.day_interval(date2,date1)*-1
		return total_day
	def week_day(self,date): # date format: 'YYYY/MM/DD'
		norm_date = '2019/08/01' # Thu
		weekday_dic = {-1:'Wed',-2:'Tue',-3:'Mon',-4:'Sun',-5:'Sat',-6:'Fri',0:'Thu',1:'Fri',2:'Sat',3:'Sun',4:'Mon',5:'Tue',6:'Wed'}
		diff_days = self.day_interval(norm_date,date)
		diff_wkdays = diff_days%7
		weekday = weekday_dic[diff_wkdays]
		return weekday
	def raw_calendar(self,m_date): # m_date format: 'YYYY/MM'
		calendar_wkdays = {'Mon':[],'Tue':[],'Wed':[],'Thu':[],'Fri':[],'Sat':[],'Sun':[]}
		year_month = m_date.split('/')
		if self.leap_year(int(year_month[0]))==1:
			year_days = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
		else:
			year_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
		for day in range(1,year_days[int(year_month[1])]+1):
			wdpair = self.week_day(m_date+'/'+str(day))
			calendar_wkdays[wdpair].append(day)
		calendar_wkdays = sorted(calendar_wkdays.items(), key = lambda x:x[1])
		return calendar_wkdays
	def pretty_calendar(self,m_date): # m_date format: 'YYYY/MM'
	# valid period: 1900/03-2099/12
		calendar_array = self.raw_calendar(m_date)
		dic = {}
		for arr in calendar_array:
			n = len(arr[1])
			for column in range(-1,n):
				dic.setdefault(column,[])
				if column==-1:
					dic[column].append(arr[0])
				else:
					dic[column].append(arr[1][column])
		print('Calendar: %s'%m_date)
		for i in dic.items():
			k = ''
			for j in i[1]:
				k += str(j) + '\t'
			print(k)
# r = Calendar().pretty_calendar('2019/08')






