import rps_test as rps
#how to test this game

#first generate a series of R(rocck) P(paper) S(scissor) command
#here we use the bulit in generator(acutually it is a function) to generate randomly
command=rps.gen(50000)

#second, let the game start and record the data

#win and lose:
#win and lose are determinant of how much bonus or penetration 
# would be executed on the AI each time it wins or loses
win=1
lose=1

#energy bar:
#the reason I made this stupid game is that I was wondering
#do humanbeings follow any pattern while playing this game quickly
#in order to apply genetic algorithm in the future, I chose to 
#use an energy bar to limit how many time an implementation could play
#if it wins, it would get some 'food', that is more energy to play more round
#the implementation that survives the most round with same give nenergy bar
#would be chosen to generate new implementations.
energy=20000

#recording data:
data=rps.playgame(win,lose,command,energy)

print data
