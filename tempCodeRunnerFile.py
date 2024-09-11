    #convert image one color space to another
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred_img = cv2.GaussianBlur(converted_img, (25, 25), 300, 300)
    
    
    img_to_pencil = cv2.divide(converted_img, blurred_img, scale = scale_value)
    
    cv2.imwrite('saved_img.png', img_to_pencil) 
    
    img = Image.open('saved_img.png')
    img = img.resize((110, 200)) 
    img = ImageTk.PhotoImage(img)
    
    l_image = Label(window, image = img, bg=c0, fg=c1)
    l_image.place(x=60, y=60)
    
stlye = ttk.Style(window)
stlye.theme_use("clam")

app_img = Image.open("image.jpg")
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)