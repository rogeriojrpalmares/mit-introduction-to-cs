def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	cost_of_down_payment = cost_of_dream_home * portion_down_payment
	print (cost_of_down_payment)
	
	monthly_salary = yearly_salary / 12
	amount_saved = 0
	months = 0
	r = 0.05
	
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < cost_of_down_payment:
		amount_saved += (amount_saved * r/12)
		amount_saved = amount_saved + (portion_saved * monthly_salary)
		months+=1
	print (f'Number of months: {months}')
	
	return months