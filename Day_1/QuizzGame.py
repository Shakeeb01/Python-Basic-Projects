Name = input("Enter Your Name : ")
print(f"{Name} welcome to the Game.")
# Question that will asked by User.
Questions = [
    "What is the Capital of Pakistan ? [ karachi,islamabad,Lahore,Sialkot ] ",
    "What is Name of the Captain of Pakistan Cricket Team ? [ babar azam,Muhmmad Rizwan,shadab Khan,shaheen Afridi ] ",
    "Who is the Current Prime Minister of Pakistan is ? [ imran khan,nawaz shareef,bilawal bhutto,shabaz shareef ] ",
    "How many Provinces are in Pakistan ? [5,3,7,4] ",
    "What is the name of Pakistan's Biggest City ? [ islamabad,karachi,Lahore,Sialkot ]",
]
#Answers of all the above questions.
Answers = [
    "islamabad",
    "babar azam",
    "shabaz shareef",
    "4",
    "karachi",
]
    
CorrectAnswers = 0
WrongAnswers = 0
for Question in Questions:
    # first Question.
    if(Question == Questions[0]):
        Question_1 = input(Questions[0])
        if(Question_1 == Answers[0]):
            
            print("Correct")
            CorrectAnswers += 1
        else:
            print("Wrong")   
            WrongAnswers += 1
    # Second Question.         
    elif(Question == Questions[1]):
        Question_2 = input(Questions[1])
        if(Question_2 == Answers[1]):
            
            print("Correct")
            CorrectAnswers += 1
        else:
            print("Wrong")
            WrongAnswers += 1
            
    # Third Question        
    elif(Question == Questions[2]):
        Question_3 = input(Questions[2])
        if(Question_3 == Answers[2]):
            
            print("Correct")
            CorrectAnswers +=1
        else:
            print("Wrong")
            WrongAnswers +=1
            
    # Fourth Question
    elif(Question == Questions[3]):
        Question_4 = input(Questions[3])
        if(Question_4 == Answers[3]):
            
            print("Correct")
            CorrectAnswers +=1
        else:
            print("Wrong")  
            WrongAnswers +=1
    
            
    # Fifth Question
    elif(Question == Questions[4]):
        Question_5 = input(Questions[4])
        if(Question_5 == Answers[4]):
            
            print("Correct")
            CorrectAnswers +=1
        else:
            print("Wrong")            
            WrongAnswers +=1    

# these two lines will display the count of correct and wrong aswers at the end.          
print("Correct Answer : ",CorrectAnswers)            
print("Wrong Answer : ",WrongAnswers)            
            