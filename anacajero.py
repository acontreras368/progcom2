from tkinter import *
from tkinter import ttk

class capitana:
	def __init__(self,a):
		self.a = a
		self.a.configure(bg='plum1')
		self.productos = ("Galletas OREO p1000","Galletas festival p2000","Papas receta clásica p2500","Papas de limón p2500","De todito picante p3000","De todito criollo p3000","H2OH p2500","Coca-Cola p3000","Mrs TEA p3000","Platanitos p2000","Natucips dulces p2000","Gomitas de aro p2500","Gomitas de gusanito p2500","Gomitas de fresa p2500","Choclitos p1000","M&M p4000","Snicker p5000","Chocolatina jet p1000","Chocolatina jet con mani p2500","Chocolatina burbujet p3000")
		self.b = IntVar()
		self.c = IntVar()
		self.j=IntVar()
		self.k=IntVar()
		self.g=IntVar()
		self.e=IntVar()
		self.total = 0
		self.iva=0
		self.totalc=0
		self.usa=0
		self.eur=0
		self.d()
	def d(self):
		self.foto= PhotoImage(file="cap3.png")

		
		self.a.title("Toti's Market")
		self.a.geometry("650x650")
		Label(self.a,text="Toti's Market" , foreground='deep pink').place(x=10,y=20)
		Label(self.a,text="Producto a comprar", foreground='magenta1').place(x=10,y=45)
		Label(self.a,text="Digita la cantidad que deseas llevar", foreground='magenta1').place(x=10,y=96)
		Label(self.a,text="Total: ", foreground='magenta1').place(x=470,y=390)
		Label(self.a,text="IVA: ", foreground='magenta1').place(x=470,y=430)
		Label(self.a,text="Total con IVA: ", foreground='magenta1').place(x=430,y=470)
		Label(self.a,text="Total en dólares: ", foreground='magenta1').place(x=420,y=510)
		Label(self.a,text="Total en euros: ", foreground='magenta1').place(x=430,y=550)
		self.combo = ttk.Combobox(self.a,state="")
		self.combo.place(x=10,y=70)
		self.combo["values"]=self.productos
		self.combo.current(0)
		Entry(self.a,textvariable=self.b).place(x=10,y=120)
		Entry(self.a,textvariable=self.c).place(x=520,y=390)
		Entry(self.a,textvariable=self.j).place(x=520,y=430)
		Entry(self.a,textvariable=self.k).place(x=520,y=470)
		Entry(self.a,textvariable=self.g).place(x=520,y=510)
		Entry(self.a,textvariable=self.e).place(x=520,y=550)
		Button(self.a,image=self.foto,width=70,height=70,command=self.agregarProducto).place(x=300,y=40)
		self.tabla = ttk.Treeview(self.a,columns=("Cantidad","Importe"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Importe",text="Importe" )
		self.tabla.place(x=10,y=150)
	def agregarProducto(self):
		texto = self.combo.get()  
		datos = texto.split("p")
		producto = datos[0]
		precio = datos[1]
		cantidad = self.b.get()
		importe = int(precio)*int(cantidad)
		

		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(importe)))
		self.total = self.total + importe
		self.c.set("$"+str(self.total))

		self.iva=self.total*0.19
		self.j.set("$"+str(self.iva))

		self.totalc=self.iva+self.total
		self.k.set("$"+str(self.totalc))
		
		self.usa=self.totalc*0.00021
		round(self.usa, 2)
		self.g.set("USD$"+str(self.usa))

		self.eur=self.totalc*0.00021
		round(self.eur, 2)
		self.e.set("€"+str(self.eur))


		
obj = capitana(Tk())
obj.a.resizable(width=False, height=False)
obj.a.mainloop()
