umur = int(input ("masukan umur anda"))

if umur < 15:
    print("anda masih anak anak")
elif umur >= 15 and umur < 18:
    print("anda remaja")
elif umur >= 18 and umur < 60:
    print("anda dewasa")
else:
    print("anda sudah tua")