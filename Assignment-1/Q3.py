#Given code 
# def save_error(error,errors=[]):
#     errors.append(error)
#     return errors
#in  this code same list object is reused across calls
#In th below code arrors=None is evaluted Safely at each call

def save_error(error,errors=None):
    if errors is None:
        errors=[]
    errors.append(error)
    return errors
print(save_error("E1"))
print(save_error("E2"))
print(save_error("E3"))
print(save_error("E4"))
print(save_error("E5"))
print(save_error("E6"))
print(save_error("E7"))