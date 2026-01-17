#function declaration
def count_message(msg, count):
    #function defination
    #Accepts a msg and uses a defaultparameter count an incremnta it by 1 
    count += 1
    print(f"Message: {msg}, Count: {count}")
    return count
count=0
#funtion call
count=count_message("heya",count)