# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221439 # Date: 12/12/2022


#Part 4 of CW

#variable to check loop
check=" "
#dictionary of program
my_dictionary={}

#to check the program range and validate it  
def check_prog(credit,prompt):
    while True:
        try:
            credit=int(input(prompt))
            if credit%20!=0 or credit>120:
                print("Out of range")
                continue
        except ValueError:
            print("Integer required")
            continue
        return credit


         
#to find the exact progression outcome validation and assigning keys,values to the  dictionary
def prog_outcome():

    student_id=input("Enter student id :")  
    
    Pass=check_prog("Pass","enter the number of credits passed :")
    defer=check_prog("Defer","enter the number of credits deffered :")
    fail=check_prog("Fail","enter the number of credits failed :")
    #check_prog called here to access more inputs and check

    if Pass+defer+fail==120 :
                        
        if Pass==120:
            print("Progress")
            outcome="Progress"
            my_dictionary[student_id]= outcome +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
            
       
            
        elif Pass==100:
            print("Progress(module trailer)")
            outcome="module trailer"
            my_dictionary[student_id]= outcome +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
           
             
        elif fail==100 or fail==120 or fail==80:
            print("Exclude")
            outcome="Exclude"
            my_dictionary[student_id]= outcome +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
          
            
        else:
            print("Module retreiver ")
            outcome="retreiver"
            my_dictionary[student_id]= outcome +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
            
    else:
        print("Total incorrect")


#loop of the function for multiple outcomes

def prog_loop():
    global check
    
    while True:

        #prog_outcome called here to check which outcome and use it to loop
        
        prog_outcome()
        print('.'*70)
        print("Would you like to enter another set of data?")
        check=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        print('.'*70)
        if check=='y':
            continue
        elif check=='q':
            for k,v in my_dictionary.items():
                print(k+":"+v)
            break
        elif check!='y' or 'q':
            print("Invalid input please try again")

#calling the final function to run main program
prog_loop()
        


       
