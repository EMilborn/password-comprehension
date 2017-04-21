# def isPassword(pw):
#     uppers = [i for i in pw if i.isupper()]
#     lowers = [i for i in pw if i.islower()]
#     numbers = [i for i in pw if i.isdigit()]
#     return bool(len(uppers) and len(lowers) and len(numbers))

def isPassword(pw):
    return scorePassword(pw) > 0

#print isPassword('AB1cc1')
#print isPassword('AbCd')
#print isPassword('AA1B2')

def scorePassword(pw):
    uppers = [i for i in pw if i.isupper()]
    lowers = [i for i in pw if i.islower()]
    numbers = [i for i in pw if i.isdigit()]
    if not (len(uppers) and len(lowers) and len(numbers)):
        return 0
    nonalpha = [i for i in pw if not i.isalnum()]
    score = len(pw) / 4
    score += min(len(uppers), len(lowers))  # mixture is important man
    score += len(numbers) / 2  # numbers are less secure or something
    score += len(nonalpha)  # nonalpha masterrace
    return min(score, 10)

print scorePassword('SpOO00OkYsEcUR1tY!!')
print scorePassword('aB1')
print scorePassword('thegreatestpasswordofalltimeWOWEE')
print scorePassword('1(o_O)/')
print scorePassword('mixuppercaseandlowercasE1')