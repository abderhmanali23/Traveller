from tsp import main_tsp
from bestRoad import main_bestRoad
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import ttk
from tkinter import messagebox
import numpy as np

Cities = ['Port Said', 'Sohag', 'Suez', 'Red Sea', 'Luxor', 'Beni Suef', 'Kafr El Sheikh', 'Dakahlia', 'Helwan', 'Aswan', 'Faiyum', 'Gharbia', 'South Sinai', 'Monufia', 'Matrouh', 'Qalyubia', 'Sharqia', 'Qena', 'Beheira', 'Alexandria', 'Damietta', 'Cairo', 'Giza', 'Asyut', 'North Sinai', 'New Valley', 'Ismailia', 'Minya']


points = {
        'Port Said': (434, 54),
        'Sohag': (429, 332),
        'Suez': (455, 120),
        'Red Sea': (519, 362),
        'Luxor': (464, 396),
        'Beni Suef': (361, 188),
        'Kafr El Sheikh': (361, 42),
        'Dakahlia': (393, 57),
        'Helwan': (392, 150),
        'Aswan': (464, 482),
        'Faiyum': (346, 167),
        'Gharbia': (363, 69),
        'South Sinai': (520, 188),
        'Monufia': (363, 87),
        'Matrouh': (170, 126),
        'Qalyubia': (376, 107),
        'Sharqia': (400, 81),
        'Qena': (474, 358),
        'Beheira': (328, 73),
        'Alexandria': (284, 60),
        'Damietta': (396, 36),
        'Cairo': (389, 122),
        'Giza': (358, 121),
        'Asyut': (404, 287),
        'North Sinai': (508, 98),
        'New Valley': (239, 404),
        'Ismailia': (438, 96),
        'Minya': (355, 237)
}

def random_cities():

    global welcome, decesion, specified, rand, choose_label, choose, proc
    welcome.destroy()
    decesion.destroy()
    specified.destroy()
    rand.destroy()

    choose_label = Label(root, text="Enter your budget: ",fg="black",bg="#ddcfe8", padx=20,pady=40, font=("Arial",20,"bold"))
    choose = Entry(root, width=20, relief="flat")

    choose_label.pack(anchor=NW, side='left')
    choose.pack(anchor=W, pady=50, padx=10, side='top')

    proc = Button(root,text="Proceed",width=10,padx=20, background="red",fg="white",relief="flat",activebackground="#a10e15",activeforeground="#dfdfe6",overrelief="groove", height=1, font=("Arial",11,"bold"), command= lambda: plotting_random(int(choose.get())))
    proc.pack(anchor=NW, padx=30)

