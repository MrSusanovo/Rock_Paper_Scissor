# Rock_Paper_Scissor
#Try to develop a rock paper scissor AI which is good at playing this game with human beings.
#python rpsgame
#python rpscisor.py
import random
upper=3
#store the game data into this class 
class Player(object):
	def __init__(self):
		self.record={"R":0,"P":0,"S":0}
		self.R=0
		self.P=1
		self.S=2
	def playsum(self):
		s=0
		for k,v in self.record.iteritems():
			s+=v
		return s+3
	def renew(self):
		self.R=self.record["R"]
		self.P=1+self.record["P"]
		self.S=2+self.record["S"]
		
#the function that judges if the player would win	
def judge(cmnd,comp):
	if cmnd=="R":
		if comp=="P":
			return -1
		elif comp=="S":
			return 1
		else:
			return 0
	elif cmnd=="P":
		if comp=="P":
			return 0
		elif comp=="S":
			return -1
		else:
			return 1
	elif cmnd=="S":
		if comp=="P":
			return 1
		elif comp=="S":
			return 0
		else:
			return -1
	else:
		return -2
# find the min value from a dictionary
def min_dic(dic,key1):
	min=dic[key1]
	key=key1
	for k,v in dic.iteritems():
		if min>v:
			min=v
			key=k
	return (key,v)
#a dictionary stores the rock paper scissor as key,and the item beat the key as the value
beat={"R":"P","P":"S","S":"R"}
# play function which plays the game
def play(player,cmd):
	#generate a random number from 0 to the sum of record.S record.P record.R
	num=random.randint(0,player.playsum())
	#print "DEBUG: the max is",player.playsum()
	#print "DEBUG: S=",player.S, "P=",player.P,"R=",player.R
	#print"the number chosen is ", num
	if num<=player.R:
		return beat['R']
	elif num<player.R+player.P:
		return beat['P']
	elif num<=player.R+player.P+player.S+3:
		return beat['S']
	else:
		return False

def playgame(win,lose,comd,generation):
	p1=Player()
	command=list(comd)
	command.reverse()
	s=0#initialize the score
	i=generation#energy bar
	count=0#count how many round the game has been played
	while i>0:
		count+=1#count once
		com=command.pop()
		if com=="E":
			break
		elif com=="N":
			#p1=Player()
			continue
		elif com=="H":
			#print "score:",s
			continue
		elif com!="R" and com!="P" and com!="S":
			#print"invalid input"
			continue
		result=play(p1,com)
		p1.record[com]-=1
		p1.record["R"]+=1
		p1.record["S"]+=1
		p1.record["P"]+=1
		#print "The computer chose ",result
		#print "your choice is ", com
		score=judge(com,result)
		if(score==1):
			#print "you win!"
			p1.record[beat[com]]-=lose
			s+=1
		#elif(score==0):
			#print"peace"
		elif(score==-1):
			#print"You lose!"
			p1.record[com]+=win
			s-=1
			i+=1
		p1.renew()
		i-=1
	return  {"Score":s,"Generation":count,"winlose":(win,lose)}
# two constants used for test, 
w_win=1
w_lose=1

# randomly generates the rock papper scissor command string with length of i
def gen(i):
	st=""
	while i>0:
		c=random.randint(0,3)
		if c==0:
			st+="R"
		elif c==1:
			st+="S"
		elif c==2:
			st+="P"
		i-=1
	return st
