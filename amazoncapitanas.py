from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class capitana:
	def __init__(self,a):
		self.a = a
		self.a.configure(bg='gray89')
		self.b = IntVar()
		self.bb=IntVar()
		self.bbb=IntVar()
		self.bbbb=IntVar()
		self.bbbbb=IntVar()
		self.bbbbbb=IntVar()
		self.bbbbbbb=IntVar()
		self.bbbbbbbb=IntVar()
		self.bbbbbbbbb=IntVar()
		self.c = IntVar()
		self.j=IntVar()
		self.k=IntVar()
		self.g=IntVar()
		self.e=IntVar()
		self.total = 0
		self.iva=0
		self.totalc=0
		self.d()
		

	

	def d(self):
	
	
		self.a.title("AMAZON")
		self.a.geometry("1600x700")
		self.foto=PhotoImage(file="teclado.png")
		self.fotoo=PhotoImage(file="mouse.png")
		self.fotooo=PhotoImage(file="audifonos.png")
		self.fotoooo=PhotoImage(file="luces.png")
		self.fotooooo=PhotoImage(file="forro.png")
		self.fotoooooo=PhotoImage(file="pulso.png")
		self.fotooooooo=PhotoImage(file="control.png")
		self.fotoooooooo=PhotoImage(file="play.png")
		self.fotooooooooo=PhotoImage(file="silla.png")
		self.amazon=PhotoImage(file="amazon.png")

		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=10,y=160) #p1
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=280,y=160) #p2
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=550,y=160) #p3

		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=10,y=360) #p4
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=280,y=360) #p5
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=550,y=360) #p6

		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=10,y=560) #p7
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=280,y=560) #p8
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='black').place(x=550,y=560) #p9
		Label(self.a,image=self.amazon,width=1600,height=29).place(x=0,y=5)
		
#PRECIOS
		Label(self.a,text="Teclado $COP 100000", foreground='black').place(x=130,y=60) #p1
		Label(self.a,text="Mouse $COP 200000", foreground='black').place(x=380,y=60) #p2
		Label(self.a,text="AirPods $COP 900000", foreground='black').place(x=650,y=60) #p3

		Label(self.a,text="Luces LED $COP 15000", foreground='black').place(x=100,y=260) #p4
		Label(self.a,text="Forro Iphone 13 $COP 25000", foreground='black').place(x=380,y=260) #p5
		Label(self.a,text=" Pulso Apple Watch Serie 6 $COP 50000", foreground='black').place(x=650,y=260) #p6

		Label(self.a,text="Control Xbox $COP 150000", foreground='black').place(x=100,y=460) #p7
		Label(self.a,text="Play Station 5 $COP 2000000", foreground='black').place(x=380,y=460) #p8
		Label(self.a,text="Silla Gamer $COP 250000", foreground='black').place(x=650,y=460) #p8

		Label(self.a,text="Total: ", foreground='royalblue4').place(x=890,y=290)
		Label(self.a,text="IVA: ", foreground='royalblue4').place(x=890,y=330)
		Label(self.a,text="Total con IVA: ", foreground='royalblue4').place(x=890,y=370)

		Label(self.a,text="Datos de compra ", foreground='royalblue4').place(x=890,y=410)
		Label(self.a,text="Nombre completo: ", foreground='royalblue4').place(x=890,y=450)
		Label(self.a,text="Cédula: ", foreground='royalblue4').place(x=890,y=490)
		Label(self.a,text="#Tarjeta: ", foreground='royalblue4').place(x=890,y=530)
		Label(self.a,text="CVV: ", foreground='royalblue4').place(x=890,y=570)
		Label(self.a,text="Dirección: ", foreground='royalblue4').place(x=890,y=610)
		Button(self.a,text="Finalizar compra",command=self.finalizar,bg="gold").place(x=890,y=650)	
		
	
