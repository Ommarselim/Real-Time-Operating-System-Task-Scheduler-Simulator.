from tkinter import *
import turtle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from copy import copy
from tkinter import*
from tkinter import ttk




from tkinter import *  
import numpy as np  
#The Canvas class of Tkinter supports functions that are used to move objects from one position to another in any canvas or Tkinter top-level.
from tkinter import messagebox
from tkintertable import TableCanvas, TableModel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#pack() method:It organizes the widgets in blocks before placing in the parent widget.
#grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
#place() method:It organizes the widgets by placing them on specific positions directed by the programmer.

from Minimum_Laxity_First import Task as mlft
from Minimum_Laxity_First import OS as mlfos
from EDF import Task as edft
from EDF import OS as edfos
from DMA import Task as dmat
from DMA import OS as dmaos
from RMA import Task as rmat
from RMA import OS as rmaos
from PIL import Image,ImageTk

class UI:
    def __init__(self):
        self.root = Tk()    
#        inhert class of tinker  to create tinker window 
        self.root.title("Real-Time Operating System tasks scheduler") 
#        name of tinker object we create prefere name it with your projectname conacatenated with your name 
        self.root.config(bg="#FFF8D6")
        self.root.state('zoomed')
        self.root.config(bg="#DAECF2")

        self.root.overrideredirect(True)
        





        self.inputFrame = Frame(self.root, bg="cyan")
        self.inputFrame.pack(fill=X)

        self.inputFrame = Frame(self.root, bg="cyan")
        self.inputFrame.pack(fill=X)
        self.inputFrame.columnconfigure(0, weight=8)
        self.inputFrame.columnconfigure(1, weight=1)
        self.inputFrame.columnconfigure(2, weight=1)
        self.inputFrame.columnconfigure(3, weight=1)
        self.inputFrame.columnconfigure(4, weight=1)
        self.inputFrame.columnconfigure(5, weight=8)

        self.rtEntries = []   #  to enter release time 
        self.ptEntries = []  #  to enter periodic time 
        self.etEntries = []   #  to enter executiontime 
        self.dtEntries = []    #  to enter deadline  time 
        self.tasks =[]   #   to enter no. of tasks 
        self.useAlgorithm=0
        
#        grid    show grid composed of table with no. of rows and no.of coloumn

        Label(self.inputFrame, text="Select number of tasks: ", font=("Constantia", 16,"bold"), bg="cyan",fg="#ff6b6b").grid(row=0, column=1, pady=5)
        Label(self.inputFrame, text= "Select the Scheduling policy: ", font=("Constantia", 16,"bold"), bg="cyan",fg="#ff6b6b").grid(row=0,column=3,pady=5)  
              
# #           bg background color, fg font colour, pad  for padding y direction as canvas composed of x , y 
#         self.useAlgorithm = 0
#         Button(self.inputFrame, text="MLF", font=("times new roman", 10), bg="red", fg="white", command= self.MLF).grid(row=2, column=2, padx= 5, pady=5)
#         Button(self.inputFrame, text="EDF", font=("times new roman", 10), bg="#2069e0", fg="white", command = self.EDF).grid(row=2, column=3, padx=5, pady=5)
#         Button(self.inputFrame, text="DMA", font=("times new roman", 10), bg="gray", fg="white", command = self.DMA).grid(row=2, column=4, padx=5, pady=5)
#         Button(self.inputFrame, text="RMA", font=("times new roman", 10), bg="purple", fg="white", command= self.RMA).grid(row=2, column=5, padx=5, pady=5)



        self.taskoption = StringVar(self.inputFrame)
        self.taskoption.set("MLF")  # Set the initial selected option

        self.option_menu = OptionMenu(self.inputFrame, self.taskoption, *["MLF", "EDF", "DMA", "RMA"])
        self.option_menu.grid(row=0,column=4,pady=5)
        self.option_menu.config(width=14)


        self.taskoption.trace("w", self.show_selected_option)

        self.exit_button = Button(self.inputFrame, text="EXIT", font=('Bold ', 18),fg= 'cyan', bd=0,relief=RIDGE, bg='#c3c3c3',command=self.exit)
        self.exit_button.place(x=0,y=0)










        self.noTasks = IntVar()
#        Tkinter contains built-in programming types which work like a normal python type with additional features used to manipulate values of widgets like Label and Entry more effectively, which makes them different from python data types.
        self.noTasks.set(0)
#        default value that appear in tab no.tasks
        self.noTasks.trace("w", self.refresh)
