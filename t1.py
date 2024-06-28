inputs=[1,0,1,0,1]
weights=[0.7,0,0.5,0,0.4]
threshold = 1.5
multiple_list= []
for i in range(0,len(inputs)):
    multiple_list.append(inputs[i]*weights[i])
    Sum = sum(multiple_list)
    

if  Sum> threshold:
    print("Mirim concert")
else :
    print("Nemirim concert")
