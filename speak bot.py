import pyttsx3
command=pyttsx3.init(driverName='sapi5')
print("Hi im am a roboo speaker created by Arshit") 
while True:
    m=input("what do you want me to speak-->")
    command.say(m)
    command.runAndWait()