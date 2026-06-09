def check_goal(goal, hours):
    if hours >2:
        print(f"great! 2 hours a day is enough to become a AI engineer.")
    else:
        print(f"You need more time to become a AI engineer.")

goals = ["AI Engineer", "python Developer", "Tech Enterpreneur"]
 
for goal in goals: 
       hours = int(input(f"how many hours will you study for AI engineer? "))
       check_goal(goal, hours)