import tkinter as tk                # python 3
from tkinter import DISABLED, font as tkfont, scrolledtext
from tkinter import *
import random

MainBGColor = "gray64"
BGButtonColor = "gray8"
FGButtonColor = "ivory1"
EnergizerColor = "orchid3"
FocusColor = "indianred"
IceBreakersColor = "springgreen3"
SensesColor = "cornflowerblue"
ImprovisationColor = "lightgoldenrod"
RhythmColor = "turquoise1"
MiscellaneousColor = "orange2"

ScrollBoxHeight = 11
ScrollBoxWidth = 75

ipadSize = 23
padSize = 5
reliefType = GROOVE

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.body_font = tkfont.Font(family='Helvetica', size=18)
        self.game_font = tkfont.Font(family='Helvetica', size=14, weight="bold")
        self.menu_font = tkfont.Font(family='Helvetica', size=10, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self)
        container.grid(rowspan=1, column=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        pageList = [StartPage, 
        SubEN, SubEN1,
        SubFO, SubFO1, SubFO2,
        SubIC, SubIC1,
        SubSE,
        SubIM, SubIM1, SubIM2,
        SubRH,
        SubMI, SubMI1, SubMI2,
        G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20,
        G21, G22, G23, G24, G25, G26, G27, G28, G29, G30, G31, G32, G33, G34, G35, G36, G37, G38, G39, G40,
        G41, G42, G43, G44, G45, G46, G47, G48, G49, G50]

        self.frames = {}
        for F in (pageList):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.pack_propagate(False)
        frame.tkraise()
    def randomGame(self):
        gameSel = random.randrange(1,50)
        self.show_frame("G"+str(gameSel))

class StartPage(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Sav's Game File!", font=controller.title_font)
        label.grid(row=1, column=2, pady=15)

        shuffle = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\shuffle.png")
        button0 = tk.Button(self, bg="slate gray", image = shuffle, relief=reliefType,
                            command=lambda: controller.randomGame())
        button0.image=shuffle
        power = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\power.png")
        button1 = tk.Button(self, bg="tomato2", image = power, relief=reliefType,
                            command=lambda: exit())
        button1.image=power
        button2 = tk.Button(self, bg=EnergizerColor, text="Energizers", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubEN"))
        button3 = tk.Button(self, bg=FocusColor, text="Focus", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubFO"))
        button4 = tk.Button(self, bg=IceBreakersColor, text="Ice Breakers", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubIC"))
        button5 = tk.Button(self, bg=SensesColor, text="Senses", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubSE"))
        button6 = tk.Button(self, bg=ImprovisationColor, text="Improvisation", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubIM"))
        button7 = tk.Button(self, bg=RhythmColor, text="Rhythm", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubRH"))
        button8 = tk.Button(self, bg=MiscellaneousColor, text="Miscellaneous", relief=reliefType, font=controller.menu_font,
                            command=lambda: controller.show_frame("SubMI"))
        button0.grid(row=1, column=3)
        button1.grid(row=1, column=1)
        button2.grid(row=2, column=1, ipadx=56, ipady=40, pady =5, padx=5)
        button3.grid(row=2, column=2, ipadx=76, ipady=40, pady =5, padx=5)
        button4.grid(row=2, column=3, ipadx=52, ipady=40, pady =5, padx=5)
        button5.grid(row=3, columnspan=4, ipadx=278, ipady=40, pady =5, padx=5)
        button6.grid(row=4, column=1, ipadx=49, ipady=40, pady =5, padx=5)
        button7.grid(row=4, column=2, ipadx=72, ipady=40, pady =5, padx=5)
        button8.grid(row=4, column=3, ipadx=45, ipady=40, pady =5, padx=5)

class SubEN(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Energizers Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubEN1"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubEN1"))
        button3 = tk.Button(self, bg=EnergizerColor, text="SHAZAM!", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G1"))
        button4 = tk.Button(self, bg=EnergizerColor, text="Fruit Salad", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G2"))
        button5 = tk.Button(self, bg=EnergizerColor, text="Duck, Duck... ANYTHING!", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G3"))
        button6 = tk.Button(self, bg=EnergizerColor, text="Keep Your Sheep", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G4"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubEN1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Energizers Page 2", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubEN"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubEN"))
        button3 = tk.Button(self, bg=EnergizerColor, text="Motion Tag", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G5"))
        button4 = tk.Button(self, bg=EnergizerColor, text="Affirmations", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G6"))
        button5 = tk.Button(self, bg=EnergizerColor, text="Hot Spot/Song Association", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G7"))
        button6 = tk.Button(self, bg=EnergizerColor, text="Zip, Zap, Zop", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G8"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubFO(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Focus Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO1"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO2"))
        button3 = tk.Button(self, bg=FocusColor, text="One Word Story", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G9"))
        button4 = tk.Button(self, bg=FocusColor, text="Round of Applause", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G10"))
        button5 = tk.Button(self, bg=FocusColor, text="Counting", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G11"))
        button6 = tk.Button(self, bg=FocusColor, text="Spot the Difference", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G12"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubFO1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Focus Page 2", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO2"))
        button3 = tk.Button(self, bg=FocusColor, text="Three, Six, Nine", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G13"))
        button4 = tk.Button(self, bg=FocusColor, text="Going on a Trip", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G14"))
        button5 = tk.Button(self, bg=FocusColor, text="Circle Switch", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G15"))
        button6 = tk.Button(self, bg=FocusColor, text="Silent & Serious", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G16"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubFO2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Focus Page 3", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubFO1"))
        button3 = tk.Button(self, bg=FocusColor, text="Bippity, Bippity, Bop", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G17"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="bottom", fill="x",ipady=20, pady=padSize, padx=10)

class SubIC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Ice Breakers Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIC1"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIC1"))
        button3 = tk.Button(self, bg=IceBreakersColor, text="Name Game", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G18"))
        button4 = tk.Button(self, bg=IceBreakersColor, text="MeYouYouMe", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G19"))
        button5 = tk.Button(self, bg=IceBreakersColor, text="The Truth About Me", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G20"))
        button6 = tk.Button(self, bg=IceBreakersColor, text="A Fine, Fine Line", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G21"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubIC1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Ice Breakers Page 2", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIC"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIC"))
        button6 = tk.Button(self, bg=IceBreakersColor, text="Ducks & Cows", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G22"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="bottom", fill="x",ipady=20, pady=padSize, padx=10)

class SubSE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Senses Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button3 = tk.Button(self, bg=SensesColor, text="Pinocchio", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G23"))
        button4 = tk.Button(self, bg=SensesColor, text="Statues", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G24"))
        button5 = tk.Button(self, bg=SensesColor, text="Sound Ball", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G25"))
        button6 = tk.Button(self, bg=SensesColor, text="Group Environment", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G26"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubIM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Improvisation Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM1"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM2"))
        button3 = tk.Button(self, bg=ImprovisationColor, text="Get in the Taxi!", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G27"))
        button4 = tk.Button(self, bg=ImprovisationColor, text="Yes, No, Please, Banana", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G28"))
        button5 = tk.Button(self, bg=ImprovisationColor, text="Why Are You Late?", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G29"))
        button6 = tk.Button(self, bg=ImprovisationColor, text="Beads on a String", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G30"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubIM1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Improvisation Page 2", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM2"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM"))
        button3 = tk.Button(self, bg=ImprovisationColor, text="Beans, Beans, Beans", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G31"))
        button4 = tk.Button(self, bg=ImprovisationColor, text="Stream of Consciousness", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G32"))
        button5 = tk.Button(self, bg=ImprovisationColor, text="Pop-Up Book", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G33"))
        button6 = tk.Button(self, bg=ImprovisationColor, text="Alphabet Conversation", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G34"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubIM2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Improvisation Page 3", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubIM1"))
        button3 = tk.Button(self, bg=ImprovisationColor, text="Expert", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G35"))
        button4 = tk.Button(self, bg=ImprovisationColor, text="Questions", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G36"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="bottom", fill="x",ipady=20, pady=padSize, padx=10)

class SubRH(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Rhythm Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button3 = tk.Button(self, bg=RhythmColor, text="We Will Shock You", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G37"))
        button4 = tk.Button(self, bg=RhythmColor, text="Snap, Clap, Stomp", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G38"))
        button5 = tk.Button(self, bg=RhythmColor, text="Penny, Penny", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G39"))
        button6 = tk.Button(self, bg=RhythmColor, text="Catch & Clap", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G40"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubMI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Miscellaneous Page 1", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI1"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI2"))
        button3 = tk.Button(self, bg=MiscellaneousColor, text="This is a Pen", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G41"))
        button4 = tk.Button(self, bg=MiscellaneousColor, text="Watch Your Step", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G42"))
        button5 = tk.Button(self, bg=MiscellaneousColor, text="Magic Present", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G43"))
        button6 = tk.Button(self, bg=MiscellaneousColor, text="Tableau Olympics", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G44"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubMI1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Miscellaneous Page 2", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI2"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI"))
        button3 = tk.Button(self, bg=MiscellaneousColor, text="I Scream", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G45"))
        button4 = tk.Button(self, bg=MiscellaneousColor, text="Pantomime Telephone", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G46"))
        button5 = tk.Button(self, bg=MiscellaneousColor, text="Who Started the Motion?", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G47"))
        button6 = tk.Button(self, bg=MiscellaneousColor, text="Keeper of the Keys", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G48"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button5.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button6.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="top", fill="x",ipady=20, pady=padSize, padx=10)

class SubMI2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainBGColor)
        self.controller = controller
        label = tk.Label(self, bg=MainBGColor, text="Miscellaneous Page 3", font=controller.title_font)
        label.pack(side="top", fill="none", pady =10)
        button1 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text=">", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI"))
        button2 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="<", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("SubMI1"))
        button3 = tk.Button(self, bg=MiscellaneousColor, text="Collaboration Creativity", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G49"))
        button4 = tk.Button(self, bg=MiscellaneousColor, text="Who's Telling the Truth?", font=controller.game_font, relief=reliefType,
                            command=lambda: controller.show_frame("G50"))
        button7 = tk.Button(self, bg=BGButtonColor, fg=FGButtonColor, text="Home", font=controller.menu_font, relief=reliefType,
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="right", fill="y", ipadx=15,pady=padSize, padx=10)
        button2.pack(side="left", fill="y", ipadx=15,pady=padSize, padx=10)
        button3.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button4.pack(side="top", fill="x", ipady=ipadSize,pady=padSize, padx=10)
        button7.pack(side="bottom", fill="x",ipady=20, pady=padSize, padx=10)

class G1(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """A large group game where groups go into battle against one another. In this war, in a similar way to Rock, Papers, Scissors, the Giants beat Knights, Knights beat Wizards, and Wizards beat Giants."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED, relief=reliefType)
        label = tk.Label(self, bg=EnergizerColor, text="SHAZAM!", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN"))
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)


class G2(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students will begin in a circle of chairs - one for every player minus one. Label each student with a type of fruit- Cherry, Strawberry, Pineapple. (definitely add more variations if class is larger) The facilitator will stand in the middle and call out one of the fruit options. Everyone who has been labeled that fruit (and the caller) will have to stand up and try to find an empty chair. The last person standing is now in the middle. The caller can also call out “Fruit Salad” in which case, everyone must now try to find a different seat. """
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Fruit Salad", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN"))
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G3(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """This game is a variation on Duck, Duck, Goose. Students sit in a large circle on the floor. One student walks around the circle and taps other students on the head (or points at their heads) saying “duck”. When the student gets to the person they wish to chase them, the first student will say a noun (can be a person, character, animal, food, etc). The second student will then become whatever noun was said with their body and “chase” the other student around trying to tag the first student before they are able to sit down. It is important that the facilitator tell the students that committing and using their body to become the word they were given is FAR more important than actually catching the first student. This continues until all/most students have gotten the chance to become something."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Duck, Duck... Anything!", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G4(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Best played with an odd number of students. There are two circles, one inner circle of chairs, and one outer circle of people. Students who decide to be in the inner circle first but take a seat on one of the chairs in the inner circle, but must leave one chair open. The rest of the players will be directly behind the chairs, with one person having an empty chair in front of them. The people in the chairs are sheep, the people behind them are the sheepherders. The person with the empty chair must try to get a sheep in their chair using nonverbal communication. It is the goal of the sheep to try to move to different chairs, and it is the goal of the herders to keep their sheep by tapping the sheep on the shoulder before the sheep get away (but the herders cannot move from behind the chair.). After enough time has passed, the sheep and the herders switch spots in the circle, so that their roles can reverse."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Keep Your Sheep", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G5(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The group of players must first decide who’s “it”. The person who’s it must come up with a motion for everyone to do, and a sound that goes along with it. Once everyone has the hang of it, they are free to move around the space, while repeating the motion. The one who’s it, while also doing the motion and sound, will try to tag someone else. Once a person is tagged, they must come up with a different motion/sound. Repeat until the facilitator decides it’s over."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Motion Tag", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G6(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have the whole class stand in a circle, holding hands (optional), eyes looking at the floor. Going around the circle, each student will say one word at a time, building upon one another to collectively create a phrase that sets a challenge for that day’s work (or positively reflecting on that day’s activity). When the group collectively feels that a phrase has been completed, they will raise their hands in the air and step in the circle creating a big clump while shouting “Yes!”. The players then take their place back in the circle and a new phrase begins where they left off. 
        
        Ex: “Today…we…will…listen…and…work…together.” ALL: “Yes!”"""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Affirmations", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G7(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """It begins with the group standing in a circle. A suggestion may be given, but it is not necessary. One person will step into the center of the circle and begin singing a song, preferably a song most of the group already knows. After a few brief lines of song someone must tap out the player in the center and take their place. That player then begins singing a new song somehow inspired by the previous song.That becomes the pattern, as player after player tap into the center of the circle to sing a song. Players in the surrounding circle may support by singing along, clapping hands, impersonating instruments, etc. The circle also provides support by tapping in to move the exercise along and not leave the singer in the center for too long."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Hot Spot/Song Association", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G8(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Invite students to stand in a circle. Ask the group to repeat the words “Zip, Zap, Zop” three or four times, all together. Introduce the activity: Imagine that I have a bolt of energy in my hands. To start the game, I will send the bolt out of energy out of my body with a strong forward motion straight to someone else in the circle (use hands, body, eyes, and voice to make contact across the circle) and say, “Zip.” Explain that the next person takes the energy and passes it immediately to someone else saying “Zap.” That person passes it on to another participant with a “Zop.” The game continues and the “Zip, Zap, Zop” sequence is repeated as the energy moves around the circle."""
        tk.Frame.__init__(self, parent, bg=EnergizerColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=EnergizerColor, text="Zip, Zap, Zop", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubEN1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G9(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The teacher starts the story with one sentence (i.e., “Once upon a time, there was a princess who dreamed of being an astronaut”). Moving clockwise around the circle, each student adds one word to the story. The circle is repeated as many times as the teacher deems necessary until they feel the story is finished."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="One Word Story", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G10(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The first person turns to the person next to them and the two try to clap at the same time. If they don’t clap at the same time, the action repeats until they do. Then the second person turns to the one on the other side of them, and the action repeats. Everyone will have someone to clap in unison with. Additional claps may be added if desired. """
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Round of Applause", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G11(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students can be sitting/standing/spread throughout the room/anyway you desire. Students must count up. One number at a time, one person at a time. If two students say the same number/there’s a mess up, the count must reset. You can set goals for the students to reach, set limitations, etc. 
        
        (Ex: Get to 20, each student can only speak twice.) Students can have their eyes open, closed, focused on one spot, etc. It’s a very open-ended activity, however, a pattern should not be established (i.e students always say the numbers in the same order/the same person starts the round)."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Counting", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G12(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have players stand in two equally sized lines. The lines should be facing one another. Have the students take 1 minute to study the appearance of the person in front of them carefully. After 1 minute, have both lines turn around and change 3 subtle things about their appearance. Once everyone is done, have everyone turn back around, and each person must try to guess what the 3 changed aspects of their partners are. Continue/shift as desired."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Spot the Difference", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G13(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have players stand in a line. The first person in line will count starting from 1, the second person will say 2, and so on and so forth. Every person that says a number that has a 3, 6, or 9 anywhere in the number will have to clap instead of saying the number. If someone forgets to clap, or claps when they’re not supposed to, the counting starts over. This repeats until the desired number is reached/until the facilitator decides to end it."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Three, Six, Nine", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G14(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Players will stand in the circle. The person designated to start says “I’m going on a trip and I’m bringing (item that starts with the letter A)”. The person next to them says “I’m going on a trip and I’m bringing (Person 1’s item and ((an item that starts with the letter B))). The pattern continues on and on, with each person repeating the items of the people before them until the alphabet is over. Other variations include not going by the alphabet, and “Going to the store” which is “I’m going to the store and I’m getting…” and the players can only list items found at the grocery store."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Going on a Trip", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G15(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Ask the players to form a circle with one person in the middle. The object of the game is for two people within the circle to silently cue each other and trade places within the circle without attracting attention of the middle player. The middle player’s goal is to get to an open spot before the switching players get there. Whoever is left without a spot is now in the middle. The players must only move inside the circle, not on the outside."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Circle Switch", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G16(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have each student choose a partner. Instruct the students to stand back to back with their partner. On the count of three, everyone must face their partner, and keep a silent and serious face. The facilitator will walk around as the inspector. The first person to smile or laugh must sit down. Have the remaining students take new partners, then repeat the exercise again. Keep going until there are only one or two pairs remaining. If at the end no one is breaking down, allow the class to act as hecklers to try and disrupt them."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Silent & Serious", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G17(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Players stand in a circle, with one person in the center. The person in the center must walk up to someone in the circle and say “Bippity Bippity Bop”, with the goal of getting through the phrase before the person they’re in front of can say “Bop”. If they do that successfully, they take that person’s spot in the circle and the other person is now in the center. If the person does say “Bop” quick enough, they have to find another person to try and replace in the circle. Add-ons include saying “Bop” to the people in the circle, and the people have to remain silent, and adding an action that the people in the circle must do."""
        tk.Frame.__init__(self, parent, bg=FocusColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=FocusColor, text="Bippity, Bippity, Bop", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubFO2"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G18(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Best played at the beginning of the year/semester. Everyone stands in a circle. The facilitator starts by saying their name. Everyone in the circle repeats the facilitator’s name. The person to the right says their name. The class repeats the name, it moves onto the next person, and so on and so forth. Repeat the process 1-2 times. Then the objects come in. The facilitator has a bean bag/hackysack/small stuffed animal/other small object that’s easy to throw. The facilitator will call the name of someone in the circle and toss it to the person they just called. The person must catch it and choose someone else to throw it to. Encourage the students to choose someone who is not right next to them in the circle. Once everyone has had the object tossed to them, start it all over again, with everyone throwing it to the same person they threw it to before, but this time, a little faster. Other variations include: Adding a second object into the mix, going backwards, or using things other than names (like fruits, vegetables, states, etc.)"""
        tk.Frame.__init__(self, parent, bg=IceBreakersColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=IceBreakersColor, text="Name Game", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIC"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G19(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have everyone stand in a line. The players must follow a script, essentially “Me. You. You. Me”, but with their names and the names of the person in front of them. The 1st student in line (i.e. Mark) turns to the 2nd student in line (i.e. Rachel) and initiates the following script
        
        - M: “Marc” (me)
        - R: “Rachel” (you)
        - M: “Rachel” (you)
        - R: “Marc” (me)

        Marc then moves to the next person in line and does the same thing. He continues with everyone down the line until he ends up standing at the opposite end from which he started. Now the new head of the line (in this case Rachel) does the same thing, all the way down the line until she ends up at the end. After the class becomes comfortable with the pattern, encourage them to speed up and do it as quickly as possible (while still speaking loud and clearly). Continue until everyone has had a chance to go down the line."""
        tk.Frame.__init__(self, parent, bg=IceBreakersColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=IceBreakersColor, text="MeYouYouMe", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIC"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G20(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students will begin in a circle of chairs - one for every player minus one. The facilitator will stand in the middle and say one thing that is true about them. (i.e “The truth about me is I live in Texas.) Everyone who can relate to that statement will have to stand up and try to find an empty chair. The last person standing is now in the middle. The person in the middle is encouraged not to “target” people that they know have specific truths."""
        tk.Frame.__init__(self, parent, bg=IceBreakersColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=IceBreakersColor, text="The Truth About Me", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIC"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G21(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Divide the class into groups of 6-8 players. Instruct them to arrange themselves in a line in order of height. When they are finished they must call out “We’re a fine, fine line, whoo!” (Or have them come up with their own silly phrase.) Repeat the game with various groups giving each one a different criteria (such as age, number of siblings, etc.) Making it a silent game is also an option."""
        tk.Frame.__init__(self, parent, bg=IceBreakersColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=IceBreakersColor, text="A Fine, Fine Line", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIC"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G22(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Everyone stands in a circle and closes their eyes. Go around the circle and tap students one by one. A tap on the right shoulder makes them a duck, a tap on the left shoulder makes them a cow. When you say “Go” they are to open their eyes, then find the member of their group by “quacking” or “moo-ing”. Once in their groups, the students are encouraged to get to know each other a bit."""
        tk.Frame.__init__(self, parent, bg=IceBreakersColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=IceBreakersColor, text="Ducks & Cows", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIC1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G23(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Narrative pantomime of the wooden puppet slowly coming to life: “Right now you're made completely of wood. Your arms and legs are carved from a single piece of wood. You can't move any part of yourself at all.Now the magic spell has begun. It begins at the top of your head. The spell moves down slowly until your head down to your eyebrows is flesh and blood. Try and move your eyebrows.The spell keeps moving down. Now you can move your eyes! All your life you've been staring straight ahead, and now you can look to the sides. The spell gets to your ears and your nose. See if you can wiggle them. The spell gets to your mouth. You can smile. It feels strange at first, and probably looks pretty strange too, but you grow more comfortable with it. Try some other facial expressions as well. Slowly you discover that you can turn your head. Careful! You can look up and down carefully as well. Look! You have feet! This is the first time you were ever sure. The spell reaches your shoulders. But remember, your arms and hands are still attached to your torso, since you are carved from a single piece of wood, so you can move ONLY your shoulders. Try some circles. Do you feel a tingle up and down your spine? That's the magic working. The spell reaches your chest. You can puff it out like a soldier. Your elbows can move now, but still not your hands. As the spell goes lower, see if you can pull your left hand away from your body. Ooofff! You did it. Bring your hand up to your face and study it. See if you can move the fingers. Wow! You've never seen anything so beautiful! See if you can get your right hand free as well.  Does it move too? The spell has reached your waist. Carefully bend forward to the side. See if you bend backwards. See if you can make a circle. The spell reaches your hips, but your knees are still locked together, and your feet are still attached to your pedestal. The spell gets to your knees. See if they bend!"""
        tk.Frame.__init__(self, parent, bg=SensesColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=SensesColor, text="Pinocchio", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubSE"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G24(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """One person is designated a “night security guard” at a museum. The rest of the players are the statues. Whenever the guard isn’t looking, the statues must change location/position/stance, whilst trying not to get caught moving. If they are caught, they can either be out of the game, or become an additional guard (facilitator’s discretion). Once every statue has been “caught”, a new guard is chosen. This game is really fun with the lights off while the guard has a flashlight/phone flashlight, but that is also at the facilitator’s discretion."""
        tk.Frame.__init__(self, parent, bg=SensesColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=SensesColor, text="Statues", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubSE"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G25(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Create a standing circle. Explain to the class that in your pocket you have a very special, very magical sound ball. Mime pulling a tiny ball out of your pocket and then show it to the class. Explain that this ball is magic because the louder the sound you make, the bigger the ball grows. The quieter the sound, the ball shrinks. Give an example of a loud sound, and mime the ball growing very large and very heavy, requiring both hands to hold it. Then give an example of a quiet sound, and mime the ball shrinking to something very tiny and light. Explain that you are going to pass this magic sound ball around the circle, and each student must make a sound to either grow or shrink the ball, then pass it to her neighbor. Remind the students that their whole bodies should reflect how heavy or light the ball is, especially when passing it to another person. After the ball goes around once, allow the kids to bounce the ball across the circle. Encourage them to make strong eye contact with whomever they are passing it to. (Once again, make sure the kids keep track of how big or small the ball is.)"""
        tk.Frame.__init__(self, parent, bg=SensesColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=SensesColor, text="Sound Ball", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubSE"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G26(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """In a group you decide on an environment (i.e. kitchen), then one by one players enter the kitchen and create one object (i.e. a player enters and opens a refrigerator) and exits. Each subsequent player that enters must use the object that the players created before as well as introduce one new element so that the last player to enter must remember everything that was used before them. It is important to emphasize the value of consistency of a physical environment.  Has the sink stayed in the same place every time, did someone leave the refrigerator door open and did the next player not think to close it?"""
        tk.Frame.__init__(self, parent, bg=SensesColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=SensesColor, text="Group Environment", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubSE"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G27(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """In this activity, you put four chairs in a square. You ask one student to be the first taxi driver so they sit in the chair that the front left seat to be the “driver.” You then ask three other people to volunteer to be passengers of this taxi. Tell the students to think of fun characters that are different from themselves and really have fun with that character in the taxi! You cycle through everyone, everyone shifting in the chairs so that they all get to be the taxi driver too. It’s easy to connect the characters that are going to be in the taxi to different things!"""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Get in the Taxi!", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G28(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Divide the class into pairs. The goal of each pair is to create a 30 second scene using only four words: “Yes”, “No”, “Please” and “Banana”. Depending on the age group, encourage the students to include a range of emotions in the scene, and if possible to have a beginning, middle and end. Although many of the scenes will be silly, encourage them to try and make it believable. Allow the students a few minutes to practice, then have them perform in front of the class."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Yes, No, Please, Banana", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G29(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Ask six players to take the stage. Choose four of the players to be “officer workers”, one player to be the “boss”, and one player to be the “late worker”. The “office workers” should sit facing the audience, miming typing on a computer. The “boss” and “late worker” leave the room while the “officer workers” come up with a reason why the “late worker” is late. (i.e. Their hair got caught in the dishwasher! Their car got crushed by a dinosaur!, etc.) Once the “office workers” have decided, they go back to typing at their computers. The “boss” enters and stands with their back to the office workers so they can’t see them. Then the “late worker” enters and faces the boss. The “late worker” can see the “officer workers”, but the “boss” can’t. The “boss” asks the “late worker” So, why are you late?! The “office workers” mime out the reason for lateness behind the “boss’” back and the “late worker” has to guess what it is. At any time, the “boss” can turn around to face the “office workers” – if they catch one of them not typing, that “office worker” is fired and must leave the office. The game ends when the “late worker” guesses the correct reason for lateness, or the “boss” fires all the “office workers”."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Why Are You Late?", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G30(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Standing in a circle, choose two students standing right next to each other. Standing in front of them, assign the person on the right to be “A” and the one on the left to be “B”. Ask them both to take 5 seconds to think of a random phrase. Then ask “A” to share, and immediately after ask “B” to share. These two phrases become the first and final lines of a story. One by one, down the circle, have students come up with sentences that complete the middle of the story. (It’s easiest to go in order from A to B) After the “string” is completed, ask the whole group to repeat the story in order. The challenge is to have the story make the most sense as possible."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Beads on a String", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G31(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Choose three people to perform the scene. The dialogue is as follows:
    
    - Person 1: Beans, beans, beans. How I love making beans!
    - Person 2: Wow, are those beans you’re making?
    - 1: Yup.
    - 2: May I have some?
    - 1: Sure!
    - 2: Oh no! These beans are… poisoned! (Dramatically falls to the ground.)
    - 1: Is there a doctor around here?
    - 3: I’m a doctor. (They pretend to check 2’s pulse.) They’re dead!
    - 1: NOOOOOOOOO!

    Then the class can give out suggestions for a style on how the scene should be done (western, telenovela, etc.) Switch out the performers as you see fit."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Beans, Beans, Beans", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G32(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Players stand in a circle. Facilitator stands in the center and gives one player a word. That player must then just empty their head in a stream of consciousness that is evoked from that word.  The player must never stop talking. Facilitator will then pick up a word from that student and give it to the next player to go on a stream of consciousness with."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Stream of Consciousness", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G33(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Ask five players to volunteer. Assign one player to be the “reader”, and the other four to be the “pop-up book”. Ask the class for a suggestion for the title of the book. Have the pop-up players laying on the ground, as if ink blots on the page. The reader opens the cover of the book and begins reading it. Whenever the reader flips a page, the four players “pop up” as if they were illustrations in the pop-up book. The reader must then “read” what is on the page, including the pop-ups into the evolving story. Occasionally the reader can go up to one of the pop-ups and ‘‘pull a tab’’ and the character goes into a simple action. Or the narrator “presses a button” and a character speaks a simple line of dialogue. The goal is for the story to have a complete beginning, middle and end."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Pop-Up Book", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G34(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Ask two players to take “the stage”. They must exchange dialogue in which the first word they speak must begin with the next letter of the alphabet, starting with whichever letter is elected and finishing at the letter just before. The conversation should make sense and propel action in the scene. It’s optional to give the players a given situation/scene beforehand."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Alphabet Conversation", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G35(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students become “experts” on certain subjects. Students take turns going in front of class. You or the audience give a subject that the student is expert in (i.e.. Cereal, Hairstyling, Fruit, Mexico, etc.) The student must talk about that subject expertly for one minute. They should be encouraged to not stop talking and to say whatever comes to mind no matter how absurd. The only rule is they can never stop talking."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Expert", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM2"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G36(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """2 players are chosen to go first. The facilitator or the class may give the two players a scenario, and then the two players must have a conversation in the context of the scenario using only questions. The first person to hesitate for too long or not use a question is eliminated, and a new player takes their place."""
        tk.Frame.__init__(self, parent, bg=ImprovisationColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=ImprovisationColor, text="Questions", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubIM2"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G37(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students stand in a circle. The facilitator starts off by demonstrating the beat of “We Will Rock You” (hit laps twice, clap once: lap, lap, clap) Once everyone has the rhythm down, the beat will keep going with everyone repeating it, and the facilitator will call on someone in the circle. The person called on (and only the person called on) must stop doing the rhythm. If they stop, they get to call on someone else. If they fail to stop, the round is over, and the person called on must choose a different rhythm to teach others. (If they cannot think of one, they can repeat WWRY.) The caller can also choose to yell “Everybody!” and at that point, everyone must cease doing the rhythm."""
        tk.Frame.__init__(self, parent, bg=RhythmColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=RhythmColor, text="We Will Shock You", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubRH"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G38(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Everyone stands in a circle. Everyone counts in the circle, 1, 2, 3, 1, 2, 3, etc. Once everyone has the hang of the counting rhythm, each “1” in the counting will be replaced with a snap. (snap, 2, 3, snap, 2, 3). Once they have a hang of that, replace the “2” with a clap (snap, clap, 3, snap, clap, 3.). Finally, the “3” will be replaced with a stomp. (snap, clap, stomp, snap, clap, stomp.) The game can then become an elimination one, where a new player starts the pattern each round and the others join in one at a time.  Once a player makes a mistake, they sit out. Play until there’s a final showdown between two remaining players (or call it a draw.)"""
        tk.Frame.__init__(self, parent, bg=RhythmColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=RhythmColor, text="Snap, Clap, Stomp", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubRH"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G39(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students stand in a circle, with one person in the middle. The person in the middle will close their eyes so the group can silently decide who starts off with the penny. Once it is decided, every player must have their left hand out, palms facing the ceiling with their fingers curled up as to hide their palms, and their fingers on their right hand bunched together in their left palm (as if using their right hand to pick up a penny from their left hand). The group must move their right hands from their left hands into the person next to them’s left hand, in sync while singing the song that goes along with it (below). While singing, the group must discreetly pass the penny throughout the circle. If the person in the center feels like they know who has the penny, they can say “Stop”, and everyone must stop what they’re doing. If the person guesses correctly, the one who got caught is now in the middle. If they guess incorrectly, the game (and song) resume. Play as long as desired.

    “Penny, Penny as you wander/ From one hand into another/ Is it fair, is it fair/ To leave poor [name of person in the middle] standing there? 
        “Penny, Penny as you wander/ From one hand into another/ Is it fair, is it fair/ To leave poor Amy standing there?"""
        tk.Frame.__init__(self, parent, bg=RhythmColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=RhythmColor, text="Penny, Penny", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubRH"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G40(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Players stand in a circle. Toss a bean bag or easy-to-catch ball back and forth around the circle. Let players know that it is the thrower’s responsibility to allow the catcher to catch it! Once a rhythm is established, introduce a “clap” every time the ball is in the air. All other players must clap in unison while the ball is in the air. Play until there is a nice rhythm and flow! For more advanced drama groups, introduce another ball into play."""
        tk.Frame.__init__(self, parent, bg=RhythmColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=RhythmColor, text="Catch & Clap", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubRH"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G41(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Everyone gets into a circle. This is a rhythm exercise. One person has a pen and passes it to the next person. While they are passing the pen, there is a dialogue going on between the person handing off the pen and the pen receiver. It goes: 
    
    - Hander: This is a pen. 
    - Receiver: A what? 
    - H: A pen.
    - R: A what?! 
    - H: A pen. 
    - R: Oh,a pen!

Then the pen gets passed on throughout the circle. You may add more pens as the exercise goes on."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="This is a Pen", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G42(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Participants are asked to line up in no particular order and count themselves off. Once everyone has a number, the group, still in line, must explore the space, following the person in front of them to maintain the numerical order. The facilitator is expected to call out any number from the group, and that individual is to lead the lot behind them. The facilitator can also use phrases such as "odd numbers' ' or "even numbers" to which the player with the respective numbers will lead the single person behind them. Lastly, the phrase "line up" is when players are expected to get back in their original order, quickly but safely. At some point in the game, the facilitator could direct groups to intersect without stopping or clashing with one another."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Watch Your Step", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G43(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Initially modeled by the teacher, this exercise asks participants to use pantomime skills and pull imaginary presents out of an imaginary box to get others to guess what the item may be. The actor can use or hold the imaginary item in different ways to help the guessers."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Magic Present", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G44(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The group is divided into two or more teams, with one person left over. The person not sorted into the group will be the guesser. The guesser is sent out of the room. The facilitator gives a word or prompt which the teams need to build using tableau in a limited amount of time (30-60 seconds). The guesser comes back in and attempts to guess the word. Once the guesser has arrived at the correct answer, they award a point to the team they found most helpful."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Tableau Olympics", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G45(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Each player stands in a circle. The facilitator tells everyone to look down. The facilitator says “1, 2, 3… Look” and on “Look” everyone must look up and directly at someone in the circle. If the person they are looking at is not looking back at them, they are “safe.” If both players are looking at each other, they must both scream “ahhh!” and fall to the ground (safely). The remaining players keep playing until there’s 1-2 players left standing."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="I Scream", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G46(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The number of students will be divided evenly into two lines. (If there is an uneven amount of students, the facilitator is encouraged to join in.) All members of each line must face the back area of the room/setting you’re in, except the first two people in each line, who will be facing each other. The first person must come up with a series of movements for the second person to watch and pass onto the next person. The person doing the movements may only repeat the sequence for the person watching once. After the repetition, the person must pass it to the next person behind them. Once it reaches the end of the line, the last person must do the sequence, then the first person does it to see how similar it was to the original. The line that had the most success in keeping the same movements is the winning team."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Pantomime Telephone", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G47(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Have everyone stand in a circle. After the instructions for the game are given, one person volunteers (or is chosen) to be the detective, and they will briefly leave the room. The people inside the circle must decide on one person to be “it”. The person who is “it” is tasked with doing movements that everyone in the group must copy at the same time. They must also continue to change the movements throughout the round. Once the person is decided and the movement starts, the facilitator may go get the detective from outside and join in on the movement. The detective’s job is to find out who started the movement, which is why it’s important for the movements to vary throughout the round. The detective typically gets 3 guesses."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Who Started the Motion", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G48(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Students stand at one side of the room, while one player (The Keeper) stands at the opposite side with their back to the other students. A set of keys is placed at their feet. When the Keeper says “Go”, the group can move toward the Keeper to try and get the keys. When the Keeper turns around, everyone must freeze. If the Keeper sees anyone “unfrozen”, that player must go back to the start. This continues until one player grabs the keys. This player now becomes the Keeper."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Keeper of the Keys", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI1"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G49(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """The students will divide into pairs. Each pair will be given a piece of paper as well as drawing tools for each of them. For a given amount of time, the students will take turns passing the paper back and forth and adding a new element (a shape, line, or words) to their drawing each time. At the end of the drawing period, the pairs will have an illustration that they will come up with a backstory for and present to the class."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Collaboration Creativity", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI2"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)

class G50(tk.Frame):

    def __init__(self, parent, controller):
        G_text = """Divide the class into groups of 3-4 students. Give all the groups a topic like “Your most embarrassing moment” or “A time you were really scared” or “Your favorite birthday party” etc. Have the students within the group share personal stories based on the topic. Tell each group to choose one story they are going to tell. Everyone in the group learns the story and tries to make it their own. Each person in the group tells the story to the class and the class tries to guess who the story really belongs to."""
        tk.Frame.__init__(self, parent, bg=MiscellaneousColor)
        self.controller = controller
        text_widget = scrolledtext.ScrolledText(self, height=ScrollBoxHeight, width=ScrollBoxWidth, font=controller.body_font, wrap='word')
        text_widget.insert(tk.END, G_text)
        text_widget.config(state=DISABLED)
        label = tk.Label(self, bg=MiscellaneousColor, text="Who's Telling the Truth?", font=controller.title_font)
        label.grid(row=0, columnspan=4, pady =10)
        back = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\arrow.png")
        buttonBack = tk.Button(self, image=back, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("SubMI2"))
        
        buttonBack.image = back
        home = PhotoImage(file=r"C:\Users\rylan_fnvcec4\iCloudDrive\Personal Projects\Game File\home.png")
        buttonHome = tk.Button(self, image=home, bg=BGButtonColor, relief=reliefType,
                           command=lambda: controller.show_frame("StartPage"))
        buttonHome.image = home
        
        text_widget.grid(row=1, columnspan=4, ipady=60)
        buttonBack.grid(row=0, column=0, pady=5)
        buttonHome.grid(row=0, column=3, pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()