#        trace to sense with new values
        om =OptionMenu(self.inputFrame, self.noTasks, *[0, 1, 2, 3, 4, 5])
        
#        declare inputs for this tab
        om.grid(row=0, column=2, pady=5)
        om.config(bg="cyan")
        om.config(width=14)

        self.taskFrameCanvas()


        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.mainloop()
#        stop execution of python program
        


    def show_selected_option(self,*args):
        self.selected_option = self.taskoption.get()
        if self.selected_option == "MLF":                        # Select and run algorithm
            self.MLF()
        elif self.selected_option =="EDF":
            self.EDF()
        elif self.selected_option =="DMA":
            self.DMA()
        elif self.selected_option =="RMA":
            self.RMA()


    def exit(self):
        self.root.quit()
        self.root.destroy()

    def MLF(self):
        self.algorithmUsed.config(text="Algorithm: Minimum Laxity First")
        self.useAlgorithm = 1

    def EDF(self):
        self.algorithmUsed.config(text="Algorithm: Earliest Deadline First")
        self.useAlgorithm = 2

    def DMA(self):
        self.algorithmUsed.config(text="Algorithm: Deadline Monotonic Assignment")
        self.useAlgorithm = 3

    def RMA(self):
        self.algorithmUsed.config(text="Algorithm: Rate Monotonic Assignment")
        self.useAlgorithm = 4

    def taskFrameCanvas(self):
        my_canvas = Canvas(self.root, bg="cyan")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=True)




        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.itemconfig('frame', width=my_canvas.winfo_width()))

        # Create ANOTHER Frame INSIDE the Canvas
        self.second_frame = Frame(my_canvas, bg="cyan")
        self.second_frame.columnconfigure(2, weight=2)

        self.algorithmUsed = Label(self.second_frame, text="Algorithm: ", font=("times new roman", 14, "bold"), bg="cyan", fg="#009900")
        self.algorithmUsed.pack()

        self.runFrame = Frame(self.second_frame, bg="cyan")
        Button(self.runFrame, text="RUN", font=("Constantia", 16,"bold"), bg="cyan", fg="white", bd=0, command= self.Run).pack(side=RIGHT, padx=5, pady=5)

        Label(self.runFrame, text="Max Time:", font=("Constantia", 16,"bold"), bg="cyan", fg="white").pack(side=LEFT, padx=5, pady=5)

        self.maxtimeEntry = Entry(self.runFrame, font=("Constantia", 16,"bold"), justify= CENTER)
        self.maxtimeEntry.pack(side=LEFT, padx=5, pady=5)
        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw", tags='frame')

        self.second_frame.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    def task(self, num):
        self.runFrame.pack_forget()
        f = Frame(self.second_frame, bg="cyan")
        f.columnconfigure(0,weight=1)
        f.pack(fill=X, expand=True,pady=5)
        self.tasks.append(f)
        Label(f, text=f"Task no.{num}", font=("Constantia", 16,"bold"), bg="cyan", fg="white").grid(row=0, column=0)

        f2 = Frame(f, bg="cyan")
        f2.grid(row=2, column=0)
        f2.columnconfigure(0,weight=1)
        f2.columnconfigure(1,weight=1)
        f2.columnconfigure(2,weight=1)
        f2.columnconfigure(3,weight=1)
        f2.columnconfigure(4,weight=1)
        f2.columnconfigure(5,weight=1)
        f2.columnconfigure(6,weight=1)
        f2.columnconfigure(7,weight=1)




        Label(f2, text= "Release time: ", font=("Constantia", 16,"bold"), bg="red", fg="white").grid(row=0, column=0,padx=4,pady=4)
        rtEntry = Entry(f2, font=("Constantia", 16,"bold"), justify= CENTER , bg="red")
        rtEntry.grid(row=0, column=1)
        self.rtEntries.append(rtEntry)

        Label(f2, text= "Execution time: ", font=("Constantia", 16,"bold"), bg="#473337", fg="white").grid(row=0, column=2,padx=4,pady=4)
        etEntry = Entry(f2, font=("Constantia", 16,"bold"), justify= CENTER)
        etEntry.grid(row=0, column=3)
        self.etEntries.append(etEntry)

        Label(f2, text= "Period: ", font=("Constantia", 16,"bold"), bg="#473337", fg="white").grid(row=0, column=4,padx=4,pady=4)
        ptEntry = Entry(f2, font=("Constantia", 16,"bold"), justify= CENTER)
        ptEntry.grid(row=0, column=5)
        self.ptEntries.append(ptEntry)

        Label(f2, text="Deadline: ", font=("Constantia", 16,"bold"), bg="#473337", fg="white").grid(row=0, column=6,padx=4,pady=4)
        dtEntry = Entry(f2, font=("Constantia", 16,"bold"), justify= CENTER)
        dtEntry.grid(row=0, column=7)
        self.dtEntries.append(dtEntry)
        Label(f, text="_____________________________________________________________________________________________________", bg="cyan", fg="white").grid(row=1, column=0)
        self.runFrame.pack()



    def refresh(self, *args):
        tasksNum = self.noTasks.get()
        if tasksNum == len(self.tasks):
            pass
        if tasksNum > len(self.tasks):  #add more tasks
            for i in range(len(self.tasks)+1, tasksNum+1):
                self.task(i)
        else:
            for i in range(len(self.tasks)-tasksNum): #remove some tasks
                self.tasks.pop(-1).destroy()
                self.rtEntries.pop(-1)
                self.etEntries.pop(-1)
                self.ptEntries.pop(-1)
                self.dtEntries.pop(-1)

        if tasksNum == 0:
            self.runFrame.pack_forget()

    def Run(self):
        tasks = []
        results = None
        try:
            maxtime = int(self.maxtimeEntry.get())
        except:
            self.errorMessage("Please ensure that the maxtime is an integer number")


        if self.checkEntries():
            results = []
            if self.useAlgorithm == 1:
                for arg in range(len(self.rtEntries)):
                    tasks.append(mlft(f"T{arg+1}", float(self.rtEntries[arg].get()), float(self.ptEntries[arg].get()), float(self.etEntries[arg].get()), float(self.dtEntries[arg].get()), maxtime))
                results = mlfos(tasks, maxtime).getResults()
            elif self.useAlgorithm==2:
                for arg in range(len(self.rtEntries)):
                    tasks.append(edft(f"T{arg + 1}", float(self.rtEntries[arg].get()), float(self.ptEntries[arg].get()),
                                      float(self.etEntries[arg].get()), float(self.dtEntries[arg].get()), maxtime))
                results = edfos(tasks, maxtime).getResults()
            elif self.useAlgorithm==3:
                for arg in range(len(self.rtEntries)):
                    tasks.append(dmat(f"T{arg + 1}", float(self.rtEntries[arg].get()), float(self.ptEntries[arg].get()),
                                      float(self.etEntries[arg].get()), float(self.dtEntries[arg].get()), maxtime))
                results = dmaos(tasks, maxtime).getResults()
            elif self.useAlgorithm==4:
                for arg in range(len(self.rtEntries)):
                    tasks.append(rmat(f"T{arg + 1}", float(self.rtEntries[arg].get()), float(self.ptEntries[arg].get()),
                                      float(self.etEntries[arg].get()), float(self.dtEntries[arg].get()), maxtime))
                results = rmaos(tasks, maxtime).getResults()
            else:
                self.errorMessage("please choose an algorithm to use.")
            if results:
                self.resultsWindow(results)


    def errorMessage(self, msg):
        messagebox.showerror("Error", msg)

    def checkEntries(self):
        for entry in range(len(self.rtEntries)):
            try:
              float(self.rtEntries[entry].get())
              float(self.ptEntries[entry].get())
              float(self.etEntries[entry].get())
              float(self.dtEntries[entry].get())
            except:
                self.errorMessage("Please ensure that all entries are filled either with integer or float numbers")
                return False
        return True
    def resultsWindow(self, results):
        rw = Toplevel(self.root)
        rw.geometry("1000x600+0+0")
        rw.state('zoomed')
        rw.title("Results")
        rw.config(height=2000)

        my_canvas = Canvas(rw, bg="cyan")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add A Scrollbar To The Canvas
        my_scrollbar = Scrollbar(rw, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.itemconfig('frame', width=my_canvas.winfo_width()))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas, bg="#300199")
        #second_frame.columnconfigure(2, weight=2)
        executionFrame = Frame(second_frame, bg="#440044")
        executionFrame.pack(fill=X, expand= True,pady=10)
        Label(executionFrame, text="Execution Result: ", font= ("times new roman", 20, "bold"), bg="#473337", fg="white").pack(side=TOP)
        execDict = results[0]
        fig = self.getExeFigure(execDict)
        executionFig = FigureCanvasTkAgg(fig,executionFrame)
        executionFig.get_tk_widget().pack(side=BOTTOM)


        if self.useAlgorithm==1:
            slackTabel = results[1]
            tabelFrame = Frame(second_frame, bg="#473337")
            tabelFrame.pack(fill=X, expand=True, pady=10)
            Label(tabelFrame, text="Slack Tabel: ", font=("times new roman", 20, "bold"), bg="#473337",
                  fg="white").pack(side=TOP)
            data = {}
            for row in slackTabel:
                data[row[1]] = {"time":row[1]}
                for index, slacktime in enumerate(row[0]):
                    slacktime = "-" if slacktime == None else slacktime
                    data[row[1]][f"T{index+1}"] = slacktime

            myframe = Frame(tabelFrame, bg="#473337")
            myframe.pack(side=BOTTOM)
            table = TableCanvas(myframe, data=data,
                                cellwidth=60, cellbackgr='#e3f698',
                                thefont=('times new roman', 20), rowheight=23, rowheaderwidth=50,
                                rowselectedcolor='yellow', read_only=True)
            table.show()

        elif self.useAlgorithm==2:
            deadlineTabel = results[1]
            tabelFrame = Frame(second_frame, bg="#473337")
            tabelFrame.pack(fill=X, expand=True)
            Label(tabelFrame, text="Deadline Tabel: ", font=("times new roman", 20, "bold"), bg="#473337",
                  fg="white").pack(side=TOP)
            data = {}
            for row in deadlineTabel:
                data[row[1]] = {"time": row[1]}
                for index, deadlinetime in enumerate(row[0]):
                    deadlinetime = "-" if deadlinetime == None else deadlinetime
                    data[row[1]][f"T{index + 1}"] = deadlinetime

            myframe = Frame(tabelFrame, bg="#473337")
            myframe.pack(side=BOTTOM)
            table = TableCanvas(myframe, data=data,
                                cellwidth=60, cellbackgr='#e3f698',
                                thefont=('times new roman', 20), rowheight=23, rowheaderwidth=50,
                                rowselectedcolor='yellow', read_only=True)
            table.show()

        else:
            taskPriorities = results[1]
            prioritiesFrame = Frame(second_frame, bg="#473337")
            prioritiesFrame.pack(fill=X, expand=True, pady=10)
            Label(prioritiesFrame, text="Tasks Priorities:", font=("times new roman", 20, "bold"), bg="#473337", fg="white").pack(side=TOP)
            priorities = ""
            for task in taskPriorities.keys():
                priorities += f"{task}: {taskPriorities[task]} \t"
            Label(prioritiesFrame, text= priorities, font=("times new roman", 20), bg="#473337", fg="white").pack(side=BOTTOM)

        brokenDeadlines = results[2]
        brokenDeadlineFrame = Frame(second_frame, bg="#473337")
        brokenDeadlineFrame.pack(fill=X, expand=True, pady=10)
        Label(brokenDeadlineFrame, text="Broken Deadlines: ", font=("times new roman",20, "bold"), bg="#473337", fg="white").pack(side=TOP)
        brokenDeadlinesText =""
        for task in brokenDeadlines.keys():
            brokenDeadlinesText += f"{task}: {brokenDeadlines[task]} \t"
        Label(brokenDeadlineFrame, text= brokenDeadlinesText, font=("times new roman", 20), bg="#473337", fg="white").pack(side=BOTTOM)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw", tags='frame')

        second_frame.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    def getExeFigure(self, execDict):
        colors = ['#f4eb97', '#89ddf4', 'gray', 'red', 'purple']

        fig, ax = plt.subplots(figsize=(16, 8))
        # ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
        # ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),facecolors=('tab:orange', 'tab:green', 'tab:red'))
        i = 1
        for task in execDict.keys():
            for execution in execDict[task]:
                execution[1] -= execution[0]

            ax.broken_barh(execDict[task], (11 * i, 7), facecolors=f'{colors[i - 1]}')
            i += 1

        ax.set_ylim(5, 15+10*(len(self.tasks)))
        ax.set_xlim(0, int(self.maxtimeEntry.get()))
        ax.set_xlabel('Time')
        ax.set_facecolor('black')
        fig.set_facecolor('white')
        ax.set_xticks(np.arange(0,int(self.maxtimeEntry.get())+1, 1))
        ax.set_yticks([15 + 10*tick for tick in range(len(self.tasks))], labels=[f'T{tnum+1}' for tnum in range(len(self.tasks))])
        ax.grid(True)

        return fig

UI()