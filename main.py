from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    title_label["text"] = "Timer"
    title_label["fg"] = GREEN
    label_tick["text"] = ""
    canvas.itemconfig(canvas_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():  # this function is the function that is called when the start button is pressed
    global reps  # This global value tells you which section of the pomodoro your in
    reps += 1
    work_sec = WORK_MIN * 60  # All three below calculate how many seconds in each part of pomodoro
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if(reps % 8 == 0): # Depending on the section your in , the text would display your current status
        title_label["text"] = "Long Break"
        title_label["fg"] = RED
        count_down(long_break_sec)  # This is actually the function that performs the juicy timer. Func takes in seconds
    elif(reps % 2 == 0):
        title_label["text"] = "Short Break"
        title_label["fg"] = PINK
        count_down(short_break_sec)
    else:
        title_label["text"] = "Work !"
        title_label["fg"] = GREEN
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):  # very important function
    mins = str((int(count / 60))).zfill(2)  # Find how many minutes to dispaly . fill with 0s
    seconds = str(int(count % 60)).zfill(2)  # find out how many minutes to display
    canvas.itemconfig(canvas_text, text=f"{mins}:{seconds}")  # *key. from the canvas -> pick an item -> pick a part
    if(count > 0):                                            # to change. In this case our item is canvas_text
        global timer
        timer = window.after(1000, count_down, count - 1)  # ** key recursive function that allows changes to be made
    else:
        start_timer()  # once a specific section is finished we move onto the next section. reps is increased
        if(reps % 2 == 0):
            print(reps)
            label_tick["text"] += "✔"
# ---------------------------- UI SETUP ------------------------------- #


window = Tk() # Calling the TK class
window.title("Pomodoro")  # Setting the title of our screen
window["background"] = YELLOW  # one of the attributes of the TK class and setting it to a constant value
window.config(padx = 100, pady = 50)  # calling a function called config. There is a difference between function and atr

# Tomato  / Timer
canvas = Canvas() # we have our window. we use the canvas to lay things on top of each other
canvas["highlightthickness"] = 0 # The canvas has a border. This hides the border
canvas["width"] = 200 # Canvas is a square frame so this sets the width
canvas["height"] = 224 # Canvas = square so this sets height
canvas["bg"] = YELLOW # this and all the above are attributes of the canvas class. we could have used constructor too
tomato_img = PhotoImage(file = "./tomato.png") # To put an image on the canvas we need to first call Photo Image
canvas.create_image(100, 112, image=tomato_img) # we store the photo image in a variable and apss that var to this
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1) # both of the above function ask for x y position and then the other attributes.

# Text Label
title_label = Label()  # simple label
title_label["text"] = "Timer"
title_label["fg"] = GREEN  # colour of the actual writing
title_label["bg"] = YELLOW
title_label["font"] = (FONT_NAME, 30, "bold")  # for font attribute we actually pass a tuple
title_label.grid(row=0, column=1)

label_tick = Label()
label_tick["fg"] = GREEN
label_tick["bg"] = YELLOW
label_tick["font"] = (FONT_NAME, 15, "bold")
label_tick.grid(row=3, column=1)

# Buttons
button1 = Button()  # simple button
button1["text"] = "Start"
button1["font"] = (FONT_NAME, 10, "bold")
button1["command"] = start_timer  # the command attribute equates to a function that is called when button is pressed
button1.grid(row=2, column=0)

button2 = Button()
button2["text"] = "Reset"
button2["font"] = (FONT_NAME, 10, "bold")
button2["command"] = reset
button2.grid(row=2, column=2)





window.mainloop()
