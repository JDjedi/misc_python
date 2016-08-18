name = 'Jonathan C. Diaz'
age = 26
height = 72.0 # inches
weight = 242.0 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats a bit heavy..."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky

print "If i add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight) # Last one is its own unit, notice the commas

lbs_to_kilos = weight * .45
inches_to_centimeters = height * 2.54

print "If your height is %d inches then in centimeters it is %d." % (height, inches_to_centimeters)
print "If your weight is %d lbs then in kilos it is %d." % (weight, lbs_to_kilos)