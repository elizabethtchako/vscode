#Elizabeth Tchako
# 07/09/24
# learnign about how you can loop through a loist to apply spefic actions to its values 



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#looping is important b ecause it automates a computers task
    

#for magician in magicians: tell  Python to retrive the first value from the list of magicians and associate it with the variable name magician
#print(magician) print the current value of magician while still 'alice'
#because the list contains more values Python returns to the first line of the loop 
#when there are no more valies in the list Python moves on to the next line pf code 
#Remebr you can choose any name you want for the temporary value ( however its meaningful to chose a name tat represent a single item from the list )
#examples (for cat in cats, for dog in dogs, for item in list_of_items)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')# each line in the indent is what is executed for eac value in the list 
    #you can do as much work as you would like with each value in the list 
    print(f"I can't wait for your next trick, {magician.title()}.\n")
    #only lines that are indented will be executed for each value in the line of the loop

#this is not indented so will print after the loop is done running 
print("Thank you, everyone. That was a great magic show") # this is not in the loop but its good practice to summarize an operation that was performed 


#python uses indentation to make code esaier to read, there are common indentation errors 
magicians = ['alice', 'david', 'carolina']
#for i in magicians:
#print(i) # if you fprget rto indent python will remind you 
# sometimes your loop will run but you didnt indent for the line you want to run for you values in the lisy, this will give you imporpoer output 
# this is a logic error 
    # if you unneccessarly indent python will also inform you of that error 
# if you you forget to unindent then everythign will repeat again in the code for the line tat was jsut deigned for the summary 
# at the end of for loop ststaments dont foget te semicolon 



