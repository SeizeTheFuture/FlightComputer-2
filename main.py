import tkinter as tk
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256
GRAPH_WIDTH = 400
GRAPH_HEIGHT = 388

FONT = ("Courier", 40, "bold")

#Create the main window and image objects
window = tk.Tk()
window.title("Flight Computer")
window.config(padx = 100, pady = 100, bg="gray")
plane_image = tk.PhotoImage(file="airplane.png")
graph_image = tk.PhotoImage(file="cessna172graph.png")

def cessna172_window():
  #Set up second window for Cessna 172 calculations
  window2 = tk.Toplevel()
  window2.title("Weight and Balance Calculator")
  window2.config(padx = 100, pady = 50, bg = "light blue")
  window2.geometry("725x625")

  def calculate():
    #Calculate total weight and display it on screen
    empty_plane_weight = empty_plane_var.get()
    fuel_weight = fuel_var.get()
    front_seats_weight = front_seats_var.get()
    rear_seats_weight = rear_seats_var.get()
    baggage1_weight = baggage1_var.get()
    baggage2_weight = baggage2_var.get()
    
    total_weight = empty_plane_weight + fuel_weight + front_seats_weight\
    + rear_seats_weight + baggage1_weight + baggage2_weight
    total_weight_value.config(text=f"{total_weight}")

    #Calculate each moment, then total moment, and display it on screen
    empty_plane_moment = empty_plane_weight * empty_plane_arm
    fuel_moment = fuel_weight * fuel_arm
    front_seats_moment = front_seats_weight * front_seats_arm
    rear_seats_moment = rear_seats_weight * rear_seats_arm
    baggage1_moment = baggage1_weight * baggage1_arm
    baggage2_moment = baggage2_weight * baggage2_arm
    total_moment = empty_plane_moment + fuel_moment+ front_seats_moment + rear_seats_moment \
    + baggage1_moment + baggage2_moment
    total_moment_value.configure(text=str(total_moment))

    #Calculate the CG 
    try:
      cg = total_moment/total_weight
    except ZeroDivisionError:
      print("You can't divide by zero!")
      cg = 0

    #Format the CG to two decimal places
    formatted_cg = "{:.2f}".format(cg)

    #Display CG on screen
    cg_value.configure(text=formatted_cg)

    #Create a button to check if it's safe to fly
    flight_check = tk.Button(window2, text="Check Flight Safety",\
                             command= lambda: check_cg(total_moment, total_weight))
    flight_check.grid(pady = 25, row = 11, column = 1)
    
  #Create and grid labels for weight and arm columns
  weight_label = tk.Label(window2, text = "Weight", bg = "light blue")
  weight_label.grid(row=0, column=1)
  arm_label = tk.Label(window2, text = "Arm", bg = "light blue")
  arm_label.grid(padx = 10, row=0, column= 2)

  #Create labels for parts of plane
  empty_plane_label = tk.Label(window2, text = "Empty Plane: ", bg = "light blue")
  empty_plane_label.grid(row=1, column=0)
  fuel_label = tk.Label(window2, text = "Usable Fuel: ", bg = "light blue")
  fuel_label.grid(row=2, column=0)
  front_seats_label = tk.Label(window2, text = "Front Seats: ", bg = "light blue")
  front_seats_label.grid(row=3, column = 0)
  rear_seats_label = tk.Label(window2, text = "Rear Seats: ", bg = "light blue")
  rear_seats_label.grid(row=4, column = 0)
  baggage1_label = tk.Label(window2, text = "Baggage Area 1: ", bg = "light blue")
  baggage1_label.grid(row=5, column = 0)
  baggage2_label = tk.Label(window2, text = "Baggage Area 2: ", bg = "light blue")
  baggage2_label.grid(row=6, column = 0)
  

  #Create varaibles to store weight inputs
  empty_plane_var = tk.IntVar()
  empty_plane_var.set(1454)
  fuel_var = tk.IntVar()
  front_seats_var = tk.IntVar()
  rear_seats_var = tk.IntVar()
  baggage1_var = tk.IntVar()
  baggage2_var = tk.IntVar()
  
  #Create and grid entry fields
  empty_plane_field = tk.Entry(window2, textvariable= empty_plane_var)
  empty_plane_field.grid(row=1, column=1)
  fuel_field = tk.Entry(window2, textvariable= fuel_var)
  fuel_field.grid(row=2,column=1)
  front_seats_field = tk.Entry(window2, textvariable= front_seats_var)
  front_seats_field.grid(row=3, column=1)
  rear_seats_field = tk.Entry(window2, textvariable= rear_seats_var)
  rear_seats_field.grid(row=4, column=1)
  baggage1_field = tk.Entry(window2, textvariable= baggage1_var)
  baggage1_field.grid(row=5, column=1)
  baggage2_field = tk.Entry(window2, textvariable= baggage2_var)
  baggage2_field.grid(row=6, column=1)
  
  #Create the arm values, labels, and grid them
  empty_plane_arm = 39.6
  fuel_arm = 48
  front_seats_arm = 37
  rear_seats_arm = 73
  baggage1_arm = 95
  baggage2_arm = 123
  
  empty_plane_arm_label = tk.Label(window2, text=str(empty_plane_arm), bg= "light blue")
  empty_plane_arm_label.grid(row=1, column=2)
  fuel_arm_label = tk.Label(window2, text=str(fuel_arm), bg= "light blue")
  fuel_arm_label.grid(row=2, column=2)
  front_seats_arm_label = tk.Label(window2, text=str(front_seats_arm), bg= "light blue")
  front_seats_arm_label.grid(row=3, column=2)
  rear_seats_arm_label = tk.Label(window2, text=str(rear_seats_arm), bg= "light blue")
  rear_seats_arm_label.grid(row=4, column=2)
  baggage1_arm_label = tk.Label(window2, text=str(baggage1_arm), bg= "light blue")
  baggage1_arm_label.grid(row=5, column=2)
  baggage2_arm_label = tk.Label(window2, text=str(baggage2_arm), bg= "light blue")
  baggage2_arm_label.grid(row=6, column=2)
  
  #Create and grid calculate button
  calculate_button = tk.Button(window2, text = "Calculate", command=calculate)
  calculate_button.grid(pady = 25, row=7,column=1)

  #Create and grid the total weight, total moment and CG labels
  total_weight_label = tk.Label(window2,text="Total Weight: ", bg = "light blue")
  total_weight_label.grid(row=8, column=0)
  total_moment_label = tk.Label(window2,text="Total Moment: ", bg = "light blue")
  total_moment_label.grid(row=9, column=0)
  cg_label = tk.Label(window2,text="Center of Gravity: ", bg = "light blue")
  cg_label.grid(row=10, column=0)

  #Create and grid the total weight, total moment, and CG values
  total_weight_value = tk.Label(window2, text="0", bg = "light blue")
  total_weight_value.grid(row=8, column=1)
  total_moment_value = tk.Label(window2, text="0", bg = "light blue")
  total_moment_value.grid(row=9, column=1)
  cg_value = tk.Label(window2, text="0", bg = "light blue")
  cg_value.grid(row=10, column=1)

