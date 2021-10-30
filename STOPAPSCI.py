from random import choice #importing random.choice function
GAME = ['STONE','PAPER','SCISSOR'] #only possible choices

p1_score,p2_score,tie = 0,0,0 #declaring scores of P1,P2 and Tie

p1_total=[] #list of total no of games won by P1
p2_total=[] #list of total no of games won by P2
tie_total=[] #list of total no of ties

for k in range (50):
    p1_score,p2_score,tie = 0,0,0 #start with Zero again
    
    for i in range (0,100,1):

        P1_CHO = choice(GAME) #P1's Choice
        P2_CHO = choice(GAME) #P2's Choice

        #to update score of P1 and P2
        if P1_CHO==P2_CHO:
            tie+=1 #IF tie

        if P1_CHO=='STONE' and P2_CHO !='STONE':
            if P2_CHO=='PAPER':
                p2_score+=1 
            else:
                p1_score+=1
                
        if P1_CHO=='PAPER' and P2_CHO !='PAPER':
            if P2_CHO=='SCISSOR':
                p2_score+=1
            else:
                p1_score+=1
                
        if P1_CHO=='SCISSOR' and P2_CHO !='SCISSOR':
            if P2_CHO=='STONE':
                p2_score+=1
            else:
                p1_score+=1
                
    #addig total no of wins and ties, in total no of game played
    p1_total.append(p1_score) 
    p2_total.append(p2_score)
    tie_total.append(tie)  
        
    print(f" P1 won {p1_score} times, P2 won {p2_score} times and Tied {tie} times.")

sump1=0 #summation of wins of P1
sump2=0 #summation of wins of P2
sumtie=0 #summation of Ties

for a in p1_total:
    sump1+=a
    
for b in p2_total:
    sump2+=b
    
for c in tie_total:
    sumtie+=c
    
p1_avg=sump1/len(p1_total) #Avg games P1 Won
p2_avg=sump2/len(p2_total) #Avg games P2 Won
tie_avg=sumtie/len(tie_total) #Avg Ties

print(f"\nP1's average is {p1_avg} and, P2's avg {p2_avg} and Tie average is {tie_avg}.")

