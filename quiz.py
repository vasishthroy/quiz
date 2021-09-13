import os
import json

# Load json file into a dict
with open("quiz.json", "r") as jf:
    quiz_dat = json.load(jf)["quiz"]

grp = tuple(quiz_dat.keys())

theme = "\n".join((f"{n + 1}. {k}" for n, k in enumerate(grp)))

while 1:
    try:
        # Ask user to choose group
        s_grp = int(input(f"Choose group\n{theme}\n(1 / 2)\n")) - 1
        grp_name = grp[s_grp]
        break
    except IndexError:
        print("Invalid Choice")
    except ValueError:
        print("Invalid Format\n Please enter option number")
        
    

questions = quiz_dat[grp_name]

score = {"right": 0, "wrong": 0, "total": len(questions.keys())}

# TODO 
# add try except
for k in questions.keys():
    print(questions[k]['question'])
    options = questions[k]["options"]
    
    while 1:
        try:
            for n, opt in enumerate(questions[k]["options"]):
                print(f"{n+1}. {opt}")
            ans = int(input("Your answer: ")) - 1
            ans = options[ans]
            break

        except IndexError:
            print("Invalid Option Number")
        except ValueError:
            print("Invalid Answer")
            print("Enter the option number\neg. 1 or 2 or 3")
    
    if ans == questions[k]['answer']:
        score["right"] += 1
    else:
        score["wrong"] += 1


disp = ("Final Score\n"
        + f"Total Questions: {score['total']}\n"
        + f"Right Answers: {score['right']}\n"
        + f"Wrong Answers: {score['wrong']}")
# disp += "\n".join()
print(disp)