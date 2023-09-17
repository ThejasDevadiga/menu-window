from tkinter import *
from ttkbootstrap import Style

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.geometry("500x500")
		self.title("Menu Page window")
		#Setup Menu
		MainMenu(self)
        
		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=1, sticky="nsew")

		self.show_frame(StartPage)	
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.style = Style(theme="superhero")
		label = Label(self, text="Start Page")
		label.pack(padx=10, pady=10)
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageOne(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		label = Label(self, text="Page One")
		label.pack(padx=10, pady=10)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageTwo(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		label = Label(self, text="Page Two")
		label.pack(padx=10, pady=10)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()

class MainMenu:
	def __init__(self, master):
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		viewmenu = Menu(menubar, tearoff=0)
		editmenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New")
		filemenu.add_command(label="Save")
		filemenu.add_command(label="Exit", command=master.quit)
		editmenu.add_command(label="Undo")
		editmenu.add_command(label="Redo")
		viewmenu.add_command(label="Show", command=master.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		menubar.add_cascade(label="Edit", menu=editmenu)
		menubar.add_cascade(label="View", menu=viewmenu)
		master.config(menu=menubar)

app = App()
app.mainloop()