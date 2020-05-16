import threading
import questions as q
from time import sleep

# All teams at 12

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.score = 0
        
    def add_pts(self, pts):
        self.score += pts
        
    def get_score(self):
        return self.score
    
    def steal(self):
        self.score += 1

def r1_countdown():
    global my_timer
    
    my_timer = 120
    for x in range(120):
        my_timer = my_timer - 1
        sleep(1)
        
    print('Out of time')
    my_timer = 120
    
class R1_Question:
    def __init__(self, h1:str, h2:str, h3:str, h4:str, answer:str):
        self.state = 1
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.hints = [h1, h2, h3, h4]
        self.answer = answer
        self.time_limit = 120 # 120 seconds
    
    def cont(self):
        self.state += 1
        
    def start(self):
        countdown_thread = threading.Thread(target = r1_countdown)
        countdown_thread.start()
        while my_timer > 0:
            print(self.hints[0:self.state])
            cont = input()
            if cont == '':
                self.cont()
            if cont == ' ':
                break
        print('DONE')

example_r1_grid = ['strawberry', 'bell pepper', 'apple', 'pear']
r1_qs = [r1q0, r1q1, r1q2, r1q3, r1q4, r1q5]

class R1_Grid:
    def __init__(self, qs):
        self.questions = qs
        
    def start_question(self, num):
        self.questions[num].start()

#######################################################################################################################

def r2_countdown():
    global my_timer2
    
    my_timer2 = 120
    for x in range(120):
        my_timer2 = my_timer2 - 1
        sleep(1)
        
    print('Out of time')
    my_timer2 = 120

class R2_Question:
	def __init__(self, h1:str, h2:str, h3:str, h4:str, answer:str):
		self.state = 1
		self.h1 = h1
		self.h2 = h2
		self.h3 = h3
		self.h4 = h4
		self.hints = [h1, h2, h3]
		self.answer = answer

	def cont(self):
		self.state += 1

	def start(self):
		countdown_thread = threading.Thread(target = r2_countdown)
		countdown_thread.start()
		while my_timer2 > 0:
			print(self.hints[0:self.state])
			cont = input()
			if cont == '':
				self.cont()
			if cont == ' ':
				break
			if cont == 'h4':
				print(self.h4)
		print('DONE')

example_r2_grid = ['Elementary', 'Middle', 'High', 'College']
r2qs = [r2q0, r2q1, r2q2, r2q3, r2q4, r2q5]

class R2_Grid:
	def __init__(self, qs):
		self.questions = qs

	def start_question(self, num):
		self.questions[num].start()

#######################################################################################################################