#entrada cantidad de productos

		Entry(self.a,textvariable=self.b).place(x=10,y=180) #p1
		Entry(self.a,textvariable=self.bb).place(x=280,y=180) #p2
		Entry(self.a,textvariable=self.bbb).place(x=550,y=180) #p3

		Entry(self.a,textvariable=self.bbbb).place(x=10,y=380) #p4
		Entry(self.a,textvariable=self.bbbbb).place(x=280,y=380) #p5
		Entry(self.a,textvariable=self.bbbbbb).place(x=550,y=380) #p6


		Entry(self.a,textvariable=self.bbbbbbb).place(x=10,y=580) #p7
		Entry(self.a,textvariable=self.bbbbbbbb).place(x=280,y=580) #p8
		Entry(self.a,textvariable=self.bbbbbbbbb).place(x=550,y=580) #p9

#precios
		Entry(self.a,textvariable=self.c).place(x=970,y=290)
		Entry(self.a,textvariable=self.j).place(x=970,y=330)
		Entry(self.a,textvariable=self.k).place(x=990,y=370)

		#datos factura
		Entry(self.a).place(x=1010,y=450) 
		Entry(self.a).place(x=970,y=490) 
		Entry(self.a).place(x=970,y=530) 
		Entry(self.a).place(x=970,y=570) 
		Entry(self.a).place(x=970,y=610) 
	


	
		
#botones productos		
		Button(self.a,image=self.foto,width=100,height=80,command=self.agregarProducto1).place(x=10,y=60)
		Button(self.a,image=self.fotoo,width=80,height=80,command=self.agregarProducto2).place(x=280,y=60)
		Button(self.a,image=self.fotooo,width=80,height=80,command=self.agregarProducto3).place(x=550,y=60)

		Button(self.a,image=self.fotoooo,width=80,height=80,command=self.agregarProducto4).place(x=10,y=260)
		Button(self.a,image=self.fotooooo,width=80,height=80,command=self.agregarProducto5).place(x=280,y=260)
		Button(self.a,image=self.fotoooooo,width=80,height=80,command=self.agregarProducto6).place(x=550,y=260)		

		Button(self.a,image=self.fotooooooo,width=80,height=80,command=self.agregarProducto7).place(x=10,y=460)
		Button(self.a,image=self.fotoooooooo,width=80,height=80,command=self.agregarProducto8).place(x=280,y=460)
		Button(self.a,image=self.fotooooooooo,width=80,height=80,command=self.agregarProducto9).place(x=550,y=460)		



		self.tabla = ttk.Treeview(self.a,columns=("Cantidad","Importe"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Importe",text="Importe" )
		self.tabla.place(x=890,y=40)

	def agregarProducto1(self):
		producto = 'Teclado'
		precio = 100000
		cantidad = self.b.get()
		importe = int(precio)*int(cantidad)
		
		
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))


	def agregarProducto2(self):
		
	
		producto = 'Mouse'
		precio = 200000
		cantidad = self.bb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))
		

	def agregarProducto3(self):
		
	
		producto = 'Audífonos'
		precio = 900000
		cantidad = self.bbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))
		
	

	def agregarProducto4(self):
		
	
		producto = 'Luces LED'
		precio = 15000
		cantidad = self.bbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))
		
		

	def agregarProducto5(self):
		
	
		producto = 'Forro Iphone 13'
		precio = 25000
		cantidad = self.bbbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))


	def agregarProducto6(self):
		
	
		producto = 'Pulso Apple Watch Serie 6'
		precio = 50000
		cantidad = self.bbbbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))
		
	def agregarProducto7(self):
		
	
		producto = 'Control'
		precio = 150000
		cantidad = self.bbbbbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))		

	def agregarProducto8(self):
		
	
		producto = 'Play Station 5'
		precio = 2000000
		cantidad = self.bbbbbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))	

	def agregarProducto9(self):
		
	
		producto = 'Silla Gamer'
		precio = 250000
		cantidad = self.bbbbbbbb.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))	

	def finalizar(self):
		messagebox.showinfo("","La compra se despachará en 10 a 15 días hábiles, gracias :)")	

obj = capitana(Tk())
obj.a.resizable(width=False, height=False)
obj.a.mainloop()
