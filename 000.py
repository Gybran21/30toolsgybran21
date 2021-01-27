import os, sys

print ("\033[1;32mMASUKAN KODE LICENSI)")

print ("\033[1;32mATAU HUBUNGI LANGSUNG FAN VALDER ")

print ("\033[1;32mKONTAK 087744768614")

print ("CTRL + Z TO EXIT ")

print ("===================================")

username = 'FAN VALDER'

password = '7467GT02'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSAMPAI JUMPA",

			sys.exit()



		else:

			print "\032[1;32mSORYY GAN PASSWORD NYA SALAH !!!\033[00m"

			print "LOGIN ULANG\n"

			restart()



	else:

		print "\033[1;32mSORYY GAN USERNAME SALAH\033[00m"

		print "LOGIN ULANG\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

