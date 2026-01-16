import sys
if len(sys.argv)<2:
    print("argument error")
    miles=11
    kilometers=miles*1.6
else:
 miles=int(sys.argv[1])
 kilometers=miles*1.6
 print("miles=",miles)
 print("kilometers=",kilometers)
