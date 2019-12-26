li4=[15,354,84,241,56,7,152,478]

def filterTest(li4):
    z=lambda x:x <=200 and x%2 ==0
    f=filter(z,li4)
    return list(f)
print(filterTest(li4))

try:
    assert filterTest(li4)==[84,56,152]
except:
    print("not equal")