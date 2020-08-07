import random
print('WELCOME!!! Play Hand Cricket with your rival-->COMPUTER')
print('RULES ARE:')
print('1: You can use only 1,2,3,4,5,6 while batting and bowling')
print('2: When your number and your rivals number comes same then the one who is batting will be declared out')
print('3: Batting and Bowling will be decided as per the TOSS')
print('NOW LETS ROLL THE COIN')
toss=['HEADS','TAILS','Heads','Tails','heads','tails']
ur_scr=0
rvl_scr=0
rvl_show=[1,2,3,4,5,6]
call=str(input('WHATS YOUR CALL, HEADS OR TAILS?:'))
if(call==random.choice(toss)):
    print('KUDOS!!! You won the toss')
    elect=str(input('What you wanted to elect:'))
    # USER BATTING STATS
    if(elect=='BAT' or elect=='Bat' or elect=='bat'):
        for i in range(1,40):
            n = int(input('Bat by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                ur_scr += n
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('You are OUT, and your score is'+'\t' + str(ur_scr) + 'runs')
                break
        print('Now its time for rival to chase the score,lets see what the result is going to be')
        # USER BOWLING STATS
        for i in range(1,40):
            n = int(input('Bowl by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if(n>6):
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                rvl_scr += nr
                if(rvl_scr==ur_scr and n==nr):
                    print('MATCH DRAWN')
                    break
                elif(rvl_scr>ur_scr):
                    print('RIVAL won the match by'+'\t'+str(rvl_scr-ur_scr)+'runs')
                    break
                else:
                    print('********NO CHEATING*********')
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('Rival is OUT, and its score is'+'\t' + str(rvl_scr) + 'runs')
                break
    # USER BOWLING STATS
    elif(elect=='BOWL' or elect=='Bowl' or elect=='bowl'):
        for i in range(1,40):
            n = int(input('Bowl by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                rvl_scr += nr
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('Rival is OUT, and its score is'+'\t' + str(rvl_scr) + 'runs')
                break
        print('Now its time for you to chase the score,lets see what the result is going to be')
        # USER BATTING STATS
        for i in range(1,40):
            n = int(input('Bat by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                ur_scr += n
                if (rvl_scr == ur_scr and n == nr) :
                    print('MATCH DRAWN')
                    break
                elif (ur_scr > rvl_scr) :
                    print('YOU won the match by' + '\t' + str(ur_scr-rvl_scr) + 'runs')
                    break
                else :
                    print('YOUR score is:',ur_scr)
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('You are OUT, and your score is'+'\t' + str(ur_scr) + 'runs')
                break
else:
    rvl_el=random.choice(['BAT','BOWL'])
    # RIVAL BATTING STATS
    print('OOPS!!! Rival won the toss and decided to',rvl_el)
    if(rvl_el=='BAT'):
        for i in range(1,40):
            n = int(input('Bowl by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                rvl_scr += nr
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('Rival is OUT, and its score is'+'\t' + str(rvl_scr) + 'runs')
                break
        print('Now its time for you to chase the score,lets see what the result is going to be')
        # RIVAL BOWLING STATS
        for i in range(1,40):
            n = int(input('Bat by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                ur_scr += n
                if (rvl_scr == ur_scr and n == nr) :
                    print('MATCH DRAWN')
                    break
                elif (ur_scr > rvl_scr) :
                    print('YOU won the match by' + '\t' + str(ur_scr-rvl_scr) + 'runs')
                    break
                else :
                    print('YOUR score is:',ur_scr)
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('You are OUT, and your score is'+'\t' + str(ur_scr) + 'runs')
                break
    # RIVAL BOWLING STATS
    elif(rvl_el=='BOWL'):
        for i in range(1,40):
            n = int(input('Bat by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                ur_scr += n
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('You are OUT, and your score is'+'\t' + str(ur_scr) + 'runs')
                break
        print('Now its time for rival to chase the score,lets see what the result is going to be')
        # RIVAL BATTING STATS
        for i in range(1,40):
            n = int(input('Bowl by entering numbers given in rule:'))
            nr = random.choice(rvl_show)
            if (n > 6) :
                print('**********NO CHEATING,ABIDE BY THE RULES**********')
            if (n != nr):
                print('Your number is:', n)
                print('Rival number is:', nr)
                rvl_scr += nr
                if (rvl_scr == ur_scr and n == nr) :
                    print('MATCH DRAWN')
                    break
                elif (rvl_scr > ur_scr) :
                    print('RIVAL won the match by' + '\t' + str(rvl_scr - ur_scr) + 'runs')
                    break
                else :
                    print('RIVAL score is:', rvl_scr)
            else:
                print('Your number is:', n)
                print('Rival number is:', nr)
                print('Rival is OUT, and its score is' + str(rvl_scr) + 'runs')
                break
# FINAL SCORES
print('YOUR SCORE:',ur_scr)
print('RIVAL SCORE:',rvl_scr)
# RESULTS
if(rvl_scr>ur_scr):
    print('SORRY!!! Better Luck Next Time')
    print('RIVAL won the match by'+'\t'+str(rvl_scr-ur_scr)+'runs')
else:
    print('HURRAYYYY!!! YOU ARE A CHAMP')
    print('YOU won the match by'+'\t' + str(ur_scr-rvl_scr) + 'runs')
print('THANKS FOR ENTERTAINING YOURSELF!!!')