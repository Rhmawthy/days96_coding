'''Alga mempunyai bola sekantong bola bermacam macam. Banyak bola dengan masing - masing warna dalam kantong tersebut di tunjukkan dalam grafik 

  
  6.   |  
       |
  5.   |       |
       |       |
  4.   |       |
       |       |
  3.   |       |              |
       |       |              |
  2.   |       |       |      |
       |       |       |      |
  1.   |       |       |      |       |
       |       |       |      |       |
  0.   |       |       |      |       |
     merah. coklat.  biru    ungu.  hijau

"jika warna bola yang di ambil Alga merupakan inputan, berapa peluan bola yang di terambil ?'''

bola = input("masukkan warna bola :")

jumlah =6+5+2+3+1

if bola == "merah" :
	peluang = 6 / jumlah 
	print("peluang bola warna merah",peluang)
	
elif bola == "coklat" :
	peluang = 5 / jumlah
	print("peluang bola warna coklat",peluang)
	
elif bola == "ungu" :
	peluang = 3 / jumlah
	print("peluang bola warna ungu",peluang)
		
elif bola == "biru" :
	peluang = 2 / jumlah
	print("peluang bola warna biru",peluang)
		
elif bola == "hijau" :
	peluang = 1 / jumlah
	print("peluang bola warna hijau",peluang)
else:
	print("masukkan warna bola yang tersedia")
	
		
