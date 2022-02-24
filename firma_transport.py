from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
root = Tk()

root.geometry("400x400")

cmb = ttk.Combobox(root, width="10", values=("Angajat", "Client", "Furnizor", "Locatie", "Parcare", "Transport", "Vehicul","Gestionare","Contract", "Factura"))
#ANGAJAT
def checkcmbo():
    if cmb.get() == "Angajat":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['cnp_angajat'])
            e2.insert(0, select['tip_angajat'])
            e3.insert(0, select['nume'])
            e4.insert(0, select['prenume'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("cnp_angajat", "tip_angajat", "nume", "prenume"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "cnp_angajat":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "tip_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by tip_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()


                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            cnp_angajat = e1.get()
            tip_angajat = e2.get()
            nume = e3.get()
            prenume = e4.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  angajat  (cnp_angajat,tip_angajat,nume,prenume) VALUES (%s, %s, %s, %s)"
                val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT cnp_angajat,tip_angajat,nume,prenume FROM angajat")
            records = mycursor.fetchall()
            print(records)

            for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                mysqldb.close()

        def update():
            cnp_angajat = e1.get()
            tip_angajat = e2.get()
            nume = e3.get()
            prenume = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat= %s"
                Update = "Update angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat='%s'" % (
                tip_angajat, nume, prenume, cnp_angajat)
                # val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat")

                e1.update(0, END)
                e2.update(0, END)
                e3.update(0, END)
                e4.update(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            cnp_angajat = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from angajat where cnp_angajat = %s"
                val = (cnp_angajat,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("800x500")
        global e1
        global e2
        global e3
        global e4

        tk.Label(root, text="Angajati", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Cnp angajat").place(x=10, y=10)
        Label(root, text="Tip angajat").place(x=10, y=40)
        Label(root, text="Nume").place(x=10, y=70)
        Label(root, text="Prenume").place(x=10, y=100)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('cnp_angajat', 'tip_angajat', 'nume', 'prenume')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

#CLIENT
    elif cmb.get() == "Client":


        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_client'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['prenume'])
            e4.insert(0, select['nr_telefon'])
            e5.insert(0, select['id_locatie'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_client", "nume", "prenume", "nr_telefon", "id_locatie"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_client":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by id_client")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()

                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()


                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()

                if cmbb.get() == "nr_telefon":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by nr_telefon")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()


                if cmbb.get() == "id_locatie":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by id_locatie")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()
            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_client = e1.get()
            nume = e2.get()
            prenume = e3.get()
            nr_telefon = e4.get()
            id_locatie = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  client  (id_client, nume, prenume, nr_telefon, id_locatie) VALUES (%s, %s, %s, %s, %s)"
                val = (id_client, nume, prenume, nr_telefon, id_locatie)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_client, nume, prenume, nr_telefon, id_locatie FROM client")
            records = mycursor.fetchall()
            print(records)

            for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                mysqldb.close()

        def update():
            id_client = e1.get()
            nume = e2.get()
            prenume = e3.get()
            nr_telefon = e4.get()
            id_locatie = e5.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
               # sql = "Update  client set nume= %s,prenume= %s, nr_telefon=%s, id_locatie = %s where id_client= %s"
               # val = (id_client, nume, prenume, nr_telefon, id_locatie)
                Update = "Update client set nume='%s', prenume='%s', nr_telefon='%s', id_locatie='%s' where id_client='%s'" % (
                         nume, prenume, nr_telefon, id_locatie, id_client)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.update(0, END)
                e2.update(0, END)
                e3.update(0, END)
                e4.update(0, END)
                e5.update(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_client = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from client where id_client = %s"
                val = (id_client,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Clienti", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Client").place(x=10, y=10)
        Label(root, text="Nume").place(x=10, y=40)
        Label(root, text="Prenume").place(x=10, y=70)
        Label(root, text="Nr Telefon").place(x=10, y=100)
        Label(root, text="id_locatie").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        e5 = Entry(root)
        e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="Update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_client', 'nume', 'prenume', 'nr_telefon', 'id_locatie')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)


 # FURNIZOR
    elif cmb.get() == "Furnizor":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_furnizor'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['tip_furnizor'])
            e4.insert(0, select['oras'])
        def join():

            id_furnizor = e1.get()
            nume = e2.get()
            id_transport = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()


            try:
                sql = "select fur.id_furnizor = '%s', fur.nume = '%s', tr.id_transport= '%s' from furnizor fur join contract c" \
                      " ON fur.id_furnizor=c.id_furnizor join transport tr ON tr.id_transport = c.id_transport WHERE fur.id_furnizor<>0 " \
                      "and tr.id_transport>1"
                mycursor.execute(sql)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                result_set = mycursor.fetchall()
                mycursor.close()

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

            for i, (id_furnizor, nume, id_transport) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_furnizor, nume, id_transport))
                mysqldb.close()

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("cnp_angajat", "tip_angajat", "nume", "prenume"))

            def sorteaza():
                mysqldb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "cnp_angajat":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "tip_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by tip_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()


                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_furnizor = e1.get()
            nume = e2.get()
            tip_furnizor = e3.get()
            oras = e4.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  furnizor  (id_furnizor,nume,tip_furnizor,oras) VALUES (%s, %s, %s, %s)"
                val = (id_furnizor, nume, tip_furnizor, oras)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_furnizor,nume,tip_furnizor,oras FROM furnizor")
            records = mycursor.fetchall()
            print(records)

            for i, (id_furnizor, nume, tip_furnizor, oras) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_furnizor, nume, tip_furnizor, oras))
                mysqldb.close()

        def update():
            id_furnizor = e1.get()
            nume = e2.get()
            tip_furnizor = e3.get()
            oras = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat= %s"
                Update = "Update furnizor set nume = '%s',tip_furnizor = '%s',oras = '%s' where id_furnizor = '%s'" % (nume, tip_furnizor, oras, id_furnizor)
                # val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.update()
                e2.update(),
                e3.update(0, END)
                e4.update(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_furnizor = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from furnizor where id_furnizor = %s"
                val = (id_furnizor,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("800x500")

        tk.Label(root, text="Furnizor", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id furnizor").place(x=10, y=10)
        Label(root, text="Nume").place(x=10, y=40)
        Label(root, text="Tip Furnizor").place(x=10, y=70)
        Label(root, text="Oras").place(x=10, y=100)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)
        Button(root, text="JOIN", command=join, height=2, width=15).place(x=720, y=200)

        cols = ('id_furnizor', 'nume', 'tip_furnizor', 'oras')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)


#LOCATIE

    elif cmb.get() == "Locatie":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_locatie'])
            e2.insert(0, select['tara'])
            e3.insert(0, select['oras'])
            e4.insert(0, select['cod_postal'])
            e5.insert(0, select['strada'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_locatie", "tara", "oras", "cod_postal", "strada"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_locatie":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by id_locatie")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

                if cmbb.get() == "tara":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by tara")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()


                if cmbb.get() == "oras":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by oras")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

                if cmbb.get() == "cod_postal":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by cod_postal")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()


                if cmbb.get() == "strada":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by strada")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

            #print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_locatie = e1.get()
            tara = e2.get()
            oras = e3.get()
            cod_postal = e4.get()
            strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  locatie  (id_locatie, tara, oras, cod_postal, strada) VALUES (%s, %s, %s, %s, %s)"
                val = (id_locatie, tara, oras, cod_postal, strada)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_locatie, tara, oras, cod_postal, strada FROM locatie")
            records = mycursor.fetchall()
            print(records)

            for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                mysqldb.close()

        def update():
            id_locatie = e1.get()
            tara = e2.get()
            oras = e3.get()
            cod_postal = e4.get()
            strada = e5.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  locatie set tara= %s,oras= %s, cod_postal=%s, strada = %s where id_locatie = %s"
                val = (id_locatie, tara, oras, cod_postal, strada)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_locatie = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from locatie where id_locatie = %s"
                val = (id_locatie,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Locatie", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Locatie").place(x=10, y=10)
        Label(root, text="Tara").place(x=10, y=40)
        Label(root, text="Oras").place(x=10, y=70)
        Label(root, text="Cod Postal").place(x=10, y=100)
        Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        e5 = Entry(root)
        e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_locatie', 'tara', 'oras', 'cod_postal', 'strada')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)
#PARCARE

    elif cmb.get() == "Parcare":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_parcare'])
            e2.insert(0, select['oras'])
            e3.insert(0, select['strada'])
            e4.insert(0, select['capacitate'])
            # e5.insert(0, select['strada'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_parcare", "oras", "strada", "capacitate"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_parcare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by id_parcare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                        mysqldb.close()

                if cmbb.get() == "oras":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by oras")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                        mysqldb.close()


                if cmbb.get() == "strada":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by strada")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                        mysqldb.close()

                if cmbb.get() == "capacitate":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by capacitate")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_parcare = e1.get()
            oras = e2.get()
            strada = e3.get()
            capacitate = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO parcare  (id_parcare, oras, strada, capacitate) VALUES (%s, %s, %s, %s)"
                val = (id_parcare, oras, strada, capacitate)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_parcare, oras, strada, capacitate  FROM parcare")
            records = mycursor.fetchall()
            print(records)

            for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                mysqldb.close()

        def update():
            id_parcare = e1.get()
            oras = e2.get()
            strada = e3.get()
            capacitate = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  parcare set oras= %s, strada= %s, capacitate =%s where id_parcare= %s"
                val = (id_parcare, oras, strada, capacitate)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_parcare = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from parcare where id_parcare = %s"
                val = (id_parcare,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Parcare", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Parcare").place(x=10, y=10)
        Label(root, text="Oras").place(x=10, y=40)
        Label(root, text="Strada").place(x=10, y=70)
        Label(root, text="Capacitate").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_parcare', 'oras', 'strada', 'capacitate')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)

#TRANSPORT

    elif cmb.get() == "Transport":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_transport'])
            e2.insert(0, select['tip_transport'])
            e3.insert(0, select['cantitate_marfa'])
            e4.insert(0, select['cnp_angajat'])
            # e5.insert(0, select['strada'])
        def having():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT avg(cantitate_marfa), id_transport FROM transport HAVING avg(cantitate_marfa)>2500")
            #sa se afiseze cantitatea medie de marfa doar daca aceasta este mai mare de 2500

            records = mycursor.fetchall()
            print(records)

            for i, (id_transport, cantitate_marfa) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_transport, cantitate_marfa,))
                mysqldb.close()


        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_transport", "tip_transport", "cantitate_marfa", "cnp_angajat"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_transport":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "tip_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by tip_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()


                if cmbb.get() == "cantitate_marfa":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by cantitate_marfa")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "cnp_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_transport = e1.get()
            tip_transport = e2.get()
            cantitate_marfa = e3.get()
            cnp_angajat = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  transport  (id_transport, tip_transport, cantitate_marfa, cnp_angajat) VALUES (%s, %s, %s, %s)"
                val = (id_transport, tip_transport, cantitate_marfa, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_transport, tip_transport, cantitate_marfa, cnp_angajat  FROM transport")
            records = mycursor.fetchall()
            print(records)

            for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                mysqldb.close()

        def update():
            id_transport = e1.get()
            tip_transport = e2.get()
            cantitate_marfa = e3.get()
            cnp_angajat = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  transport set tip_transport= %s, cantitate_marfa= %s, cnp_angajat =%s where id_transport= %s"
                val = (id_transport, tip_transport, cantitate_marfa, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_transport = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from transport where id_transport = %s"
                val = (id_transport,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Transport", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Transport").place(x=10, y=10)
        Label(root, text="Tip Transport").place(x=10, y=40)
        Label(root, text="Cantitate Marfa").place(x=10, y=70)
        Label(root, text="CNP Angajat").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)
        Button(root, text="HAVING", command=having, height=2, width=15).place(x=720, y=200)

        cols = ('id_transport', 'tip_transport', 'cantitate_marfa', 'cnp_angajat')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)

#VEHICUL


    elif cmb.get() == "Vehicul":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_vehicul'])
            e2.insert(0, select['km'])
            e3.insert(0, select['capacitate_maxima'])
            e4.insert(0, select['id_parcare'])
            # e5.insert(0, select['strada'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("km", "capacitate_maxima", "id_parcare"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "km":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by km")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

                if cmbb.get() == "capacitate_maxima":
                    print("Capacitate maxima:")
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by capacitate_maxima")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

                if cmbb.get() == "id_parcare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by id_parcare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

        #print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.5", rely="0.1")

        def Add():
            id_vehicul = e1.get()
            km = e2.get()
            capacitate_maxima = e3.get()
            id_parcare = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  vehicul  (id_vehicul, km, capacitate_maxima, id_parcare) VALUES (%s, %s, %s, %s)"
                val = (id_vehicul, km, capacitate_maxima, id_parcare)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT *  FROM vehicul")
            records = mycursor.fetchall()
            print(records)

            for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                mysqldb.close()

        def update():
            id_vehicul = e1.get()
            km = e2.get()
            capacitate_maxima = e3.get()
            id_parcare = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                #sql = "Update vehicul set km= %s, capacitate_maxima = %s, id_parcare =%s where id_vehicul= %s"
                #val = (km, capacitate_maxima, id_parcare, id_vehicul)
                Update = "Update vehicul set km='%s', capacitate_maxima='%s', id_parcare='%s' where id_vehicul='%s'" % (
                    km, capacitate_maxima, id_parcare, id_vehicul)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_vehicul = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from vehicul where id_vehicul = %s"
                val = (id_vehicul,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def clear():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            listBox.delete()
            mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Vehicul", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Vehicul").place(x=10, y=10)
        Label(root, text="KM").place(x=10, y=40)
        Label(root, text="Capacitate Maxima").place(x=10, y=70)
        Label(root, text="Id Parcare").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)


        cols = ('id_vehicul', 'km', 'capacitate_maxima', 'id_parcare')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)
        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)
        # show()
        listBox.bind('<Double-Button-1>', GetValue)
        root.mainloop()

#GESTIONARE

    elif cmb.get() == "Gestionare":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_gestionare'])
            e2.insert(0, select['id_vehicul'])
            e3.insert(0, select['cnp_angajat'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_gestionare", "id_vehicul", "cnp_angajat"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_gestionare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM gestionare order by id_gestionare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "id_vehicul":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM gestionare order by id_vehicul")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                        mysqldb.close()

        def Add():
            id_gestionare = e1.get()
            id_vehicul = e2.get()
            cnp_angajat = e3.get()


            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  gestionare  (id_gestionare, id_vehicul, cnp_angajat) VALUES (%s, %s, %s)"
                val = (id_gestionare, id_vehicul, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_gestionare, id_vehicul, cnp_angajat FROM gestionare")
            records = mycursor.fetchall()
            print(records)

            for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                mysqldb.close()

        def update():
            id_gestionare = e1.get()
            id_vehicul = e2.get()
            cnp_angajat = e3.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  gestionare set id_vehicul= %s,cnp_angajat where id_gestionare= %s"
                val = (id_gestionare, id_vehicul, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_gestionare = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from gestionare where id_gestionare = %s"
                val = (id_gestionare,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Gestionare", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Gestionare").place(x=10, y=10)
        Label(root, text="Id Vehicul").place(x=10, y=40)
        Label(root, text="CNP Angajat").place(x=10, y=70)


        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_gestionare', 'id_vehicul', 'cnp_angajat')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

#CONTRACT

    elif cmb.get() == "Contract":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_contract'])
            e2.insert(0, select['id_furnizor'])
            e3.insert(0, select['id_transport'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_contract", "id_furnizor", "id_transport"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_contract":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_contract")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()

                if cmbb.get() == "id_furnizor":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_furnizor")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()


                if cmbb.get() == "id_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()


            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_contract = e1.get()
            id_furnizor = e2.get()
            id_transport = e3.get()


            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  contract  (id_contract, id_furnizor, id_transport) VALUES (%s, %s, %s)"
                val = (id_contract, id_furnizor, id_transport)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_contract,id_furnizor, id_transport FROM contract")
            records = mycursor.fetchall()
            print(records)

            for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                mysqldb.close()

        def update():
            id_contract = e1.get()
            id_furnizor = e2.get()
            id_transport = e3.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  contract set id_furnizor= %s,id_transport where id_contract= %s"
                val = (id_furnizor, id_transport, id_contract)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_contract = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from contract where id_contract = %s"
                val = (id_contract,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Contract", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Contract").place(x=10, y=10)
        Label(root, text="Id_furnizor").place(x=10, y=40)
        Label(root, text="Id_transport").place(x=10, y=70)


        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_contract', 'id_furnizor', 'id_transport')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

        root.mainloop()

    elif cmb.get() == "Factura":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_factura'])
            e2.insert(0, select['data_emitere'])
            e3.insert(0, select['id_transport'])
            e4.insert(0, select['id_client'])


        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_factura", "data_emitere", "id_transport", "id_client"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_factura":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_factura")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

                if cmbb.get() == "data_emitere":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by data_emitere")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()


                if cmbb.get() == "id_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

                if cmbb.get() == "id_client":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_client")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_factura = e1.get()
            data_emitere = e2.get()
            id_transport = e3.get()
            id_client = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  factura  (id_factura,data_emitere, id_client, id_transport) VALUES (%s, %s,%s, %s)"
                val = (id_factura, data_emitere, id_client, id_transport)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_factura,data_emitere, id_client, id_transport FROM factura")
            records = mycursor.fetchall()
            print(records)

            for i, (id_factura, data_emitere, id_client, id_transport) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_factura, data_emitere, id_client, id_transport))
                mysqldb.close()

        def update():
            id_factura = e1.get()
            data_emitere = e2.get()
            id_transport = e3.get()
            id_client = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  factura set data_emitere=%s, id_transport= %s,id_client=%s where id_factura= %s"
                val = (data_emitere, id_transport, id_client, id_factura)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_factura = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from factura where id_factura = %s"
                val = (id_factura,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Factura", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Factura").place(x=10, y=10)
        tk.Label(root, text="Data Emitere").place(x=10, y=30)
        Label(root, text="Id_transport").place(x=10, y=60)
        Label(root, text="Id_client").place(x=10, y=90)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_factura', 'data_emitere', 'id_furnizor', 'id_transport')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")


cmb.place(relx="0.1", rely="0.1")

btn = ttk.Button(root, text="Alege Tabelul", command=checkcmbo)
btn.place(relx="0.5", rely="0.1")

root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
root = Tk()

root.geometry("400x400")

cmb = ttk.Combobox(root, width="10", values=("Angajat", "Client", "Furnizor", "Locatie", "Parcare", "Transport", "Vehicul","Gestionare","Contract", "Factura"))
#ANGAJAT
def checkcmbo():
    if cmb.get() == "Angajat":

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['cnp_angajat'])
            e2.insert(0, select['tip_angajat'])
            e3.insert(0, select['nume'])
            e4.insert(0, select['prenume'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("cnp_angajat", "tip_angajat", "nume", "prenume"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "cnp_angajat":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "tip_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by tip_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()


                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            cnp_angajat = e1.get()
            tip_angajat = e2.get()
            nume = e3.get()
            prenume = e4.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  angajat  (cnp_angajat,tip_angajat,nume,prenume) VALUES (%s, %s, %s, %s)"
                val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT cnp_angajat,tip_angajat,nume,prenume FROM angajat")
            records = mycursor.fetchall()
            print(records)

            for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                mysqldb.close()

        def update():
            cnp_angajat = e1.get()
            tip_angajat = e2.get()
            nume = e3.get()
            prenume = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat= %s"
                Update = "Update angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat='%s'" % (
                tip_angajat, nume, prenume, cnp_angajat)
                # val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.update(0, END)
                e2.update(0, END)
                e3.update(0, END)
                e4.update(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            cnp_angajat = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from angajat where cnp_angajat = %s"
                val = (cnp_angajat,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("800x500")
        global e1
        global e2
        global e3
        global e4

        tk.Label(root, text="Angajati", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Cnp angajat").place(x=10, y=10)
        Label(root, text="Tip angajat").place(x=10, y=40)
        Label(root, text="Nume").place(x=10, y=70)
        Label(root, text="Prenume").place(x=10, y=100)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('cnp_angajat', 'tip_angajat', 'nume', 'prenume')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

#CLIENT
    elif cmb.get() == "Client":


        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_client'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['prenume'])
            e4.insert(0, select['nr_telefon'])
            e5.insert(0, select['id_locatie'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_client", "nume", "prenume", "nr_telefon", "id_locatie"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_client":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by id_client")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()

                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()


                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()

                if cmbb.get() == "nr_telefon":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by nr_telefon")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()


                if cmbb.get() == "id_locatie":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM client order by id_locatie")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                        mysqldb.close()
            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_client = e1.get()
            nume = e2.get()
            prenume = e3.get()
            nr_telefon = e4.get()
            id_locatie = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  client  (id_client, nume, prenume, nr_telefon, id_locatie) VALUES (%s, %s, %s, %s, %s)"
                val = (id_client, nume, prenume, nr_telefon, id_locatie)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_client, nume, prenume, nr_telefon, id_locatie FROM client")
            records = mycursor.fetchall()
            print(records)

            for i, (id_client, nume, prenume, nr_telefon, id_locatie) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_client, nume, prenume, nr_telefon, id_locatie))
                mysqldb.close()

        def update():
            id_client = e1.get()
            nume = e2.get()
            prenume = e3.get()
            nr_telefon = e4.get()
            id_locatie = e5.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  client set nume= %s,prenume= %s, nr_telefon=%s, id_locatie = %s where id_client= %s"
                val = (id_client, nume, prenume, nr_telefon, id_locatie)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_client = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from client where id_client = %s"
                val = (id_client,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Clienti", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Client").place(x=10, y=10)
        Label(root, text="Nume").place(x=10, y=40)
        Label(root, text="Prenume").place(x=10, y=70)
        Label(root, text="Nr Telefon").place(x=10, y=100)
        Label(root, text="id_locatie").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        e5 = Entry(root)
        e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_client', 'nume', 'prenume', 'nr_telefon', 'id_locatie')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)


 # FURNIZOR
    elif cmb.get() == "Furnizor":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_furnizor'])
            e2.insert(0, select['nume'])
            e3.insert(0, select['tip_furnizor'])
            e4.insert(0, select['oras'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("cnp_angajat", "tip_angajat", "nume", "prenume"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "cnp_angajat":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "tip_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by tip_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()


                if cmbb.get() == "nume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by nume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

                if cmbb.get() == "prenume":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM angajat order by prenume")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (cnp_angajat, tip_angajat, nume, prenume) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(cnp_angajat, tip_angajat, nume, prenume))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_furnizor = e1.get()
            nume = e2.get()
            tip_furnizor = e3.get()
            oras = e4.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  furnizor  (id_furnizor,nume,tip_furnizor,oras) VALUES (%s, %s, %s, %s)"
                val = (id_furnizor, nume, tip_furnizor, oras)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_furnizor,nume,tip_furnizor,oras FROM furnizor")
            records = mycursor.fetchall()
            print(records)

            for i, (id_furnizor, nume, tip_furnizor, oras) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_furnizor, nume, tip_furnizor, oras))
                mysqldb.close()

        def update():
            id_furnizor = e1.get()
            nume = e2.get()
            tip_furnizor = e3.get()
            oras = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                # sql = "Update  angajat set tip_angajat='%s', nume='%s', prenume='%s' where cnp_angajat= %s"
                Update = "Update furnizor set nume = '%s',tip_furnizor = '%s',oras = '%s' where id_furnizor = '%s'" % (nume, tip_furnizor, oras, id_furnizor)
                # val = (cnp_angajat, tip_angajat, nume, prenume)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.update(0, END)
                e2.update(0, END)
                e3.update(0, END)
                e4.update(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_furnizor = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from furnizor where id_furnizor = %s"
                val = (id_furnizor,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("800x500")

        tk.Label(root, text="Furnizor", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id furnizor").place(x=10, y=10)
        Label(root, text="Nume").place(x=10, y=40)
        Label(root, text="Tip Furnizor").place(x=10, y=70)
        Label(root, text="Oras").place(x=10, y=100)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_furnizor', 'nume', 'tip_furnizor', 'oras')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)


#LOCATIE

    elif cmb.get() == "Locatie":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_locatie'])
            e2.insert(0, select['tara'])
            e3.insert(0, select['oras'])
            e4.insert(0, select['cod_postal'])
            e5.insert(0, select['strada'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_locatie", "tara", "oras", "cod_postal", "strada"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_locatie":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by id_locatie")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

                if cmbb.get() == "tara":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by tara")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()


                if cmbb.get() == "oras":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by oras")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

                if cmbb.get() == "cod_postal":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by cod_postal")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()


                if cmbb.get() == "strada":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM locatie order by strada")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                        mysqldb.close()

            #print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_locatie = e1.get()
            tara = e2.get()
            oras = e3.get()
            cod_postal = e4.get()
            strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  locatie  (id_locatie, tara, oras, cod_postal, strada) VALUES (%s, %s, %s, %s, %s)"
                val = (id_locatie, tara, oras, cod_postal, strada)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_locatie, tara, oras, cod_postal, strada FROM locatie")
            records = mycursor.fetchall()
            print(records)

            for i, (id_locatie, tara, oras, cod_postal, strada) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_locatie, tara, oras, cod_postal, strada))
                mysqldb.close()

        def update():
            id_locatie = e1.get()
            tara = e2.get()
            oras = e3.get()
            cod_postal = e4.get()
            strada = e5.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  locatie set tara= %s,oras= %s, cod_postal=%s, strada = %s where id_locatie = %s"
                val = (id_locatie, tara, oras, cod_postal, strada)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_locatie = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from locatie where id_locatie = %s"
                val = (id_locatie,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Locatie", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Locatie").place(x=10, y=10)
        Label(root, text="Tara").place(x=10, y=40)
        Label(root, text="Oras").place(x=10, y=70)
        Label(root, text="Cod Postal").place(x=10, y=100)
        Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        e5 = Entry(root)
        e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_locatie', 'tara', 'oras', 'cod_postal', 'strada')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)
#PARCARE

    elif cmb.get() == "Parcare":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_parcare'])
            e2.insert(0, select['oras'])
            e3.insert(0, select['strada'])
            e4.insert(0, select['capacitate'])
            # e5.insert(0, select['strada'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_parcare", "oras", "strada", "capacitate"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_parcare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by id_parcare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitatea) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitatea))
                        mysqldb.close()

                if cmbb.get() == "oras":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by oras")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitatea) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitatea))
                        mysqldb.close()


                if cmbb.get() == "strada":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by strada")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitatea) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitatea))
                        mysqldb.close()

                if cmbb.get() == "capacitatea":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM parcare order by capacitatea")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_parcare, oras, strada, capacitatea) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_parcare, oras, strada, capacitatea))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_parcare = e1.get()
            oras = e2.get()
            strada = e3.get()
            capacitate = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  parcare  (id_parcare, oras, strada, capacitate) VALUES (%s, %s, %s, %s)"
                val = (id_parcare, oras, strada, capacitate)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_parcare, oras, strada, capacitate  FROM parcare")
            records = mycursor.fetchall()
            print(records)

            for i, (id_parcare, oras, strada, capacitate) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_parcare, oras, strada, capacitate))
                mysqldb.close()

        def update():
            id_parcare = e1.get()
            oras = e2.get()
            strada = e3.get()
            capacitate = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
               # sql = "Update  parcare set oras= %s, strada= %s, capacitate =%s where id_parcare= %s"
                #val = (oras, strada, capacitate, id_parcare)
                Update = "Update parcare set oras='%s', strada='%s', capacitate='%s' where id_parcare='%s'" % (
                    oras,strada, capacitate, id_parcare)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.update(0, END)
                e2.update(0, END)
                e3.update(0, END)
                e4.update(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_parcare = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from parcare where id_parcare = %s"
                val = (id_parcare,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Parcare", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Parcare").place(x=10, y=10)
        Label(root, text="Oras").place(x=10, y=40)
        Label(root, text="Strada").place(x=10, y=70)
        Label(root, text="Capacitate").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_parcare', 'oras', 'strada', 'capacitate')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)

#TRANSPORT

    elif cmb.get() == "Transport":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_transport'])
            e2.insert(0, select['tip_transport'])
            e3.insert(0, select['cantitate_marfa'])
            e4.insert(0, select['cnp_angajat'])
            # e5.insert(0, select['strada'])
        def having():

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT avg(cantitate_marfa), id_transport FROM transport HAVING avg(cantitate_marfa)>2500")
            #sa se afiseze cantitatea medie de marfa doar daca aceasta este mai mare de 2500

            records = mycursor.fetchall()
            print(records)

            for i, (id_transport, cantitate_marfa) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_transport, cantitate_marfa,))
                mysqldb.close()


        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_transport", "tip_transport", "cantitate_marfa", "cnp_angajat"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_transport":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "tip_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by tip_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()


                if cmbb.get() == "cantitate_marfa":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by cantitate_marfa")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "cnp_angajat":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM transport order by cnp_angajat")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_transport = e1.get()
            tip_transport = e2.get()
            cantitate_marfa = e3.get()
            cnp_angajat = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  transport  (id_transport, tip_transport, cantitate_marfa, cnp_angajat) VALUES (%s, %s, %s, %s)"
                val = (id_transport, tip_transport, cantitate_marfa, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_transport, tip_transport, cantitate_marfa, cnp_angajat  FROM transport")
            records = mycursor.fetchall()
            print(records)

            for i, (id_transport, tip_transport, cantitate_marfa, cnp_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_transport, tip_transport, cantitate_marfa, cnp_angajat))
                mysqldb.close()

        def update():
            id_transport = e1.get()
            tip_transport = e2.get()
            cantitate_marfa = e3.get()
            cnp_angajat = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                Update = "Update transport set tip_transport='%s', cantitate_marfa='%s', cnp_angajat='%s' where id_transport='%s'" % (
                    tip_transport, cantitate_marfa, cnp_angajat, id_transport)
                mycursor.execute(Update)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_transport = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from transport where id_transport = %s"
                val = (id_transport,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Transport", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Transport").place(x=10, y=10)
        Label(root, text="Tip Transport").place(x=10, y=40)
        Label(root, text="Cantitate Marfa").place(x=10, y=70)
        Label(root, text="CNP Angajat").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)
        Button(root, text="HAVING", command=having, height=2, width=15).place(x=720, y=200)

        cols = ('id_transport', 'tip_transport', 'cantitate_marfa', 'cnp_angajat')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)


        listBox.bind('<Double-Button-1>', GetValue)

#VEHICUL


    elif cmb.get() == "Vehicul":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            # e5.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_vehicul'])
            e2.insert(0, select['km'])
            e3.insert(0, select['capacitate_maxima'])
            e4.insert(0, select['id_parcare'])
            # e5.insert(0, select['strada'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("km", "capacitate_maxima", "id_parcare"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "km":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by km")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

                if cmbb.get() == "capacitate_maxima":
                    print("Capacitate maxima:")
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by capacitate_maxima")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

                if cmbb.get() == "id_parcare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM vehicul order by id_parcare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                        mysqldb.close()

        #print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.5", rely="0.1")

        def Add():
            id_vehicul = e1.get()
            km = e2.get()
            capacitate_maxima = e3.get()
            id_parcare = e4.get()
            # strada = e5.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  vehicul  (id_vehicul, km, capacitate_maxima, id_parcare) VALUES (%s, %s, %s, %s)"
                val = (id_vehicul, km, capacitate_maxima, id_parcare)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT *  FROM vehicul")
            records = mycursor.fetchall()
            print(records)

            for i, (id_vehicul, km, capacitate_maxima, id_parcare) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_vehicul, km, capacitate_maxima, id_parcare))
                mysqldb.close()

        def update():
            id_vehicul = e1.get()
            km = e2.get()
            capacitate_maxima = e3.get()
            id_parcare = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update vehicul set km= %s, capacitate_maxima = %s, id_parcare =%s where id_vehicul= %s"
                val = (km, capacitate_maxima, id_parcare, id_vehicul)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_vehicul = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from vehicul where id_vehicul = %s"
                val = (id_vehicul,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                # e5.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()



        root = Tk()
        root.geometry("900x500")

        tk.Label(root, text="Vehicul", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Vehicul").place(x=10, y=10)
        Label(root, text="KM").place(x=10, y=40)
        Label(root, text="Capacitate Maxima").place(x=10, y=70)
        Label(root, text="Id Parcare").place(x=10, y=100)
        # Label(root, text="Strada").place(x=10, y=130)
        # Label(root, text="Email").place(x=10, y=100)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        # e5 = Entry(root)
        # e5.place(x=130, y=130)
        # e5 = Entry(root)
        # e5.place(x=130, y=100)


        cols = ('id_vehicul', 'km', 'capacitate_maxima', 'id_parcare')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)
        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)
        # show()
        listBox.bind('<Double-Button-1>', GetValue)
        root.mainloop()

#GESTIONARE

    elif cmb.get() == "Gestionare":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_gestionare'])
            e2.insert(0, select['id_vehicul'])
            e3.insert(0, select['cnp_angajat'])

        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_gestionare", "id_vehicul", "cnp_angajat"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_gestionare":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM gestionare order by id_gestionare")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                        mysqldb.close()

                if cmbb.get() == "id_vehicul":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM gestionare order by id_vehicul")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                        mysqldb.close()

        def Add():
            id_gestionare = e1.get()
            id_vehicul = e2.get()
            cnp_angajat = e3.get()


            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  gestionare  (id_gestionare, id_vehicul, cnp_angajat) VALUES (%s, %s, %s)"
                val = (id_gestionare, id_vehicul, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_gestionare, id_vehicul, cnp_angajat FROM gestionare")
            records = mycursor.fetchall()
            print(records)

            for i, (id_gestionare, id_vehicul, cnp_angajat) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_gestionare, id_vehicul, cnp_angajat))
                mysqldb.close()

        def update():
            id_gestionare = e1.get()
            id_vehicul = e2.get()
            cnp_angajat = e3.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  gestionare set id_vehicul= %s,cnp_angajat where id_gestionare= %s"
                val = (id_gestionare, id_vehicul, cnp_angajat)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_gestionare = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from gestionare where id_gestionare = %s"
                val = (id_gestionare,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Gestionare", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id Gestionare").place(x=10, y=10)
        Label(root, text="Id Vehicul").place(x=10, y=40)
        Label(root, text="CNP Angajat").place(x=10, y=70)


        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_gestionare', 'id_vehicul', 'cnp_angajat')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

#CONTRACT

    elif cmb.get() == "Contract":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_contract'])
            e2.insert(0, select['id_furnizor'])
            e3.insert(0, select['id_transport'])
        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_contract", "id_furnizor", "id_transport"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_contract":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_contract")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()

                if cmbb.get() == "id_furnizor":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_furnizor")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()


                if cmbb.get() == "id_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM contract order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                        mysqldb.close()


            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")

        def Add():
            id_contract = e1.get()
            id_furnizor = e2.get()
            id_transport = e3.get()


            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  contract  (id_contract, id_furnizor, id_transport) VALUES (%s, %s, %s)"
                val = (id_contract, id_furnizor, id_transport)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_contract,id_furnizor, id_transport FROM contract")
            records = mycursor.fetchall()
            print(records)

            for i, (id_contract, id_furnizor, id_transport) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_contract, id_furnizor, id_transport))
                mysqldb.close()

        def update():
            id_contract = e1.get()
            id_furnizor = e2.get()
            id_transport = e3.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  contract set id_furnizor= %s,id_transport where id_contract= %s"
                val = (id_furnizor, id_transport, id_contract)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_contract = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from contract where id_contract = %s"
                val = (id_contract,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Contract", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Contract").place(x=10, y=10)
        Label(root, text="Id_furnizor").place(x=10, y=40)
        Label(root, text="Id_transport").place(x=10, y=70)


        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_contract', 'id_furnizor', 'id_transport')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

        root.mainloop()

    elif cmb.get() == "Factura":
        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select['id_factura'])
            e2.insert(0, select['data_emitere'])
            e3.insert(0, select['id_transport'])
            e4.insert(0, select['id_client'])


        def sort():
            # combobox pentru a alege ce sortez
            cmbb = ttk.Combobox(root, width="10", values=("id_factura", "data_emitere", "id_transport", "id_client"))

            def sorteaza():
                mydb = mysql.connector.connect(
                    host='localhost',
                    database='firma_transport',
                    password='ciscosecpa55',
                    user='root',
                )

                if cmbb.get() == "id_factura":
                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_factura")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

                if cmbb.get() == "data_emitere":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by data_emitere")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()


                if cmbb.get() == "id_transport":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_transport")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

                if cmbb.get() == "id_client":

                    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                                      database="firma_transport")
                    mycursor = mysqldb.cursor()
                    mycursor.execute("SELECT *  FROM factura order by id_client")
                    records = mycursor.fetchall()
                    print(records)

                    for i, (id_factura, data_emitere, id_transport, id_client) in enumerate(records, start=1):
                        listBox.insert("", "end", values=(id_factura, data_emitere, id_transport, id_client))
                        mysqldb.close()

            print("Sortare în terminal: ")
            cmbb.place(relx="0.4", rely="0.1")
            btn = ttk.Button(root, text="sorteaza", command=sorteaza)
            btn.place(relx="0.55", rely="0.1")


        def Add():
            id_factura = e1.get()
            data_emitere = e2.get()
            id_transport = e3.get()
            id_client = e3.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO  factura  (id_factura,data_emitere, id_client, id_transport) VALUES (%s, %s,%s, %s)"
                val = (id_factura, data_emitere, id_client, id_transport)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Adaugat cu succes...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)

                e1.focus_set()
            except Exception as e:
                print(e)

                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id_factura,data_emitere, id_client, id_transport FROM factura")
            records = mycursor.fetchall()
            print(records)

            for i, (id_factura, data_emitere, id_client, id_transport) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id_factura, data_emitere, id_client, id_transport))
                mysqldb.close()

        def update():
            id_factura = e1.get()
            data_emitere = e2.get()
            id_transport = e3.get()
            id_client = e4.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "Update  factura set data_emitere=%s, id_transport= %s,id_client=%s where id_factura= %s"
                val = (data_emitere, id_transport, id_client, id_factura)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Update realizat...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            id_factura = e1.get()

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="ciscosecpa55",
                                              database="firma_transport")
            mycursor = mysqldb.cursor()

            try:
                sql = "delete from factura where id_factura = %s"
                val = (id_factura,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Sters cu succes...")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()

            except Exception as e:

                print(e)
                mysqldb.rollback()
                mysqldb.close()

        root = Tk()
        root.geometry("900x500")
        tk.Label(root, text="Factura", fg="red", font=(None, 20)).place(x=500, y=5)

        tk.Label(root, text="Id_Factura").place(x=10, y=10)
        tk.Label(root, text="Data Emitere").place(x=10, y=30)
        Label(root, text="Id_transport").place(x=10, y=60)
        Label(root, text="Id_client").place(x=10, y=90)

        e1 = Entry(root)
        e1.place(x=130, y=10)

        e2 = Entry(root)
        e2.place(x=130, y=40)

        e3 = Entry(root)
        e3.place(x=130, y=70)

        e4 = Entry(root)
        e4.place(x=130, y=100)

        Button(root, text="Add", command=Add, height=2, width=15).place(x=20, y=200)
        Button(root, text="update", command=update, height=2, width=15).place(x=180, y=200)
        Button(root, text="Delete", command=delete, height=2, width=15).place(x=320, y=200)
        Button(root, text="Sort", command=sort, height=2, width=15).place(x=460, y=200)
        Button(root, text="SHOW", command=show, height=2, width=15).place(x=580, y=200)

        cols = ('id_factura', 'data_emitere', 'id_furnizor', 'id_transport')
        listBox = ttk.Treeview(root, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)
            listBox.place(x=10, y=250)

        #show()
        listBox.bind('<Double-Button-1>', GetValue)

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")


cmb.place(relx="0.1", rely="0.1")

btn = ttk.Button(root, text="Alege Tabelul", command=checkcmbo)
btn.place(relx="0.5", rely="0.1")

root.mainloop()
