import owiener

e = 3118640089701947493
n = 6560046178098980376
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
    
# Hacked d=4221909016509078