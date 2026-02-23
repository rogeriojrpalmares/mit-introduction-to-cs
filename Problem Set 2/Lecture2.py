'''concatenate strings'''
'''
a = "tes"
b = "t"
c = "do Rogerio"
silly = a * 3
print (a+b + " "+c)
print (silly)

b = ":"
c = ")"
print (b+2*c)

f = "a"
g = " b"
h = "3"
s2 = (f+g)*int(h)
print (s2)

s ="abc"
len(s)
chars = len(s)
print (chars)

#indexing which starts from zero

s ="abc"
print (s[-1])
print (s[0])
print (s[2])
# index out of range error ==> print (s[3])
print (len(s)-1)
#slicing to get substrings
#s = "abcdefg"
#print (s[3:6:2])
#print (s[:])
#print (s[::-1])
#print (s[4:1:-2])

#s= "ABC d3f ghi"
#print(s[3:len(s)-1])
#print (s[3::-1])
#empty string below
#print (s[6:3])

a = "the"
b = 3
c = "musketeers"
print (a, b, c)
#print (a + b + c)
print (a + str(b) + c)

#text = input("Type something: ")
#print (5*text)

#num1 = input ("Type a number: ")
#print (5*num1)

#num2 = int(input("Type a number"))
#print (num2*2)
verb = input("Type a verb: ")
print ("I can",verb,"better than you")
#F strings
print (f'I can {verb} better than you')
print ((verb + " ")*4 +verb)
'''
#Conditions for branching
secret = 20
guess = int(input("Guess a number: "))
if guess < secret:
	print ("Too low")
elif guess > secret:
	print ("Too high")
else:
	print ("Same as secret")
