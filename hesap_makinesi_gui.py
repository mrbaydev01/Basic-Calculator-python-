import tkinter as tk

def hesapla(islem):
    try:
        a = float(sayi1.get())
        b = float(sayi2.get())
        
        if islem == "topla":
            sonuc.set(a + b)
        elif islem == "cikar":
            sonuc.set(a - b)
        elif islem == "carp":
            sonuc.set(a * b)
        elif islem == "bol":
            if b != 0:
                sonuc.set(a / b)
            else:
                sonuc.set("0'a bölünemez!")
    except ValueError:
        sonuc.set("Geçersiz giriş!")

root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("300x300")

tk.Label(root, text="Birinci Sayı:").pack()
sayi1 = tk.Entry(root)
sayi1.pack()

tk.Label(root, text="İkinci Sayı:").pack()
sayi2 = tk.Entry(root)
sayi2.pack()

sonuc = tk.StringVar()
tk.Label(root, text="Sonuç:").pack()
tk.Label(root, textvariable=sonuc, font=("Arial", 14)).pack()

tk.Button(root, text="Topla", command=lambda: hesapla("topla")).pack()
tk.Button(root, text="Çıkar", command=lambda: hesapla("cikar")).pack()
tk.Button(root, text="Çarp", command=lambda: hesapla("carp")).pack()
tk.Button(root, text="Böl", command=lambda: hesapla("bol")).pack()

root.mainloop()
