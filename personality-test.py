import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import random 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

_open = 0
conscience = 0
cb_on = 0
extrovert = 0
agree = 0
neurotic = 0

matplotlib.use("TkAgg")

class GUI(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		self.title('Personality Test')

		container.pack(side='top', fill='both', expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		containers = (Main, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9, Page10,
        			  Page11, Page12, Page13, Page14, Page15, Page16, Page17, Page18, Page19, Page20,
        			  Page20_5, Page21, Page22, Page23, Results)

		for i in containers:

			frame = i(container, self)
			self.frames[i] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.forward(Main)

	def forward(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

        
class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="Welcome to our Personality Test where we can analyze you.")
        label.pack(**pad)

        button = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page1))
        button.pack(**pad)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="How would you want to be addressed? (Optional)")
        label.pack(**pad)

        entry1 = tk.Entry(self)
        entry1.pack(**pad)
        entry1.bind("<Return>", lambda x: controller.forward(Page2))
        button1 = tk.Button(self, text="Ok",
                            command=lambda: controller.forward(Page2))
        button1.pack(**pad)

class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="Enter your contact number: (Optional)")
        label.pack(**pad)

        entry2 = tk.Entry(self)
        entry2.pack(**pad)
        entry2.bind("<Return>", lambda x: controller.forward(Page3))

        button2 = tk.Button(self, text="Ok",
                            command=lambda: controller.forward(Page3))
        button2.pack(**pad)

class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="Enter your affiliated student number: (Optional)")
        label.pack(**pad)

        entry3 = tk.Entry(self)
        entry3.pack(**pad)
        entry3.bind("<Return>", lambda x: controller.forward(Page4))

        button3 = tk.Button(self, text="Ok",
                            command=lambda: controller.forward(Page4))
        button3.pack(**pad)

class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="Let's start the Personality Test")
        label.pack(**pad)

        button4 = tk.Button(self, text="Ok",
                            command=lambda: controller.forward(Page5))
        button4.pack(**pad)


class Page5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic
        
        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I believe in the importance of art")
        label.pack(**pad)

        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	checkbox = tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var)
        	cb.append(checkbox)  
        	cb[i].pack(**pad) 

        cb_on = var.get()
        button5 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page6))
        button5.pack(**pad)

        
        def get():

        	global _open
        	_open += cb_on
        	
        get()

class Page6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="It’s important to me that people are on time")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button6 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page7))
        button6.pack(**pad)

        def get():

        	global conscience
        	conscience += cb_on

        get()

class Page7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I make friends easily")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button7 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page8))
        button7.pack(**pad)

       	def get():
       		global extrovert
        	extrovert+= cb_on

        get()

class Page8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I consider myself considerate")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button8 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page9))
        button8.pack(**pad)

        def get():
        	
        	global agree
        	agree += cb_on

        get()

class Page9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I often feel blue")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button9 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page10))
        button9.pack(**pad)

        def get():
        	
        	global neurotic
        	neurotic+= cb_on
        get()

class Page10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I have a vivid imagination")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button10 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page11))
        button10.pack(**pad)

        def get():
        	global _open
        	_open+= cb_on

        get()
class Page11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I make plans and stick to them")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button11 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page12))
        button11.pack(**pad)

        def get():
        	global conscience
        	conscience+= cb_on

        get()

