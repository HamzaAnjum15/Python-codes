# 
import random
h = "head"
t = "tail"
ask = (input(f"{h} or {t}? "))
def head_tail(ask):
    num = int(input("enter a number between 1 to 6 "))
    rand = random.randint(1, 6)
    print(f"the computer chose {rand}")
    head = "head comes"
    tail = "tail comes"
    if (num+rand) % 2 != 0:
        print(head)
        if ask == head[0]:
            bat = "Bat"
            ball = "Ball"
            print(f"you won the toss! {bat} or {ball}?")
        else:
            print("you lost the toss")
            print("hello")

    else:
        print(tail)
        if ask == tail[0]:
            bat = "Bat"
            ball = "Ball"
            print(f"you won the toss! {bat} or {ball}?")
        else:
            print("you lost the toss")
    bat_first = str("batting")
    ball_first = str("balling")
    decision = input()
    # def bat(decision):
    if decision == bat_first[0:3]:
     print("you chose batting")
     score_run1 = 2
     score_run=0
     rand1=0
     rand2=0
    while rand1 != score_run1:        
      rand1 = random.randint(1, 6)
      score_run1 = int(input("enter score "))
      print(f"the computer chose {rand1}")
      score_run += score_run1
      print(score_run)
      if rand1==score_run1:
        break
    print("you are out")
    print(f"your score is {score_run-score_run1}")
    # def balecision):
    if decision == ball_first[0:3]:
        print("you chose balling")
    score_run1 = 2
    score_run=0
    rand1=0
    rand2=0
    while rand2 != score_run1:        
      rand2 = random.randint(1, 6)
      score_run1 = int(input("enter score "))
      print(f"the computer chose {rand2}")
      rand1+=rand2
      print(rand1)
      if rand2==score_run1:
        break
    print("computer is out")
    print(f"the score of computer is {rand1-rand2}")
    # print(ball(decision))                                
    # print(bat(decision))
print(head_tail(ask))