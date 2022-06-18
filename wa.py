import request,os

url_api_spam_wa = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

os.system("clear")
os.system("figlet Spam-Wa Official XRazzel"
print("[-] Creator: XRazzel")
print("[-] Tolls: Spam Wa")
nomor = input("\n[?] input nomor : ")
jumlah = input("[?] input jumlah : ")
print()
data = {
  "nomor": nomor
  }
  for free_tutorial in range(int(jumlah)):
    sanz = request.get(url_api_spam_wa, parms=data
    if "Berhasil Dong ! .... Terlalu Easy Dek." in sanz.>
            print("[+] Berhasil Dong" )
    else:
            print("[!] Gagal Goblok") 
