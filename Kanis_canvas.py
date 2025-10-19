from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

rel_dir = os.path.dirname(os.path.abspath(__file__))


wynik_ok = 'OK'
wynik_niski = 'ZA NISKI'
wyniki_wysoki = 'ZA WYSOKI'
brak_badania = 'NIE BADANO'

#------- wymiary A4 w mm
pdf_w,pdf_h = A4
#----- LOGO CANIS
canis_logo = '{}\\canis_logo.png'.format(rel_dir)
font_path = '{}\\FreeSans.ttf'.format(rel_dir)
fontBold_path = '{}\\FreeSansBold.ttf'.format(rel_dir)
save_path = '{}\\Wyniki'.format(rel_dir)
#raport  = canvas.Canvas('Hello.pdf', pagesize=A4)
pdfmetrics.registerFont(TTFont('FreeSans', font_path))
pdfmetrics.registerFont(TTFont('FreeSansBold', fontBold_path))

class diag_canvas():
    def __init__(self, docname: str, raport_date: str, nr_zlecenia='', gatunek='', wlasciciel='', nazwa='', 
                ast_wynik='', alt_wynik='', alp_wynik='', bilirubina_wynik='',ggt_wynik='',ldh_wynik='',cholesterol_wynik='',triglicerydy_wynik='',kw_zolt_wynik='',bialko_wynik='',
                albuminy_wynik='',glukoza_wynik='',fruktozamina_wynik='',mocznik_wynik='', kreatynina_wynik='',kinaza_wynik='',amylaza_wynik='',lipaza_wynik='', wapn_wynik='',fosfor_wynik='',
                magnez_wynik='',zelazo_wynik='',potas_wynik='',sod_wynik='',chlorki_wynik='',uwagi='brak'):
        self.docname = docname
        self.raport_date = raport_date
        self.nr_zlecenia = nr_zlecenia
        self.gatunek = gatunek
        self.wlasciciel = wlasciciel
        self.nazwa = nazwa

        self.ast_wynik=ast_wynik
        self.alt_wynik = alt_wynik
        self.alp_wynik = alp_wynik
        self.bilirubina_wynik = bilirubina_wynik
        self.ggt_wynik=ggt_wynik
        self.ldh_wynik=ldh_wynik
        self.cholesterol_wynik=cholesterol_wynik
        self.triglicerydy_wynik = triglicerydy_wynik
        self.kw_zolt_wynik = kw_zolt_wynik
        self.bialko_wynik = bialko_wynik
        self.albuminy_wynik=albuminy_wynik
        self.glukoza_wynik = glukoza_wynik
        self.fruktozamina_wynik = fruktozamina_wynik
        self.mocznik_wynik = mocznik_wynik
        self.kreatynina_wynik = kreatynina_wynik
        self.kinaza_wynik=kinaza_wynik
        self.amylaza_wynik = amylaza_wynik
        self.lipaza_wynik = lipaza_wynik
        self.wapn_wynik=wapn_wynik
        self.fosfor_wynik = fosfor_wynik
        self.magnez_wynik=magnez_wynik
        self.zelazo_wynik=zelazo_wynik
        self.potas_wynik = potas_wynik
        self.sod_wynik = sod_wynik
        self.chlorki_wynik=chlorki_wynik

        

        self.uwagi=uwagi
        #normy badań kota
        # biochemia krwi
        ast_kot_norma = [6.0,44.0]          #U/l
        alt_kot_norma = [20.0,107.0]        #U/l
        alp_kot_norma = [23.0,107.0]        #U/l
        bilirubina_kot_norma = [0.5,1.2]    #mg/dl
        ggt_kot_norma = [0.0,10.0]          #U/l
        ldh_kot_norma = [161.0,1051.0]      #U/l
        cholesterol_kot_norma = [77.4,201.2] #mg/dl
        triglicerydy_kot_norma = [17.7,159.4] ##mg/dl
        kw_zolt_kot_norma = [0.0,25.0] #umol/l
        białko_kot_norma = [60.0,80.0] #g/l
        albuminy_kot_norma = [27.0,39.0] #g/l
        glukoza_kot_norma = [100.0,130.0]#mg/dl
        fruktozamina_kot_norma = [0.0,400.0] #umol/l
        mocznik_kot_norma = [25.0,70.0]#mg/dl
        kreatynina_kot_norma = [1.0,1.8]#mg/dl
        kinaza_kot_norma = [49.0,688.0] #U/l
        amylaza_kot_norma = [433.0,1248.0] #U/l
        lipaza_kot_norma = [157.0,1715.0] #U/l
        wapn_kot_norma = [8.0,11.1] #mg/dl
        fosfor_kot_norma = [3.0,6.8]        #mg/dl
        magnez_kot_norma =[2.1,3.2] #mg/dl
        zelazo_kot_norma =[68.0,215.0] #ug/dl
        potas_kot_norma = [4.1,5.6] #mg/dl
        sod_kot_norma = [143.6,156.5] #mg/dl
        chlorki_kot_norma = [360.0,420.0] #mg/dl
        



        #normy badań psa
        # biochemia krwi
        ast_psa_norma = [1.0,45.0]          #U/l
        alt_psa_norma = [3.0,60.0]        #U/l
        alp_psa_norma = [20.0,155.0]        #U/l
        bilirubina_psa_norma = [0.3,0.9]    #mg/dl
        ggt_psa_norma = [5.0,25.0]          #U/l
        ldh_psa_norma = [105.0,1683.0]      #U/l
        cholesterol_psa_norma = [127.7,360.0] #mg/dl
        triglicerydy_psa_norma = [17.7,115.1] ##mg/dl
        kw_zolt_psa_norma = [0.0,30.0] #umol/l
        białko_psa_norma = [50.0,75.0] #g/l
        albuminy_psa_norma = [33.0,56.0] #g/l
        glukoza_psa_norma = [70.0,120.0]#mg/dl
        fruktozamina_psa_norma = [0.0,320.0] #umol/l
        mocznik_psa_norma = [20.0,50.0]#mg/dl
        kreatynina_psa_norma = [0.9,1.7]#mg/dl
        kinaza_psa_norma = [25.0,467.0] #U/l
        amylaza_psa_norma = [300.0,1850.0] #U/l
        lipaza_psa_norma = [268.0,1769.0] #U/l
        wapn_psa_norma = [8.4,11.5] #mg/dl
        fosfor_psa_norma = [2.5,6.3]        #mg/dl
        magnez_psa_norma =[1.7,2.9] #mg/dl
        zelazo_psa_norma =[94.0,122.0] #ug/dl
        potas_psa_norma = [4.1,5.4] #mg/dl
        sod_psa_norma = [320.0,360.0] #mg/dl
        chlorki_psa_norma = [350.0,410.0] #mg/dl

        normy=[]

        if self.gatunek=='Kot':
            #biochemia
            normy.append(ast_kot_norma)
            normy.append(alt_kot_norma)
            normy.append(alp_kot_norma)
            normy.append(bilirubina_kot_norma)
            normy.append(ggt_kot_norma)
            normy.append(ldh_kot_norma)
            normy.append(cholesterol_kot_norma)
            normy.append(triglicerydy_kot_norma)
            normy.append(kw_zolt_kot_norma)
            normy.append(białko_kot_norma)
            normy.append(albuminy_kot_norma)
            normy.append(glukoza_kot_norma)
            normy.append(fruktozamina_kot_norma)
            normy.append(mocznik_kot_norma)
            normy.append(kreatynina_kot_norma)
            normy.append(kinaza_kot_norma)
            normy.append(amylaza_kot_norma)
            normy.append(lipaza_kot_norma)
            normy.append(wapn_kot_norma)
            normy.append(fosfor_kot_norma)
            normy.append(magnez_kot_norma)
            normy.append(zelazo_kot_norma)
            normy.append(potas_kot_norma)
            normy.append(sod_kot_norma)
            normy.append(chlorki_kot_norma)
        elif self.gatunek=='Pies':
            #biochemia
            normy.append(ast_psa_norma)
            normy.append(alt_psa_norma)
            normy.append(alp_psa_norma)
            normy.append(bilirubina_psa_norma)
            normy.append(ggt_psa_norma)
            normy.append(ldh_psa_norma)
            normy.append(cholesterol_psa_norma)
            normy.append(triglicerydy_psa_norma)
            normy.append(kw_zolt_psa_norma)
            normy.append(białko_psa_norma)
            normy.append(albuminy_psa_norma)
            normy.append(glukoza_psa_norma)
            normy.append(fruktozamina_psa_norma)
            normy.append(mocznik_psa_norma)
            normy.append(kreatynina_psa_norma)
            normy.append(kinaza_psa_norma)
            normy.append(amylaza_psa_norma)
            normy.append(lipaza_psa_norma)
            normy.append(wapn_psa_norma)
            normy.append(fosfor_psa_norma)
            normy.append(magnez_psa_norma)
            normy.append(zelazo_psa_norma)
            normy.append(potas_psa_norma)
            normy.append(sod_psa_norma)
            normy.append(chlorki_psa_norma)

       

        
        complete_filename = os.path.join(save_path,docname)
        self.raport  = canvas.Canvas(complete_filename, pagesize=A4)

        self.raport.setLineWidth(.3)
        self.raport.setFont('FreeSans',12)

        self.raport.drawString(30,780,'Gabinet Weterynaryjny CANIS')
        self.raport.drawString(30,765,'ul. Krajobrazowa 2')
        self.raport.drawString(30,750,'35-119 Rzeszów')
        self.raport.drawString(30,735,'tel. 17 859 03 79, Email: kontakt@canisrzeszow.pl')
        self.raport.drawString(30,720,'http://canisrzeszow.pl/')
        self.raport.drawString(480,780, f'{raport_date}')
        self.raport.line(480,777,580,777)
        self.raport.line(5,715,580,715)

        self.raport.drawString(30,700, f'Nr zlecenia: {self.nr_zlecenia}')
        self.raport.drawString(300,700,f'Gatunek: {self.gatunek}')
        self.raport.drawString(30,685, f'Właściciel: {self.wlasciciel}')
        self.raport.drawString(300,685, f'Imie zw.: {self.nazwa}')
        self.raport.line(5,680,580,680)

        self.raport.drawString(30,665,'Badanie')
        self.raport.drawString(200,665,'Wynik')
        self.raport.drawString(320,665,'Jedn.')
        self.raport.drawString(420,665,'Norma')
        self.raport.line(30,655,550,655)
        self.raport.setFont('FreeSansBold',12)
        self.raport.drawString(30,640,'OZNACZENIA BIOCHEMICZNE')
        self.raport.setFont('FreeSans',12)
        self.raport.line(30,635,550,635)

        self.raport.setFont('FreeSans',10)
        self.raport.drawString(30,625,'AST')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,625,f'{self.ast_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,625,'U/l')
        self.raport.drawString(420,625,f'{normy[0]}')
        if ast_wynik!='' and ast_wynik < normy[0][0]:
            self.raport.drawString(500,625,wynik_niski)
        elif ast_wynik!='' and ast_wynik > normy[0][1]:
            self.raport.drawString(500,625,wyniki_wysoki)
        elif self.ast_wynik=='':
            self.raport.drawString(500,625,brak_badania)
        else:
            self.raport.drawString(500,625, wynik_ok)
        
        self.raport.line(30,622,550,622)

        self.raport.drawString(30,610,'ALT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,610,f'{self.alt_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,610,'U/l')
        self.raport.drawString(420,610,f'{normy[1]}')
        if alt_wynik!='' and alt_wynik < normy[1][0]:
            self.raport.drawString(500,610,wynik_niski)
        elif alt_wynik!='' and alt_wynik > normy[1][1]:
            self.raport.drawString(500,610,wynik_niski)
        elif alt_wynik=='':
            self.raport.drawString(500,610,brak_badania)
        else:
            self.raport.drawString(500,610,wynik_ok)
        self.raport.line(30,607,550,607)


        self.raport.drawString(30,595,'ALP')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,595,f'{self.alp_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,595,'U/l')
        self.raport.drawString(420,595,f'{normy[2]}')
        if self.alp_wynik!='' and self.alp_wynik < normy[2][0]:
            self.raport.drawString(500,595,wynik_niski)
        elif self.alp_wynik!='' and self.alp_wynik> normy[2][1]:
            self.raport.drawString(500,595,wyniki_wysoki)
        elif self.alp_wynik=='':
            self.raport.drawString(500,595,brak_badania)
        else:
            self.raport.drawString(500,595,wynik_ok)
        self.raport.line(30,592,550,592)

        self.raport.drawString(30,580,'Bilirubina całkowita')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,580,f'{self.bilirubina_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,580,'mg/dl')
        self.raport.drawString(420,580,f'{normy[3]}')
        if self.bilirubina_wynik!='' and self.bilirubina_wynik < normy[3][0]:
            self.raport.drawString(500,580, wynik_niski)
        elif self.bilirubina_wynik!='' and self.bilirubina_wynik > normy[3][1]:
            self.raport.drawString(500,580,wyniki_wysoki)
        elif self.bilirubina_wynik =='':
            self.raport.drawString(500,580,brak_badania)
        else:
            self.raport.drawString(500,580,wynik_ok)
        self.raport.line(30,577,550,577)

        self.raport.drawString(30,565,'GGT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,565,f'{ggt_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,565,'U/l')
        self.raport.drawString(420,565,f'{normy[4]}')
        if ggt_wynik!='' and ggt_wynik<normy[4][0]:
            self.raport.drawString(500,565,wynik_niski)
        elif  ggt_wynik!='' and ggt_wynik>normy[4][1]:
            self.raport.drawString(500,565,wynik_niski)
        elif ggt_wynik=='':
            self.raport.drawString(500,565,brak_badania)
        else:
            self.raport.drawString(500,565,wynik_ok)
        self.raport.line(30,562,550,562)

        self.raport.drawString(30,550,'LDH')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,550,f'{ldh_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,550,'U/l')
        self.raport.drawString(420,550,f'{normy[5]}')
        if self.ldh_wynik!='' and self.ldh_wynik < normy[5][0]:
            self.raport.drawString(500,550,wynik_niski)
        elif self.ldh_wynik!='' and self.ldh_wynik > normy[5][1]:
            self.raport.drawString(500,550,wyniki_wysoki)
        elif self.ldh_wynik=='':
            self.raport.drawString(500,550,brak_badania)
        else:
            self.raport.drawString(500,550,wynik_ok)
        self.raport.line(30,547,550,547)

        self.raport.drawString(30,535,'Cholesterol')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,535,f'{cholesterol_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,535,'mg/dl')
        self.raport.drawString(420,535,f'{normy[6]}')
        if self.cholesterol_wynik!='' and self.cholesterol_wynik <normy[6][0]:
            self.raport.drawString(500,535,wynik_niski)
        elif self.cholesterol_wynik!='' and self.cholesterol_wynik > normy[6][1]:
            self.raport.drawString(500,535,wyniki_wysoki)
        elif self.cholesterol_wynik=='':
            self.raport.drawString(500,535,brak_badania)
        else:
            self.raport.drawString(500,535,wynik_ok)
        self.raport.line(30,532,550,532)

        self.raport.drawString(30,520,'Triglicerydy')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,520,f'{triglicerydy_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,520,'mg/dl')
        self.raport.drawString(420,520,f'{normy[7]}')
        if self.triglicerydy_wynik!='' and self.triglicerydy_wynik <normy[7][0]:
            self.raport.drawString(500,520,wynik_niski)
        elif self.triglicerydy_wynik!='' and self.triglicerydy_wynik>normy[7][1]:
            self.raport.drawString(500,520,wyniki_wysoki)
        elif self.triglicerydy_wynik=='':
            self.raport.drawString(500,520,brak_badania)
        else:
            self.raport.drawString(500,520,wynik_ok)
        self.raport.line(30,517,550,517)

        self.raport.drawString(30,505,'Kwasy żółciowe') 
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,505,f'{kw_zolt_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,505,'umol/ll')
        self.raport.drawString(420,505,f'{normy[8]}')
        if self.kw_zolt_wynik!='' and self.kw_zolt_wynik < normy[8][0]:
            self.raport.drawString(500,505,wynik_niski)
        elif self.kw_zolt_wynik!='' and self.kw_zolt_wynik > normy[8][1]:
            self.raport.drawString(500,505, wyniki_wysoki)
        elif self.kw_zolt_wynik=='':
            self.raport.drawString(500,505,brak_badania)
        else:
            self.raport.drawString(500,505,wynik_ok)
        self.raport.line(30,502,550,502)

        self.raport.drawString(30,490, 'Białko całkowite')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,490,f'{bialko_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,490,'g/l')
        self.raport.drawString(420,490,f'{normy[9]}')
        if self.bialko_wynik!='' and self.bialko_wynik < normy[9][0]:
            self.raport.drawString(500,490,wynik_niski)
        elif self.bialko_wynik!='' and self.bialko_wynik > normy[9][1]:
            self.raport.drawString(500,490,wyniki_wysoki)
        elif self.bialko_wynik=='':
            self.raport.drawString(500,490, brak_badania)
        else:
            self.raport.drawString(500,490,wynik_ok)
        self.raport.line(30,487,550,487)

        self.raport.drawString(30,475,'Albuminy')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,475,f'{albuminy_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,475,'g/l')
        self.raport.drawString(420,475,f'{normy[10]}')
        if self.albuminy_wynik!='' and self.albuminy_wynik < normy[10][0]:
            self.raport.drawString(500,475,wynik_niski)
        elif self.albuminy_wynik!='' and self.albuminy_wynik > normy[10][1]:
            self.raport.drawString(500,475,wyniki_wysoki)
        elif self.albuminy_wynik=='':
            self.raport.drawString(500,475, brak_badania)
        else:
             self.raport.drawString(500,475,wynik_ok)
        self.raport.line(30,472,550,472)

        self.raport.drawString(30,460,'Glukoza')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,460,f'{glukoza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,460,'mg/dl')
        self.raport.drawString(420,460,f'{normy[11]}')
        if self.glukoza_wynik!='' and self.glukoza_wynik < normy[11][0]:
            self.raport.drawString(500,460,wynik_niski)
        elif self.glukoza_wynik!='' and self.glukoza_wynik > normy[11][1]:
            self.raport.drawString(500,460,wyniki_wysoki)
        elif self.glukoza_wynik=='':
            self.raport.drawString(500,460, brak_badania)
        else:
            self.raport.drawString(500,460,wynik_ok)
        self.raport.line(30,457,550,457)

        self.raport.drawString(30,445,'Fruktozamina')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,445,f'{fruktozamina_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,445,'umol/l')
        self.raport.drawString(420,445,f'{normy[12]}')
        if self.fruktozamina_wynik!='' and self.fruktozamina_wynik < normy[12][0]:
            self.raport.drawString(500,445, wynik_niski)
        elif self.fruktozamina_wynik!='' and self.fruktozamina_wynik > normy[12][1]:
            self.raport.drawString(500,445), wyniki_wysoki
        elif self.fruktozamina_wynik=='':
            self.raport.drawString(500,445,brak_badania)
        else: 
            self.raport.drawString(500,445,wynik_ok)
        self.raport.line(30,442,550,442)

        self.raport.setFont('FreeSans',10)
        self.raport.drawString(30,430, 'Mocznik')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,430,f'{mocznik_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,430,'mg/dl')
        self.raport.drawString(420,430,f'{normy[13]}')
        if self.mocznik_wynik!='' and self.mocznik_wynik < normy[13][0]:
            self.raport.drawString(500,430,wynik_niski)
        elif self.mocznik_wynik!='' and self.mocznik_wynik > normy[13][1]:
            self.raport.drawString(500,430, wyniki_wysoki)
        elif self.mocznik_wynik=='':
            self.raport.drawString(500,430,brak_badania)
        else: 
            self.raport.drawString(500,430, wynik_ok)
        self.raport.line(30,427,550,427)

        self.raport.drawString(30,415, 'Kreatynina')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,415,f'{kreatynina_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,415,'mg/dl')
        self.raport.drawString(420,415,f'{normy[14]}')
        if self.kreatynina_wynik!='' and self.kreatynina_wynik < normy[14][0]:
            self.raport.drawString(500,415,wynik_niski)
        elif self.kreatynina_wynik!='' and self.kreatynina_wynik > normy[14][1]:
            self.raport.drawString(500,415,wyniki_wysoki)
        elif self.kreatynina_wynik=='':
            self.raport.drawString(500,415,brak_badania)
        else:
            self.raport.drawString(500,415,wynik_ok)
        self.raport.line(30,412,550,412)

        self.raport.drawString(30,400, 'Kinaza kreatynowa')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,400,f'{kinaza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,400,'U/l')
        self.raport.drawString(420,400,f'{normy[15]}')
        if self.kinaza_wynik!='' and self.kinaza_wynik < normy[15][0]:
            self.raport.drawString(500,400,wynik_niski)
        elif self.kinaza_wynik!='' and self.kinaza_wynik > normy[15][1]:
            self.raport.drawString(500,400,wyniki_wysoki)
        elif self.kinaza_wynik=='':
            self.raport.drawString(500,400, brak_badania)
        else:
            self.raport.drawString(500,400,wynik_ok)
        self.raport.line(30,397,550,397)

        self.raport.drawString(30,385, 'Amylaza')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,385,f'{amylaza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,385,'U/l')
        self.raport.drawString(420,385,f'{normy[16]}')
        if amylaza_wynik!='' and amylaza_wynik < normy[16][0]:
            self.raport.drawString(500,385,wynik_niski)
        elif amylaza_wynik!='' and amylaza_wynik > normy[16][1]:
            self.raport.drawString(500,385,wyniki_wysoki)
        elif amylaza_wynik=='':
            self.raport.drawString(500,385,brak_badania)
        else:
            self.raport.drawString(500,385,wynik_ok)
        self.raport.line(30,382,550,382)

        self.raport.drawString(30,370,'Lipaza')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,370,f'{lipaza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,370,'U/l')
        self.raport.drawString(420,370,f'{normy[17]}')
        if lipaza_wynik!='' and lipaza_wynik < normy[17][0]:
            self.raport.drawString(500,370,wynik_niski)
        elif lipaza_wynik!='' and lipaza_wynik > normy[17][1]:
            self.raport.drawString(500,370,wyniki_wysoki)
        elif lipaza_wynik=='':
            self.raport.drawString(500,370,brak_badania)
        else:
            self.raport.drawString(500,370,wynik_ok)
        self.raport.line(30,367,550,367)

        self.raport.drawString(30,355, 'Wapń')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,355,f'{wapn_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,355,'mg/dl')
        self.raport.drawString(420,355,f'{normy[18]}')
        if wapn_wynik!='':
            if wapn_wynik < normy[18][0]:
                self.raport.drawString(500,355,wynik_niski)
            elif wapn_wynik > normy[18][1]:
                self.raport.drawString(500,355,wyniki_wysoki)
            else:
                self.raport.drawString(500,355,wynik_ok)
        elif  wapn_wynik=='':
            self.raport.drawString(500,355, brak_badania)
        self.raport.line(30,352,550,352)

        self.raport.drawString(30,340,'Fosfor')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,340,f'{fosfor_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,340,'mg/dl')
        self.raport.drawString(420,340,f'{normy[19]}')
        if fosfor_wynik!='':
            if fosfor_wynik < normy[19][0]:
                self.raport.drawString(500,340,wynik_niski)
            elif fosfor_wynik > normy[19][1]:
                self.raport.drawString(500,340,wyniki_wysoki)
            else:
                self.raport.drawString(500,340,wynik_ok)
        elif fosfor_wynik=='':
            self.raport.drawString(500,340,brak_badania)
        self.raport.line(30,337,550,337)

        self.raport.drawString(30,325,'Magnez')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,325,f'{magnez_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,325,'mg/dl')
        self.raport.drawString(420,325,f'{normy[20]}')
        if magnez_wynik!='':
            if magnez_wynik < normy[20][0]:
                self.raport.drawString(500,325,wynik_niski)
            elif magnez_wynik > normy[20][1]:
                self.raport.drawString(500,325,wyniki_wysoki)
            else:
                self.raport.drawString(500,325,wynik_ok)
        elif magnez_wynik=='':
            self.raport.drawString(500,325,brak_badania)
        self.raport.line(30,322,550,322)

        self.raport.drawString(30,310,'Żelazo')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,310,f'{zelazo_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,310,'ug/dl')
        self.raport.drawString(420,310,f'{normy[21]}')
        if zelazo_wynik!='':
            if zelazo_wynik < normy[21][0]:
                self.raport.drawString(500,310,wynik_niski)
            elif zelazo_wynik > normy[21][1]:
                self.raport.drawString(500,310,wyniki_wysoki)
            else:
                self.raport.drawString(500,310,wynik_ok)
        elif zelazo_wynik=='':
            self.raport.drawString(500,310,brak_badania)
        self.raport.line(30,307,550,307)

        self.raport.drawString(30,295,'Potas')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,295,f'{potas_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,295,'mmol/l')
        self.raport.drawString(420,295,f'{normy[22]}')
        if potas_wynik!='':
            if potas_wynik < normy[22][0]:
                self.raport.drawString(500,295,wynik_niski)
            elif potas_wynik > normy[22][1]:
                self.raport.drawString(500,295,wyniki_wysoki)
            else:
                self.raport.drawString(500,295,wynik_ok)
        elif potas_wynik=='':
            self.raport.drawString(500,295,brak_badania)
        self.raport.line(30,292,550,292)

        self.raport.drawString(30,280,'Sód')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,280,f'{sod_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,280,'mg/dl')
        self.raport.drawString(420,280,f'{normy[23]}')
        if sod_wynik!='':
            if sod_wynik < normy[23][0]:
                self.raport.drawString(500,280,wynik_niski)
            elif sod_wynik > normy[23][1]:
                self.raport.drawString(500,280,wyniki_wysoki)
            else:
                self.raport.drawString(500,280,wynik_ok)
        elif sod_wynik=='':
            self.raport.drawString(500,280,brak_badania)
        self.raport.line(30,277,550,277)

        self.raport.drawString(30,265,'Chlorki')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,265,f'{chlorki_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,265,'mg/dl')
        self.raport.drawString(420,265,f'{normy[24]}')
        if chlorki_wynik!='':
            if chlorki_wynik < normy[20][0]:
                self.raport.drawString(500,265,wynik_niski)
            elif chlorki_wynik > normy[20][1]:
                self.raport.drawString(500,265,wyniki_wysoki)
            else:
                self.raport.drawString(500,265,wynik_ok)
        elif chlorki_wynik=='':
            self.raport.drawString(500,265,brak_badania)
        self.raport.line(30,262,550,262)




        self.raport.drawString(30,240,'Uwagi: ')
        self.raport.drawString(65,240,f'{self.uwagi}')
        
        self.raport.save()

#test = diag_canvas('test','2022-10-24','6543213','Kot', 'Bartłomiej Nowak', 'Bella', 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'nie ma żadnych')



