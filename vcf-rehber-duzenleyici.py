# ================= AUTO DEPENDENCY INSTALL =================
import sys
import subprocess

REQUIRED_PACKAGES = [
    "ttkbootstrap==1.14.6",
    "Pillow"
]

def install_and_import(package):
    try:
        __import__(package.split("==")[0])
    except ImportError:
        print(f"[+] {package} bulunamadı, yükleniyor...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package],
            stdout=subprocess.DEVNULL
        )

for pkg in REQUIRED_PACKAGES:
    install_and_import(pkg)
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import *
import re
import quopri
from tkinter import StringVar

contacts = []
filtered_contacts = []


# ----------------- GÜÇLÜ VCF IMPORTER -----------------
def decode_value(value: str):
    """QUOTED-PRINTABLE ve UTF-8 decoding"""
    try:
        if "=" in value:
            value = quopri.decodestring(value).decode("utf-8")
    except:
        pass
    return value.strip()


def normalize_phone(num: str):
    """Bütün telefon formatlarını +90 555 555 55 55 olacak şekilde normalize eder"""
    digits = re.sub(r"[^0-9+]", "", num)

    # Başındaki 0'yı kırp
    if digits.startswith("0"):
        digits = digits[1:]

    # Eğer + yoksa → Türkiye varsay
    if not digits.startswith("+"):
        if digits.startswith("90"):
            digits = "+" + digits
        elif len(digits) == 10:  # Örn: 5323456789
            digits = "+90" + digits
        else:
            digits = "+" + digits

    # Formatlı çıkış
    d = re.sub(r"[^0-9]", "", digits)
    if d.startswith("90") and len(d) == 12:
        return f"+90 {d[2:5]} {d[5:8]} {d[8:10]} {d[10:12]}"

    return digits


def read_vcf(file_path):
    """Senin GUI koduna tam uyumlu yeni profesyonel VCF importer"""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    cards = re.findall(r"BEGIN:VCARD(.*?)END:VCARD", content, re.S)

    unique = []
    numbers_seen = set()
    duplicate_count = 0

    for c in cards:
        name = ""
        org = ""
        numbers = []

        for line in c.split("\n"):
            line = line.strip()

            # FN
            if line.startswith("FN"):
                parts = line.split(":", 1)
                if len(parts) > 1:
                    name = decode_value(parts[1])

            # N alanı fallback
            elif line.startswith("N:") or line.startswith("N;"):
                parts = line.split(":", 1)
                if len(parts) > 1:
                    clean = decode_value(parts[1].replace(";", " ").strip())
                    if not name and clean:
                        name = clean

            # ORG fallback
            elif line.startswith("ORG"):
                parts = line.split(":", 1)
                if len(parts) > 1:
                    org = decode_value(parts[1])

            # TEL alanı
            elif line.startswith("TEL"):
                parts = line.split(":", 1)
                if len(parts) > 1:
                    raw = parts[1].strip()
                    normalized = normalize_phone(raw)
                    numbers.append(normalized)

        # İsim yok → fallback üret
        if not name:
            if org:
                name = org
            elif numbers:
                name = f"Kişi {numbers[0]}"
            else:
                name = "İsimsiz"

        # Aynı numarayı tekrar eklememek
        for num in numbers:
            if num in numbers_seen:
                duplicate_count += 1
                continue
            numbers_seen.add(num)

            unique.append({"name": name, "number": num})

    return unique, duplicate_count


# ----------------- TABLOYU YENİLE -----------------
def refresh_table(data=None):
    global filtered_contacts
    tree.delete(*tree.get_children())

    if data is None:
        data = contacts

    filtered_contacts = data

    for idx, c in enumerate(data):
        tree.insert("", "end", iid=str(idx), values=(c["name"], c["number"]))


# ----------------- ARAMA -----------------
def search_contacts(event=None):
    text = search_var.get().lower()

    if text == "":
        refresh_table(contacts)
        return

    results = [c for c in contacts if text in c["name"].lower() or text in c["number"]]
    refresh_table(results)


# ----------------- DÜZENLE -----------------
def edit_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Uyarı", "Düzenlemek için bir kayıt seç!")
        return

    idx = int(selected[0])
    contact = filtered_contacts[idx]

    edit_win = Toplevel(root)
    edit_win.title("Kişiyi Düzenle")
    edit_win.geometry("300x200")

    Label(edit_win, text="Ad").pack(pady=5)
    name_entry = Entry(edit_win)
    name_entry.insert(0, contact["name"])
    name_entry.pack()

    Label(edit_win, text="Numara").pack(pady=5)
    number_entry = Entry(edit_win)
    number_entry.insert(0, contact["number"])
    number_entry.pack()

    def save_edit():
        new_name = name_entry.get().strip()
        new_number = number_entry.get().strip()

        if new_name == "" or new_number == "":
            messagebox.showerror("Hata", "Alanlar boş olamaz!")
            return

        original_index = contacts.index(contact)
        contacts[original_index] = {"name": new_name, "number": new_number}

        search_contacts()
        edit_win.destroy()

    Button(edit_win, text="Kaydet", command=save_edit).pack(pady=15)


# ----------------- SİL -----------------
def delete_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Uyarı", "Silmek için bir kayıt seç!")
        return

    idx = int(selected[0])
    contact = filtered_contacts[idx]

    if messagebox.askyesno("Sil", f"{contact['name']} silinsin mi?"):
        contacts.remove(contact)
        search_contacts()


# ----------------- VCF YÜKLE -----------------
def load_vcf():
    global contacts
    file_path = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
    if not file_path:
        return

    contacts, dup = read_vcf(file_path)

    refresh_table()

    messagebox.showinfo("Tamamlandı", f"{dup} adet mükerrer numara kaldırıldı.")


# ----------------- VCF KAYDET -----------------
def save_vcf():
    file_path = filedialog.asksaveasfilename(defaultextension=".vcf")
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as f:
        for c in contacts:
            f.write("BEGIN:VCARD\n")
            f.write("VERSION:3.0\n")
            f.write(f"FN:{c['name']}\n")
            f.write(f"TEL:{c['number']}\n")
            f.write("END:VCARD\n\n")

    messagebox.showinfo("Kayıt", "Temiz rehber kaydedildi.")


# ----------------- GUI TASARIM -----------------

style = Style(theme="darkly")

root = style.master
root.title("Modern VCF Rehber Düzenleyici")
root.geometry("800x500")

top_frame = Frame(root)
top_frame.pack(fill="x", padx=10, pady=10)

Button(top_frame, text="VCF Yükle", command=load_vcf, bootstyle="info").pack(side="left", padx=5)
Button(top_frame, text="VCF Kaydet", command=save_vcf, bootstyle="success").pack(side="left", padx=5)
Button(top_frame, text="Düzenle", command=edit_contact, bootstyle="warning").pack(side="left", padx=5)
Button(top_frame, text="Sil", command=delete_contact, bootstyle="danger").pack(side="left", padx=5)

search_var = StringVar()
search_entry = Entry(top_frame, textvariable=search_var, width=40)
search_entry.pack(side="right", padx=5)
search_entry.bind("<KeyRelease>", search_contacts)

Label(top_frame, text="Ara:", bootstyle="inverse").pack(side="right")

columns = ("Ad", "Numara")
tree = Treeview(root, columns=columns, show="headings", bootstyle="dark")
tree.heading("Ad", text="Ad")
tree.heading("Numara", text="Numara")
tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