def plot_window(best_road, cost):

    image_path = 'Egypt.png'
    image = mpimg.imread(image_path)


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))


    ax1.imshow(image)

    ax1.set_title('Egypt')
    ax1.set_xlabel('X Label')
    ax1.set_ylabel('Y Label')

    x, y = [points[i][0] for i in best_road], [points[i][1] for i in best_road]

    colors = plt.cm.viridis(np.linspace(0, 1, len(x)))

    for i in range(len(x) - 1):
        ax1.plot(x[i:i+2], y[i:i+2], color=colors[i])

    ax1.scatter(x, y, c=colors, cmap='viridis')

    text = []
    for i in range(len(x)):
        if i == 0:
            s = [f"-", best_road[i]]
        
        else:
            s = [best_road[i - 1], best_road[i]]
            

        text.append(s)

    text.append(["Total cost", cost])
    ax2.axis('off')
    table = ax2.table(cellText=text, colLabels=['Start Point', 'Destination'], cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.tight_layout()
    plt.show()


def ploting_specified():
    
    global check_boxes, start_choice, variables
    selected = []
    for ind, city in enumerate(variables):
        if city.get():
            selected.append(Cities[ind])

    best_road, cost = main_tsp(selected, start_choice.get())
    plot_window(best_road, cost)

def plotting_random(budget):

    global choose, choose_label, proc
    result = main_bestRoad(budget)
    if type(result) is str:
        messagebox.showerror("Error", "budget is low")

    
    else:

        choose.destroy()
        choose_label.destroy()
        proc.destroy()

        canvas = Canvas(root, borderwidth=0, highlightthickness=1,background="#ddcfe8", highlightbackground="#ddcfe8", width = 780, height = 430)
        canvas.grid(row=0, column=0, sticky='nsew')

        yscrollbar = Scrollbar(root, orient='vertical', command=canvas.yview)
        yscrollbar.grid(row=0, column=1, sticky='ns')

        table_frame = Frame(canvas, bg="#ddcfe8")
        table_frame.grid(row=0, column=0, sticky='nsew')

        for i, header in enumerate(["Number of Cities", "cost", "Map"]):
            label = Label(table_frame,pady=5, text=header, borderwidth=1, relief='solid', highlightbackground="#ddcfe8",background="#ddcfe8",foreground="black",highlightcolor="black",highlightthickness=1,font=("Arial",10,"bold"), width=35)
            if i == 2:
                label.configure(width=25)
            label.grid(row=0, column=i, sticky='nsew')

        
        for i, row in enumerate(result):

            label = Label(table_frame,pady=8, text=str(len(row[0]) - 1), borderwidth=1, relief='solid', highlightbackground="#ddcfe8",background="#ddcfe8",foreground="black",highlightcolor="black",highlightthickness=1,font=("Arial",10,"bold"), width=35)
            label.grid(row=i+1, column=0)

            label2 = Label(table_frame,pady=8, text=str(row[1]), borderwidth=1, relief='solid', highlightbackground="#ddcfe8",background="#ddcfe8",foreground="black",highlightcolor="black",highlightthickness=1,font=("Arial",10,"bold"), width=35)
            label2.grid(row=i+1, column=1)
            
            fun = lambda r=row: plot_window(r[0], str(r[1]))
            showbutton = Button(table_frame,text="Show",width=15,padx=20, background="red",fg="white",relief="flat",activebackground="#a10e15",activeforeground="black",overrelief="groove", height=1, font=("Arial",10,"bold"), command= fun, borderwidth=1, highlightthickness=1)
            showbutton.grid(row=i+1, column=2)
        
        canvas.create_window((0,0), window=table_frame)
        table_frame.update_idletasks()            
        canvas.config(scrollregion=canvas.bbox('all'),  yscrollcommand=yscrollbar.set)
        yscrollbar.config(command=canvas.yview)
        canvas.yview_moveto(0)


def specified_cities():

    global welcome, decesion, specified, rand, start_choice, check_boxes, variables
    welcome.destroy()
    decesion.destroy()
    specified.destroy()
    rand.destroy()

    choose_label = Label(root, text="Please choose the cities you want to visit. ",fg="black",bg="#ddcfe8", padx=20,pady=30, font=("Arial",20,"bold"))
    choose_label.grid(row=0, column=0, columnspan=4, sticky='w')

    start_label = Label(root, text="Choose the start destination: ",fg="black",bg="#ddcfe8", padx=20,pady=10, font=("Arial",14,"bold"))
    start_label.grid(row=1, column=0, columnspan=2)


    start_choice = ttk.Combobox(root, values=Cities)
    start_choice.grid(row=1, column=2)
    check_boxes = []
    variables = []

    table_frame = Frame(root, bg="#ddcfe8", pady=20, padx=30)
    table_frame.grid(row=2, column=0, sticky='nsew', columnspan=4)

    row = 0
    column = 0
    for i in Cities:

        var = BooleanVar(root)
        check_box = Checkbutton(table_frame, text=i+'', background="#ddcfe8", padx=20, activebackground="#ddcfe8", variable=var )
        
        variables.append(var)
        check_boxes.append(check_box)
        
        if column % 5 == 0:
            row += 1; column = 0
        
        check_box.grid(row=row, column=column, sticky="w")

        column += 1
        
    proc2 = Button(root,text="Proceed",width=10,padx=20, background="red",fg="white",relief="flat",activebackground="#a10e15",activeforeground="#dfdfe6",overrelief="groove", height=1, font=("Arial",11,"bold"), command=ploting_specified)
    proc2.grid(row = row + 1, column= 1, pady = 30, columnspan=2)   



root = Tk()
root.geometry("800x430+300+300")
root.resizable(False,False)
root.title('Traveller')
root.configure(background="#ddcfe8")

welcome = Label(root, text="Welcome to our travelling system.",fg="black",bg="#ddcfe8", padx=20,pady=40, font=("Arial",20,"bold"))
welcome.pack(anchor=NW)

decesion = Label(root, text="Do you want travelling to a specified cities or random cities depending on your budget?",fg="black",bg="#ddcfe8", padx=20,pady=10, font=("Arial",13,"bold"))
decesion.pack(anchor=NW)

specified = Button(root,text="Specified Cities",width=10,padx=30, background="red",fg="white",relief="flat",activebackground="#a10e15",activeforeground="#dfdfe6",overrelief="groove", height=2, font=("Arial",11,"bold"), command=specified_cities)
specified.pack(side="right", padx=100)

rand = Button(root,text="Random Cities",width=10,padx=30, background="green",fg="white",relief="flat",activebackground="green",activeforeground="#dfdfe6",overrelief="groove", height=2, font=("Arial",11,"bold"), command=random_cities)
rand.pack(side="left", padx=100)

root.mainloop()