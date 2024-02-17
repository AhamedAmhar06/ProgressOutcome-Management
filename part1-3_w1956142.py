# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221439 # Date: 12/12/2022

#Part 1 to Part 3 of CW 


#lists of outcomes
prog_list=[]  
trailer_list=[]
exclude_list=[]
retriever_list=[]

#counts of outcomes
prog_count=0
trailer_count=0
exclude_count=0
retriever_count=0
#varaible to check loop
check=" "
#open a textfile
file = open("textfile.txt", "w")


#to check the program range and validate it
def check_prog(credit,prompt):
    while True:
        try:
            credit=int(input(prompt))
            if credit%20!=0 or credit>120:
                print("out of range")
                continue
        except ValueError:
            print("integer required")
            continue
        return credit
             
#to find the exact progression outcome validation


    
def prog_outcome():
    global prog_count,trailer_count,exclude_count,retriever_count
    global prog_list,trailer_list,exclude_list,retiever_list

 
    #check_prog function called t
    Pass=check_prog("Pass","enter the number of credits passed :")
    defer=check_prog("Defer","enter the number of credits deffered :")
    fail=check_prog("Fail","enter the number of credits failed :")

    if Pass+defer+fail==120 :
                        
        if Pass==120:
            print("Progress")
            prog_list.append(Pass)
            prog_list.append(defer)
            prog_list.append(fail)
            prog_count+=1
            
        elif Pass==100:
            print("Progress(module trailer)")
            trailer_list.append(Pass)
            trailer_list.append(defer)
            trailer_list.append(fail)
            trailer_count+=1
             
        elif fail==100 or fail==120 or fail==80:
            print("Exclude")
            exclude_list.append(Pass)
            exclude_list.append(defer)
            exclude_list.append(fail)
            exclude_count+=1
            
        else:
            print("Module retreiver ")
            retriever_list.append(Pass)
            retriever_list.append(defer)
            retriever_list.append(fail)
            retriever_count+=1
    else:
        print("Total incorrect")


#to ask the user for more inputs till exit option is selected in loop 
def prog_loop():
    global check
    
    while True:

        prog_outcome()  #prog_outcome function called
        print('.'*70)
        print("Would you like to enter another set of data?")
        check=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        print('.'*70)
        if check=='y':
            continue
        elif check=='q':
            break
        elif check!='y' or 'q':
            print("Invalid input please try again")
       
        


#histogram of the outcome after exit option
def prog_histogram():
    
    
    prog_loop()     #prog_loop function called back to output histogram if its exited
    
    if check=='q':
        
        print("Histogram")
        print("Progress   ",prog_count,":", prog_count*"*")
        print("Trailer    ",trailer_count,":", trailer_count*"*")
        print("Retreiever ",retriever_count,":",retriever_count*"*")
        print("Excluded   ",exclude_count,":", exclude_count*"*")
        total=prog_count+trailer_count+retriever_count+exclude_count
        print(total,"Outcomes in Total")
        print('.'*70)

#list version extended of the program
def list_extension():
    global prog_list,trailer_list,exclude_list,retiever_list
    
  

    prog_histogram()        #prog_histogram function called here to output as lists
    
    print("Part 2: ")
                                
    for i in range(0, len(prog_list), 3):
        print('Progress - ' ,prog_list[i],',', prog_list[i+1],',', prog_list[i+2])
    for i in range(0, len(trailer_list), 3):
        print('Progress (module trailer  )-' ,trailer_list[i],',', trailer_list[i+1],',', trailer_list[i+2])
    for i in range(0, len(retriever_list), 3):
        print('Module retriever' ,retriever_list[i],',', retriever_list[i+1],',', retriever_list[i+2])
    for i in range(0, len(exclude_list), 3):
        print('Exclude' ,exclude_list[i],',', exclude_list[i+1],',', exclude_list[i+2])


        
#text file extension of the progress 
def prog_text():
    global prog_list,trailer_list,exclude_list,retiever_list,file
    
    
    list_extension()   #list extenstion function called to use same method to create text file 
    for i in range(0, len(prog_list), 3):
        prog_text=(f"Progress- {prog_list[i]}, {prog_list[i+1]}, {prog_list[i+2]}\n")
        file.write(prog_text)
        
    for i in range(0, len(trailer_list), 3):
        trailer_text=(f"Progress (module trailer  )- {trailer_list[i]}, {trailer_list[i+1]}, {trailer_list[i+2]}\n")
        file.write(str(trailer_text))
        
    for i in range(0, len(retriever_list), 3):
        retriever_text=(f"Module retriever- {retriever_list[i]},{retriever_list[i+1]},{retriever_list[i+2]}\n")
        file.write(str(retriever_text))
        
    for i in range(0, len(exclude_list), 3):
        exclude_text=(f"Exclude- {exclude_list[i]}, {exclude_list[i+1]}, {exclude_list[i+2]}\n")
        file.write(str(exclude_text))
        
    file.close()

    file=open("textfile.txt", "r")
    display=file.read()
    print('.'*70)
    print("part 3")
    print(display)
    file.close()



#calling the final function as whole connected program
prog_text()



      
        
