from tkinter import *
import tkinter


raiz = Tk() 
raiz.title("Lab1") #Cambiar el nombre de la ventana 
raiz.geometry("800x700") #Configurar tamaño
raiz.config(bg="misty rose") #Cambiar color de fondo
raiz.resizable(0,0)

Label(raiz, text="\n " , bg="misty rose").pack()
Label(raiz, text="Informe de laboratorio 1: Ecuaciones Empíricas \n" , bg="misty rose").pack()
img = tkinter.PhotoImage(file= "informe1.png")
Label_img= tkinter.Label(raiz, image=img)
Label_img.pack()


Label(raiz, text="Autores: \n  Javier Andrés García Sánchez \n Andrés Eduardo Cristancho Rincón \n Ana Sofía de los Ángeles Contreras Rivera \n \n Laboratorio de mecánica \n  \n Docente: Dudbil Olvasada Pabon Riaño \n \n Universidad Autónoma de Bucaramanga UNAB", bg="misty rose").pack()



  
def openNewWindow(): 
      
    
    
    newWindow = Toplevel(raiz) 
  
    
    
    newWindow.title("Resumen introducción") 
  
    
    newWindow.geometry("800x400") 
    newWindow.config(bg="misty rose") #Cambiar color de fondo
    newWindow.resizable(0,0)
  
    Label(newWindow, text="\n " , bg="misty rose").pack()
    Label(newWindow,  text = "Resumen \n " , bg="misty rose").pack() 
    
    Label(newWindow,  text =  "El siguiente artículo compara la ecuación teórica para el periodo de un péndulo con una ecuación obtenida experimentalmente \n tras analizar el comportamiento de oscilación de una sexta de anillos, \n a los cuales se les midió sus diámetros (internos y externos), \n masas y periodos de oscilación por medio de herramientas tales como un calibrador, una balanza y unos sensores infrarrojos, respectivamente. \n Los resultados muestran una relación directamente proporcional comparando el periodo con el diámetro medio \n y la masa, teniendo en cuenta que a mayor peso y diámetro medio del anillo, mayor será su período. \n Además, se presenta una variación en la oscilación del último anillo, originada por error humano, \n que causa una desviación en la ecuación experimental. \n \n", bg="misty rose").pack() 
    Label(newWindow, text="Introducción \n" , bg="misty rose").pack()
    Label(newWindow, text="La física es una ciencia teórica y experimental, mediante el campo experimental se logran estudiar fenómenos físicos y naturales, \n  al realizar prácticas de laboratorio se extraen valores a los que se les asigna el nombre de variables (dependientes o independientes) \n por medio de ecuaciones empíricas el factor de dependencia entre variables se puede denotar como una función. \n El objetivo de esta práctica de laboratorio es indagar acerca de la relación que tienen las variables masa y dimensión, \n  con el periodo de oscilación de un anillo, \n y comparar los resultados obtenidos con la ecuación teórica para el periodo de un anillo oscilante. \n  ", bg="misty rose").pack()
btn = Button(raiz,  
             text ="Click aquí para ver el resumen e introducción",  
             command = openNewWindow,bg="wheat1") 
btn.pack(pady = 10) 

def openNewWindow2(): 
      
    
    
    newWindow2 = Toplevel(raiz) 
  
    
    Label(raiz, text="\n " , bg="misty rose").pack()
    newWindow2.title("Desarrollo experimental y resultados") 
  
    
    newWindow2.geometry("800x800") 
    newWindow2.config(bg="misty rose") #Cambiar color de fondo
    newWindow2.resizable(0,0)
  
    Label(newWindow2, text="\n " , bg="misty rose").pack()
    Label(newWindow2,  text = "Desarrollo experimental \n " , bg="misty rose").pack() 
   
    Label(newWindow2,  text =  "Primero, se realizaron las mediciones en torno al anillo dado por el docente (las mediciones fueron: masa, diámetro interno y externo) \n utilizando la balanza y vernier. \n Posteriormente se seleccionó una varilla corta para introducir el anillo, \n mediante el Módulo de adquisición de datos CASSY LAB se logró obtener el periodo que tardó el anillo en oscilar cuando fue soltado, \n fue repetido tres veces para lograr una mayor precisión en los datos. \n Finalmente, cuando ya se habían tomado todos los datos, se procedió a tabular y graficar. \n \n", bg="misty rose").pack() 
    Label(newWindow2, text="Resultados \n" , bg="misty rose").pack()
    Label(newWindow2, text="El período, masa y diámetro de un anillo oscilante son directamente proporcionales. \n Si una de estas magnitudes aumenta, las otras también aumentan. \n El error humano en la toma de mediciones y datos cambia por unas décimas los valores de las variables. \n Esta diferencia puede dar lugar a discrepancias en los resultados entre las ecuaciones ideales o teóricas y las ecuaciones experimentales. \n En el peor de los casos, esta variación dificulta la interpretación de los datos debido a resultados completamente distintos a lo que cabría esperar. \n Sólo unas cuantas décimas de diferencia son capaces de alterar todo un resultado. \n De ahí, la gran importancia por manejar bien las cifras significativas de los datos en una investigación, pues, a la larga, arrojan diferencias significativas.\n \n", bg="misty rose").pack() 
    img = tkinter.PhotoImage(file= "informe2.png")
    Label_img= tkinter.Label(newWindow2, image=img)
    Label_img.pack()


btn2 = Button(raiz,  
             text ="Click aquí para ver el desarrollo experimental y resultados",  
             command = openNewWindow2,bg="wheat1") 
btn2.pack(pady = 10) 





raiz.mainloop() 