class Page12(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I am the life of the party")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button12 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page13))
        button12.pack(**pad)

        def get():
        	global extrovert
        	extrovert+= cb_on

        get()
class Page13(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I accept people the way they are")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button13 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page14))
        button13.pack(**pad)

        def get():
        	global agree
        	agree+= cb_on

        get()

class Page14(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I get nervous easily")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button14 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page15))
        button14.pack(**pad)

        def get():
        	global neurotic
        	neurotic+= cb_on

        get()
class Page15(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I enjoy going to art museums")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button15 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page16))
        button15.pack(**pad)

        def get():
        	 global _open
        	 _open+= cb_on

        get()

class Page16(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I always make good use of my time")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button16 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page17))
        button16.pack(**pad)

        def get():
        	global conscience
        	conscience+= cb_on

        get()


cb_on_ = ['Open-Minded','Close-Minded','Conscious','Spontaneous','Extroverted','Introverted','Agreeable','Hostile','Neurotic','Stable']

class Page17(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I have a lot to say")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button17 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page18))
        button17.pack(**pad)

        def get():
        	global extrovert
        	extrovert+= cb_on

        get()
class Page18(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I give second chances")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button18 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page19))
        button18.pack(**pad)

        def get():
        	global agree
        	agree+= cb_on

        get()

class Page19(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I get irritated easiy")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button19 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page20))
        button19.pack(**pad)

        def get():
        	global neurotic
        	neurotic+= cb_on

        get()
class Page20(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I love hearing new ideas")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button20 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page20_5))
        button20.pack(**pad)

        def get():
        	global _open
        	_open+= cb_on

        get()
class Page20_5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I consider myself organized and systematic")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button20_5 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page21))
        button20_5.pack(**pad)

        def get():
        	global conscience
        	conscience+= cb_on

        get()

class Page21(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I am sociable")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button21 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page22))
        button21.pack(**pad)

        def get():
        	global extrovert
        	extrovert+= cb_on

        get()
class Page22(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I take care of other people before taking care of myself")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button22 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Page23))
        button22.pack(**pad)

        def get():
        	global agree
        	agree+= cb_on

        get()

class Page23(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global _open
        global conscience
        global extrovert
        global agree
        global neurotic

        pad = {'padx': 5, 'pady': 5}
        label = tk.Label(self, text="I consider myself moody and sensitive")
        label.pack(**pad)
        
        # Checkbox

        var = tk.IntVar()        
        cb = []
        text = ['Disagree','Somewhat Disagree','Neutral','Somewhat Agree','Agree']
        for i in range(5):
        	cb.append(tk.Checkbutton(self, onvalue = i+1, offvalue=0, text=text[i], variable = var))  
        	cb[i].pack(**pad)         

        cb_on = var.get()
        button23 = tk.Button(self, text="Next",
                            command=lambda: controller.forward(Results))
        button23.pack(**pad)

        def get():
        	global neurotic
        	neurotic+= cb_on

        get()


class Results(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)        

		global _open 
		global conscience 
		global extrovert 
		global agree 
		global neurotic 
		global cb_on_

		_open += cb_on
		conscience += cb_on
		cb = random.choice(cb_on_)
		extrovert += cb_on
		agree+= cb_on
		neurotic += cb_on

		label = tk.Label(self, text="You are {personality}".format(personality = cb))
		label.place(x=170, y=100, anchor='center')
		button20 = tk.Button(self, text="Ok",
                            command=lambda: app.destroy())
		button20.place(x = 170, y = 200, anchor='center')


# class Graph(tk.Frame):

    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self, parent)

    #     pad = {'padx': 5, 'pady': 5}
    #     label = tk.Label(self, text="These are your results.")
    #     label.pack(**pad)
                
#         fig = plt.Figure()
#         ax = fig.add_subplot(111)

#         X = np.linspace(1,20,5)
#         Y = [12,17,8,10,19]
#         ax.bar(X, Y)
#         plt.title('Results')
#         plt.xlabel('Traits')
#         plt.ylabel('Score')
#         plt.xticks([0,1,2,3,4], ["Openness","Conscientiousness","Extraversion","Agreeableness","Neuroticism"], fontsize='small')
#         plt.ylim(0,20)
#         plt.legend(["Openness","Conscientiousness","Extraversion","Agreeableness","Neuroticism"])
        
#         for i in ax.patches:
#         	width, height = i.get_width(), i.get_height()
#         	x, y = i.get_xy() 
#         	plt.annotate(f'{round(height/20,2)}', (x + 0.3, height*1.01), fontsize = 'large')
#         plt.savefig('img.jpeg')

#         canvas = FigureCanvasTkAgg(fig, self)
#         canvas.draw()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         button_ = tk.Button(self, text="Ok",
#                             command=lambda: app.destroy())
#         button_.pack(**pad)


if __name__ == '__main__':
	
	app = GUI()
	app.mainloop()
	

	


