#Elizabeth Tchako
#07/05/24
#Understanding lists

bicycles  = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)# print ['trek', 'cannondale', 'redline', 'specialized']

#lists are ordered collection, you can access any element in a list by telling Python the positon or INDEX
#to access an element in a list, write the name of the list followed by the index of the item in enclosed square brackets
#Index positon start at 0 NOT 1
print(bicycles[0])#print = trek

#You can use methods on lists that you would impose on strings
print(bicycles[0].title()) # print = Trek
print(bicycles[0].upper())#print = TREK

#Lets ask for  at index 1 and 
print(bicycles[1])
print(bicycles[3])

#if you ever want to just return the last item in a list ask for item at index[1]
#helpful because mayeb you want to access without knowing the last item 
print(bicycles[-1])

#extends to other index [-2] return second to last [-3] third to last 

#you can use individual valus from a list just as you would any oter variable 
#^meaning do the same manipluation to both

message = f'My first bicycle was a {bicycles[0].title()}'
print(message)# print My first bicycle was a Trek