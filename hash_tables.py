voted = {}

def check_vote(voter):
    if voted.get(voter):
        print("Kick them out, they have already voted")
        voted_status = True
    else:
        voted[voter] = True
        print("Let them vote")
        voted_status = False
    return voted_status

voted_status = False
while voted_status != True:
    name = input("What is your name ")
    voted_status = check_vote(name)
    print(voted_status)
        
