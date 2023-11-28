#This is a dictionary database to add, delete and store information about students


database={} #the dictionary database



def validator(age, grade): #validates age and grade datas by checking whether they are a number or not
    try:
        int(age)
        int(grade) #checking if the age and grade entered are numbers (name can be a number)

        return 'valid'
        
    except:
        return 'invalid'







def adder(name, age, grade): #adds a student to the database
    if name not in database:

        validation = validator(age, grade)

        if validation == "valid":
            database[name] = {'age':age, 'grade':grade}

            return {"msg":"Successfully registered!","status":"finish"} #msg is the message from the function while the status "finish" will make the loop break to finish the task of adding a student
        else:

             return {"msg":"Check the validity of your input and try again.('Press enter without any input to exit this mode')","status":"retry"}


    else:
        return {"msg":"This name already exists in the database, use a more specific name. ('Press enter without any input to exit this mode')","status":"retry"} #msg is the message from the function while the status "retry" will make the loop continue to try adding the student again




def viewer(name, mode='single'): #responds with a list of students on 'all' mode or just a single student in 'single' mode
    if mode == 'single':
        if name in database:
            return {"msg":f"Name: {name}\nAge: {database[name]['age']}\nGrade: {database[name]['grade']}","status":"finish"}

        else:
            return {"msg":"Student not found, try again! (Press enter to quit this mode)","status":"retry"}

    else:
        if database == {}:
            return "There are no students in the database."
        else:
            all_students = ""

            for i in database:
                all_students += f"Name: {i}\n"
                all_students += f"Age: {database[i]['age']}\n"
                all_students += f"Grade: {database[i]['grade']}\n"
                all_students += '\n\n'

            return all_students





def editor(name, age, grade): #edits student's info
    if name in database:
        validation = validator(age, grade)

        if validation == "valid":
            database[name]['age'] = age
            database[name]['grade']= grade

            return {"msg":"Student's info updated successfully!","status":"finish"}
        else:
            return {"msg":"Check the validity of you input and try again. ('Press enter without any input to exit this mode')","status":"retry"}
    
    else:
        return {"msg":"Name not found ('Press enter without any input to exit this mode')","status":"retry"}



def deleter(name): #deletes a student from the database
    if name in database:
        database.pop(name)

        return {"msg":"Student successfully deleted from the database.","status":"finish"}

    else:
        return {"msg":"Name not found ('Press enter without any input to exit this mode')","status":"retry"}






while(True):
    task = input("""
    Enter:
    1-To add a student
    2-To view a student
    3-To list all students
    4-To update a student's info
    5-To delete a student
    6-Quit

    """)



    if task == "1": #adding a student
        while(True):
            name = input("Name: ")

            if name == "":
                break #breaks the loop when the person presses enter without typing a name

            age = input("Age: ")

            if age == "":
                break

            grade = input("Grade: ")

            if grade == "":
                break

            response = adder(name, age, grade) #the response from adder function (what it returned)

            print('\n'+response['msg']+'\n')

            if response['status'] == 'finish':
                break



    elif task == "2": #reading a student from the database
        while(True):
            name = input("Name:")

            if name == "":
                break

            response = viewer(name)

            print('\n'+response['msg']+'\n')

            if response['status'] == 'finish':
                break

    elif task == "3": #listing all students in the database
        response = viewer('', 'all')

        print('\n'+response+'\n')

    elif task == "4": #to update a student's info
        while(True):
            name = input("Name: ")

            if name == "":
                break

            age = input("New age: ")

            if age == "":
                break

            grade = input("New grade: ")

            if grade == "":
                break

            response = editor(name, age, grade)

            print('\n'+response['msg']+'\n')

            if response['status'] == 'finish':
                break

    elif task == "5": #delete a student
        while(True):
            name = input("Name: ")

            if name == "":
                break

            response = deleter(name)

            print('\n'+response['msg']+'\n')

            if response['status'] == 'finish':
                break

    elif task == "6": #quit
        break