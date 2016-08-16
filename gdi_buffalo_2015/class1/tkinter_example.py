import Tkinter
import random

my_gui = Tkinter.Tk()

my_gui.title("Pypet")
my_gui.geometry("500x300")


def express_happy():
        say_options =["I love you!", "Hip hip hurray!", "Purr, Purr"]
        my_label = Tkinter.Label(my_gui, text = random.choice(say_options))
        my_label.pack()

feed_button = Tkinter.Button(my_gui, text = "Feed Me", command = express_happy)

feed_button.pack()

my_gui.mainloop()


    	
