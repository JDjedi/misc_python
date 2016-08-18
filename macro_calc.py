def mc_def(base):
	new_Base = base - (base * .25)
	protien = new_Base * .3
	fat = new_Base * .2
	carbs = new_Base * .5
	total_calc = protien + fat + carbs

	print "You should be consuming %d calories worth of carbs" % carbs
	print "You should be consuming %d calories worth of protien" % protien
	print "You should be consuming %d calories worth of fat" % fat
	print "Total caloric conusumption should be: %d" % total_calc

mc_def(3500)