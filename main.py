import texts, weather

send = weather.checkTemps()

if send == True:
    texts.sendMessage()
else:
    exit()