from tkinter import* 
root=Tk()
root.geometry("500x500")
root.title("Image Viewer")
root.configure(background= "gray")

img_path= [""]

label_planet= Label(root, text= "planet: ", bg= "red")
label_planet_name= Label(root, font= ("courier",18,"bold"), bg= "yellow")
label_planet_image= Label(root, bg= "black", borderwidth= 2, 
                          highlightthickness= 5, relief= SOLID)
label_image["image"]= img
img_path= filedialog.askopenfilename(title= "Open Text File", filetypes=[("Image Files","*.jpg;*.gif;*.jpg;;*.png;;*txt")])
label_planet_gravity_radius= Label(root, font= ("courier",10,"bold"), bg= "orange")
label_planet_info= Label(root, font= ("courier",10,"bold"), bg="indigo",wraplength= 500 )

def open_info():
      print("hi")
      
btn= Button(root,text= "Open Image", command= planet_info )
btn.place(relx= 0.5, rely= 0.18, anchor=CENTER)

label_planet.place(relx= 0.5, rely= 0.1, anchor= CENTER)
label_planet_name.place(relx= 0.5, rely= 0.25, anchor= CENTER)
label_planet_image.place(relx= 0.5, rely= 0.5, anchor= CENTER)
label_planet_gravity_radius.place(relx= 0.5, rely= 0.8, anchor= CENTER)
label_planet_info.place(relx= 0.5, rely= 0.9, anchor= CENTER)


root.mainloop()



