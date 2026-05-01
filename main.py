import tkinter
import  base64

Notlar = {}

def kaydet():
    Notlar[şifre.get()] = dosyaAdı.get()

    yazı = girilecekNot.get("1.0" , tkinter.END)

    sifreli_bayt = base64.b64encode(yazı.encode("utf-8"))
    sifreli_metin = sifreli_bayt.decode("utf-8")

    with open(f"{dosyaAdı.get()}.txt", "a", encoding="utf-8") as dosya:
        dosya.write(sifreli_metin)

def şifreÇöz():
    if şifre.get() in Notlar.keys():
        with open(f"{dosyaAdı.get()}.txt", "r", encoding="utf-8") as dosya:
            sca = dosya.read()

        cozulen_bayt = base64.b64decode(sca.encode("utf-8"))
        gercek_yazi = cozulen_bayt.decode("utf-8")

        with open(f"{dosyaAdı.get()}.txt" , "w", encoding="utf-8") as dosya:
            dosya.write(gercek_yazi)

        yanlış.config(text = "Şifre Doğru")

    else:
        yanlış.config(text = "Şifre Yanlış")


#Screen
screen = tkinter.Tk()
screen.minsize(500, 800)
screen.title("Secret Notes")

#İmage
resim = tkinter.PhotoImage(file="C:/Users/samet/Pictures/Screenshots/456.png")
resim_alani = tkinter.Label(screen, image=resim)
resim_alani.place(x= 400, y = 30)

resim2 = tkinter.PhotoImage(file="C:/Users/samet/Pictures/Screenshots/456.png")
resim_alani2 = tkinter.Label(screen, image=resim)
resim_alani2.place(x= 30, y = 30)

#Label
başlık = tkinter.Label(text = "Secret Notes" , font=("Arial", 20))
başlık.pack()

dosyaAdıBaşlık = tkinter.Label(text = "Dosya Adı" , font=("Arial", 15))
dosyaAdıBaşlık.place(x = 190 , y = 95)

notBaşlığı = tkinter.Label(text = "Not" , font=("Arial", 15))
notBaşlığı.place(x = 225 , y = 200)

şifreBaşlığı = tkinter.Label(text = "Şifreyi Giriniz" , font=("Arial", 12))
şifreBaşlığı.place(x = 190 , y = 550)

yanlış = tkinter.Label(text = "" , font=("Arial", 15))
yanlış.place(x = 185 , y = 730)

#Entry
dosyaAdı = tkinter.Entry(width = 30)
dosyaAdı.place(x = 128 , y = 130)

şifre = tkinter.Entry(width = 30)
şifre.place(x = 130 , y = 590)

#Text
girilecekNot = tkinter.Text(width = 24 , height = 15)
girilecekNot.place(x = 128 , y = 240)

#Button
kaydetButonu = tkinter.Button(text = "Kaydet ve Şifrele", command = kaydet)
kaydetButonu.place(x = 195 , y = 630)

şifreÇöz = tkinter.Button(text = "Şifreyi Çöz" , command = şifreÇöz)
şifreÇöz.place(x = 215 , y = 680)

screen.mainloop()
