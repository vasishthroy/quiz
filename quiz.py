import json

# Load json file into a dict
with open("quiz.json", "r") as jf:
    quiz_dat = json.load(jf)["quiz"]

def printc(text, col_code, pt=True, end="\n"):
    """
    Prints Color print Text
    """
    color_txt = f"\033[{col_code}m{text}\033[m"

    if pt:
        print(color_txt, end=end)
        return None
    
    return color_txt


grp = tuple(quiz_dat.keys())

theme = "\n".join((f"{n + 1}. {k}" for n, k in enumerate(grp)))

while 1:
    try:
        # Ask user to choose group
        s_grp = int(input(f"Choose group\n{theme}\n(1 / 2)\n")) - 1
        grp_name = grp[s_grp]
        break

    # Print error message if wrong index or data type is input
    except IndexError:
        printc("Invalid Choice", 31)
    except ValueError:
        printc("Invalid Format\nPlease enter option number", 31)
        
questions = quiz_dat[grp_name]

# Dictionary to track scores
score = {"right": 0, "wrong": 0, "total": len(questions.keys())}

# Display question and options
for k in questions.keys():
    # Return to option selection in case of wrong input from user 
    while 1:
        print(questions[k]['question'])
        options = questions[k]["options"]
    
        try:
            for n, opt in enumerate(questions[k]["options"]):
                print(f"{n+1}. {opt}")

            # Index starts with zero and option starts from 1 
            ans = int(input("Your answer: ")) - 1 
            ans = options[ans]
            break

        # Print error message if wrong index or data type is input
        except IndexError:
            printc("Invalid Option Number", 31)
        except ValueError:
            printc("Invalid Answer", 31)
            printc("Enter the option number\neg. 1 or 2 or 3", 31)
        finally:
            print("\n")
    
    # Score counting
    if ans == questions[k]['answer']:
        score["right"] += 1
    else:
        score["wrong"] += 1

disp = ("Final Score\n"
        + f"Total Questions: {score['total']}\n"
        + printc(f"Right Answers: {score['right']}\n", 32,False)
        + printc(f"Wrong Answers: {score['wrong']}", 31,False))

print(f"\n{disp}")