import sys
import os

from kanisLayout import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt6.QtCore import QDate, Qt
import subprocess
from Kanis_canvas import diag_canvas
from datetime import date, time, datetime



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.save_folder()
        self.start_date()
        
        
               
    def start_date(self):
        self.dataBadania.setDate(date.today())

    def save_folder(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        if os.path.isdir(f'{self.dir_path}\\Wyniki'):
            pass
        else:
            os.mkdir(f'{self.dir_path}\\Wyniki')
        self.save_path = f'{self.dir_path}\\Wyniki'

    def zmiana_norm(self,s):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.normy=[]
        
        if s=='Pies':
            self.normy.clear()
            file = open(f'{self.dir_path}\\normy_psa.txt','r')
            for line in file:
                temp_line=line.replace('_',' ').replace(' ','').strip().split('=')
                self.normy.append(temp_line)
            self.normaAST.setText(f'NORMA {self.normy[0][0]}: {self.normy[0][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaALT.setText(f'NORMA {self.normy[1][0]}: {self.normy[1][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaALP.setText(f'NORMA {self.normy[2][0]}: {self.normy[2][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaBILI.setText(f'NORMA {self.normy[3][0]}: {self.normy[3][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaGGT.setText(f'NORMA {self.normy[4][0]}: {self.normy[4][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaLDH.setText(f'NORMA {self.normy[5][0]}: {self.normy[5][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaCHOL.setText(f'NORMA {self.normy[6][0]}: {self.normy[6][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaTRIG.setText(f'NORMA {self.normy[7][0]}: {self.normy[7][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKWASZ.setText(f'NORMA KWAS ŻÓŁCIOWY: {self.normy[8][1].replace('[','').replace(']','').replace(',','-')} umol/l')
            self.normaBIALKO.setText(f'NORMA BIAŁKO: {self.normy[9][1].replace('[','').replace(']','').replace(',','-')} g/l')
            self.normaALBUM.setText(f'NORMA {self.normy[10][0]}: {self.normy[10][1].replace('[','').replace(']','').replace(',','-')} g/l')
            self.normaGLUKO.setText(f'NORMA {self.normy[11][0]}: {self.normy[11][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaFRUKTOZ.setText(f'NORMA FRUKTOZAMINA: {self.normy[12][1].replace('[','').replace(']','').replace(',','-')} umol/l')
            self.normaMOCZN.setText(f'NORMA {self.normy[13][0]}: {self.normy[13][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKREAT.setText(f'NORMA {self.normy[14][0]}: {self.normy[14][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKINAZ.setText(f'NORMA {self.normy[15][0]}: {self.normy[15][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaAMYLAZ.setText(f'NORMA {self.normy[16][0]}: {self.normy[16][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaLIPAZ.setText(f'NORMA {self.normy[17][0]}: {self.normy[17][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaWAPN.setText(f'NORMA WAPŃ: {self.normy[18][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaFOSFOR.setText(f'NORMA {self.normy[19][0]}: {self.normy[19][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaMAGNE.setText(f'NORMA {self.normy[20][0]}: {self.normy[20][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaZELAZ.setText(f'NORMA ŻELAZO: {self.normy[21][1].replace('[','').replace(']','').replace(',','-')} ug/dl')
            self.normaPOTAS.setText(f'NORMA {self.normy[22][0]}: {self.normy[22][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaSOD.setText(f'NORMA SÓD: {self.normy[23][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaCHLOR.setText(f'NORMA {self.normy[24][0]}: {self.normy[24][1].replace('[','').replace(']','').replace(',','-')} g/l')
        elif s=='Kot':
            self.normy.clear()
            file = open(f'{self.dir_path}\\normy_kota.txt','r')
            for line in file:
                temp_line=line.replace('_',' ').replace(' ','').strip().split('=')
                self.normy.append(temp_line)
            self.normaAST.setText(f'NORMA {self.normy[0][0]}: {self.normy[0][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaALT.setText(f'NORMA {self.normy[1][0]}: {self.normy[1][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaALP.setText(f'NORMA {self.normy[2][0]}: {self.normy[2][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaBILI.setText(f'NORMA {self.normy[3][0]}: {self.normy[3][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaGGT.setText(f'NORMA {self.normy[4][0]}: {self.normy[4][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaLDH.setText(f'NORMA {self.normy[5][0]}: {self.normy[5][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaCHOL.setText(f'NORMA {self.normy[6][0]}: {self.normy[6][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaTRIG.setText(f'NORMA {self.normy[7][0]}: {self.normy[7][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKWASZ.setText(f'NORMA KWAS ŻÓŁCIOWY: {self.normy[8][1].replace('[','').replace(']','').replace(',','-')} umol/l')
            self.normaBIALKO.setText(f'NORMA BIAŁKO: {self.normy[9][1].replace('[','').replace(']','').replace(',','-')} g/l')
            self.normaALBUM.setText(f'NORMA {self.normy[10][0]}: {self.normy[10][1].replace('[','').replace(']','').replace(',','-')} g/l')
            self.normaGLUKO.setText(f'NORMA {self.normy[11][0]}: {self.normy[11][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaFRUKTOZ.setText(f'NORMA FRUKTOZAMINA: {self.normy[12][1].replace('[','').replace(']','').replace(',','-')} umol/l')
            self.normaMOCZN.setText(f'NORMA {self.normy[13][0]}: {self.normy[13][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKREAT.setText(f'NORMA {self.normy[14][0]}: {self.normy[14][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaKINAZ.setText(f'NORMA {self.normy[15][0]}: {self.normy[15][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaAMYLAZ.setText(f'NORMA {self.normy[16][0]}: {self.normy[16][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaLIPAZ.setText(f'NORMA {self.normy[17][0]}: {self.normy[17][1].replace('[','').replace(']','').replace(',','-')} U/l')
            self.normaWAPN.setText(f'NORMA WAPŃ: {self.normy[18][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaFOSFOR.setText(f'NORMA {self.normy[19][0]}: {self.normy[19][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaMAGNE.setText(f'NORMA {self.normy[20][0]}: {self.normy[20][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaZELAZ.setText(f'NORMA ŻELAZO: {self.normy[21][1].replace('[','').replace(']','').replace(',','-')} ug/dl')
            self.normaPOTAS.setText(f'NORMA {self.normy[22][0]}: {self.normy[22][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaSOD.setText(f'NORMA SÓD: {self.normy[23][1].replace('[','').replace(']','').replace(',','-')} mg/dl')
            self.normaCHLOR.setText(f'NORMA {self.normy[24][0]}: {self.normy[24][1].replace('[','').replace(']','').replace(',','-')} g/l')
        elif s=='Inne':
            self.czyszczenie_labeli()

    def czyszczenie_labeli(self):
        self.normaAST.setText(f'NORMA AST: U/l')
        self.normaALT.setText(f'NORMA ALT: U/l')
        self.normaALP.setText(f'NORMA ALP: U/l')
        self.normaBILI.setText(f'NORMA BILIRUBINA: mg/dl')
        self.normaGGT.setText(f'NORMA GGT: U/l')
        self.normaLDH.setText(f'NORMA LDH: U/l')
        self.normaCHOL.setText(f'NORMA CHOLESTEROL: mg/dl')
        self.normaTRIG.setText(f'NORMA TRIGLICERYDY: mg/dl')
        self.normaKWASZ.setText(f'NORMA KWAS ŻÓŁCIOWY: umol/l')
        self.normaBIALKO.setText(f'NORMA BIAŁKO: g/l')
        self.normaALBUM.setText(f'NORMA ALBUMINY: g/l')
        self.normaGLUKO.setText(f'NORMA GLUKOZA: mg/dl')
        self.normaFRUKTOZ.setText(f'NORMA FRUKTOZAMINA: umol/l')
        self.normaMOCZN.setText(f'NORMA MOCZNIK: mg/dl')
        self.normaKREAT.setText(f'NORMA KREATYNINA: mg/dl')
        self.normaKINAZ.setText(f'NORMA KINAZA: U/l')
        self.normaAMYLAZ.setText(f'NORMA AMYLAZA: U/l')
        self.normaLIPAZ.setText(f'NORMA LIPAZA: U/l')
        self.normaWAPN.setText(f'NORMA WAPŃ: mg/dl')
        self.normaFOSFOR.setText(f'NORMA FOSFOR: mg/dl')
        self.normaMAGNE.setText(f'NORMA MAGNEZ: mg/dl')
        self.normaZELAZ.setText(f'NORMA ŻELAZO: ug/dl')
        self.normaPOTAS.setText(f'NORMA POATAS: mg/dl')
        self.normaSOD.setText(f'NORMA SÓD: mg/dl')
        self.normaCHLOR.setText(f'NORMA CHLORKI: g/l')

    def czyszczenie(self):
        self.rodzajZwierz.setCurrentIndex(0)
        self.nrZlecenia.clear()
        self.nazwaZwierz.clear()
        self.nazwaWlasc.clear()
        self.wynikALBUM.clear()
        self.wynikaLIPA.clear()
        self.wynikALP.clear()
        self.wynikaMAGN.clear()
        self.wynikALT.clear()
        self.wynikAMYLA.clear()
        self.wynikAST.clear()
        self.wynikBIAL.clear()
        self.wynikBILI.clear()
        self.wynikCHLORKI.clear()
        self.wynikCHOL.clear()
        self.wynikFOSF.clear()
        self.wynikFRUKTO.clear()
        self.wynikGGT.clear()
        self.wynikGLUK.clear()
        self.wynikKINAZ.clear()
        self.wynikKREAT.clear()
        self.wynikKWAS.clear()
        self.wynikLDH.clear()
        self.wynikMOCZN.clear()
        self.wynikPOTAS.clear()
        self.wynikSOD.clear()
        self.wynikTRIG.clear()
        self.wynikUWAGI.clear()
        self.wynikWAPN.clear()
        self.wynikZELAZ.clear()

    def zamiana_wartosci(self):
        all_ql = self.findChildren(QLineEdit)
        self.znalezione = []

        for line_edit in all_ql:
            obj_name = line_edit.objectName()
            if obj_name.startswith('wyni'):
                text_val = line_edit.text().strip()
                if not text_val:
                    self.znalezione.append([obj_name, ''])
                    continue
                try:
                    fl_val = float(text_val.replace(',',''))
                    self.znalezione.append([obj_name, fl_val])
                except ValueError:
                    self.znalezione.append([obj_name, ''])
        #for x in range(len(self.znalezione)):
        #    print(x, self.znalezione[x])  

    def drukuj(self):
        nazwa_pliku = f'{self.dataBadania.text().replace('.','_')}_{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}_{self.nazwaWlasc.text()}_{self.nazwaZwierz.text()}.pdf'
        self.zamiana_wartosci()
        self.plik = diag_canvas(nazwa_pliku, str(self.dataBadania.text()), self.nrZlecenia.text(), self.rodzajZwierz.currentText(), self.nazwaWlasc.text(),
                                self.nazwaZwierz.text(), self.znalezione[8][1], self.znalezione[10][1], self.znalezione[14][1], self.znalezione[15][1],
                                self.znalezione[12][1], self.znalezione[7][1], self.znalezione[25][1], self.znalezione[5][1], self.znalezione[3][1],
                                self.znalezione[2][1], self.znalezione[6][1], self.znalezione[1][1], self.znalezione[11][1], self.znalezione[22][1],
                                self.znalezione[4][1], self.znalezione[13][1], self.znalezione[16][1], self.znalezione[0][1], self.znalezione[21][1],
                                self.znalezione[19][1], self.znalezione[9][1], self.znalezione[24][1], self.znalezione[23][1], self.znalezione[17][1], 
                                self.znalezione[18][1], self.wynikUWAGI.text())
        to_open = f'{self.save_path}\\{nazwa_pliku}'
        subprocess.Popen(to_open, shell=True)

    def otworz_folder(self):
        if sys.platform == 'win32':
            os.startfile(self.save_path)
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()