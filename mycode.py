
def simple_interest(principal, rate, time):
  return (principal * rate * time) / 100

p = 10000
r = 10
t = 2

interest = simple_interest(p, r, t)
print("Simple Interest: ", interest)

def compound_interest(principal, rate, time): 

 A = principal * (pow((1 + rate / 100), time)) 

 CI= A - principal 

 print("Compound interest is", CI) 


compound_interest(10000,5,2)




