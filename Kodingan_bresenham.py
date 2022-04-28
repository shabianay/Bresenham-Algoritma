#import library/package yang dibutuhkan
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Inisialisasi Fungsi
def init(): #Inisialisasi Fungsi
    glClearColor(0.0,0.0,0.0,1.0) #Menghapus layar dan mengatur warna
    gluOrtho2D(0,100,0,100) #Mengatur sudut
    

def plotLine(x1,y1,x2,y2):
    #Melakukan perhitungan bresenham algoritma
    m = 2 * (y2 - y1) #mencari m
    pk = m - (x2 - x1) #mencari pk
    y=y1 

    #Membuat garis
    glClear(GL_COLOR_BUFFER_BIT) #Membersihkan layar latar belakang dengan warna hitam
    glColor3f(1.0,0.0,0.0) #Digunakan untuk menentukan warna garis/titik, menggunakan warna merah
    glPointSize(10.0) #Mengatur besar titik yang akan digambar
    glBegin(GL_POINTS) #Menggambar titik

    #looping dari langkah ke 1 sampai langkah terakhir
    for x in range(x1,x2+1):
        #Pilih pixel yang akah digambar
        glVertex2f(x,y)
        pk =pk + m
        if (pk>= 0):
            y=y+1
            pk =pk - 2 * (x2 - x1)
    glEnd()
    glFlush()

def main():
    #Memberikan menu atau pilihan
    choice = 0
    while (choice != 2):
        choice = input("Please Choose \n\t1. Baris Baru\n\t2. Exit\n")
        if int(choice) == 1: #jika memilih no 1 pengguna diwajibkan untuk mengisi nilai x1,y1,x2,y2
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            print("starting window....")
            glutInit(sys.argv) #inisialisasi glut
            glutInitDisplayMode(GLUT_RGB) #inisialisasi tipe display glut
            glutInitWindowSize(500,500) #inisialisasi ukuran layar glut
            glutInitWindowPosition(0,0) #inisiasliasi posisi layar glut
            glutCreateWindow("Bresenham Algorithm") #inisialisasi pembuatan window
            glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2))
            glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))
            init()
            glutMainLoop()
        else: #Ketika memilih no 2 maka akan mengulang untuk mengisi
            print("Invalid choice")
            choice = 0

main()