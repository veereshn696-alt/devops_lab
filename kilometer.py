import sys
if len(sys.argv)<2:
    print("argument error ")
else:
    miles=int(sys.argv[1])
kilometers=miles*1.6
print("miles=",miles)
print("kilometers=",kilometers)