def check_cg(moment, weight):
  point = Point(moment, weight)
  polygon = Polygon([(52000, 1500), (68000, 1960), (88000, 2300), (109000, 2300), (70000, 1500)])
  window3 = tk.Toplevel(bg="light green")
  window3.title("Flight Check")
  window3.config(padx= 100, pady= 100)
  
  if (polygon.contains(point)):
    safe_flight_label = tk.Label(window3, text="Safe to Fly!", font=FONT, bg="light green")
    safe_flight_label.grid(row=0, column=1)
    cg_canvas = tk.Canvas(window3, width=GRAPH_WIDTH, height=GRAPH_HEIGHT,\
                          bg = "light green", highlightthickness = 0)
    cg_canvas.grid(row=1, column= 1)
    cg_canvas.create_image(GRAPH_WIDTH/2, GRAPH_HEIGHT/2, image=graph_image)
  else:
    window3.config(bg="red")
    unsafe_flight_label = tk.Label(window3, text="Don't Fly!", font=FONT, bg="red")
    unsafe_flight_label.grid(row=0, column=1)
    cg_canvas = tk.Canvas(window3, width=GRAPH_WIDTH, height=GRAPH_HEIGHT,\
                          bg = "red", highlightthickness = 0)
    cg_canvas.grid(row=1, column= 1)
    cg_canvas.create_image(GRAPH_WIDTH/2, GRAPH_HEIGHT/2, image=graph_image)

#Finish setting up the main window
canvas = tk.Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "gray", highlightthickness = 0)
canvas.grid(row=1, column=1)
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=plane_image)
header = tk.Label(text="Flight Computer", font=FONT, fg="blue", bg = "gray")
header.grid(row=0, column=1)
weight_balance_button = tk.Button(text="Cessna 172 Weight and Balance", command=cessna172_window)
weight_balance_button.grid(row=2,column=1)
window.mainloop()