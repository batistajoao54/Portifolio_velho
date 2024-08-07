from tkinter import *
from tkinter import ttk


def ver():
    cima_c1 = ['2','180','121','120','109','104','107','13','183','105',
            '176','7','194','132','9','163','101','126','119','118',
            '117','125','218']

    cima_c2 = [ 
        '154','193','202','201','187','123','185','5','205','164','139','211','141',
        '50','51','138','168','165','151','124','216','149','54','156','216','137',
        '212','140','148','144','146','136','162','217'
    ]

    parede = [
        '57','166','145','197','55','158','172','159','173','142','147','174','60','61',
        '170','169','198','62','157','209','153','160','175','64','171','127b','167'
    ]

    baixo_c1 = [
        '106','luciano','14','130','131','186','108','112','190','200','116','129',
        '3','8','210','127a','133','219','182'
    ]

    baixo_c2 = [
        '10','134','135','58','59','16','111','110','192','196','189','102',
        '181','115','17','114','203','214','195','188','199'
    ]

    estante_baixo = [
        '207','103','6','113','208','204','128','122','52','152','155','200',
        '4','191','150','215','213','143','199b','206','161',
    ]

    parede_interna = [
        '228','223b','225','222','226','227','223','224','229','230',
        '231','232','233','234','235','236','237','238','239','240',
        '241','242','243','244','245','246','247','248','249','250',
        '251','252','253','254','255','256','257','258','259','260',
        '261','263','263','264','265','266','267','268','269','270',
        '271','272','273','274','275','276','277','278','279','280',
        '281','282','283','284','285','286','287','288','289','290',
        '291','292','293','294','295','296','297','298','299','300',
    ]

    matriz = nomeEntry.get()

    if matriz in cima_c1:
        faca = Label(inicio,text="                                    ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Cima na coluna1", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    elif matriz in cima_c2:
        faca = Label(inicio,text="                                     ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Cima na coluna2", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    elif matriz in parede:
        faca = Label(inicio,text="                                     ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Parede", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)

    elif matriz in baixo_c1:
        faca = Label(inicio,text="                                     ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Embaixo na coluna1", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    elif matriz in baixo_c2:
        faca = Label(inicio,text="                                     ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Embaixo na coluna2", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    elif matriz in estante_baixo:
        faca = Label(inicio,text="                                  ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Embaixo na estante", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    elif matriz in parede_interna:    
        faca = Label(inicio,text="                                      ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Na parede interna", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
    
    else:   
        faca = Label(inicio,text="                                     ", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)
        faca = Label(inicio,text="Não localizada", fg='#FF0000',font='verdana 16', bg='#FFFFE0')
        faca.place(x=10, y=50)



#criando janela
inicio = Tk()
inicio.config(bg='#FFFFE0')
inicio.title('MATRIZ')

width = 300
heigth = 100
tela_largura = inicio.winfo_screenwidth()
tela_altura = inicio.winfo_screenheight()
x = (tela_largura / 2) - (width /2)
y = (tela_altura /4) - (heigth /4)
inicio.geometry('%dx%d+%d+%d' % (width, heigth, x, y))
inicio.resizable(0,0)


#
nome = Label(inicio, text="MATRIZ: ", font='verdana 16', bg='#FFFFE0')
nome.place(x=10,y=10)
nomeEntry = ttk.Entry(inicio, width=8,font='verdana 16')
nomeEntry.place(x=110,y=10)

botaoadicionar = Button(inicio,text="VER",bg='#000000',font='verdana 9',fg='#FFFF00',width=6,height=1,relief='flat',command=ver)
botaoadicionar.place(x=230,y=12)

botaoadicionar.bind('<Return>', lambda event, b=botaoadicionar: b.invoke())



inicio.mainloop()
