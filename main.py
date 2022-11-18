import sys
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts 
import nltk
 
nltk.download('omw-1.4')

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)




def hello():
	speaker.say('Greeting master Welcome to VBM')
	speaker.say('I"m here for mainly three functions 1 inquiry about campus, 2 inquiry about addmission, 3 inquiry about Students')
	speaker.say('so what can i do for you?')
	speaker.runAndWait()

def about():
	speaker.say('I am bvm smart reception assistant')
	speaker.say('I am here to help you.')
	speaker.runAndWait()

def made():
	speaker.say('I am made by BVM Computer Students')
	speaker.runAndWait()

def addmission():
	speaker.say('Please visit website of Birla Vidya mandir Nainital www.birlavidyamandir.com')
	speaker.say('At the home page you will find the Registration Form')
	speaker.say('Download the Registration Form and take a printout of it  Fill all the details carefully then submit to BVM office.')
	speaker.say("Thank you")
	speaker.runAndWait()

def tanmay():
	speaker.say('His name is Tanmay Prakash and Folio id is 2196111 and class is 9th A')
	speaker.say("He live in Tilak House and House master name is Mister Brijesh Pandey")
	speaker.say("House master contact number is 9876890012")
	speaker.say("Thank you")
	speaker.runAndWait()

def kartikey():
	speaker.say('His name is Kartikey Yadav and Folio id is 2215064 and class is 10th D')
	speaker.say("He live in Tagore House and House master name is Mister A N Mishra")
	speaker.say("House master contact number is 9811190012")
	speaker.say("Thank you")
	speaker.runAndWait()

def umang():
	speaker.say('This is Umang Patel and Folio id is 3256780 and class is 11th B')
	speaker.say("He live in Tagore House and House master name is Mister Ramesh Verma")
	speaker.say("House master contact number is 9911190012")
	speaker.say("Thank you")
	speaker.runAndWait()

def raghav():
	speaker.say('This is Raghav and his Folio id is 1298022 and class is 12th D')
	speaker.say("He live in Tagore House and House master name is Mister Ram Mishra")
	speaker.say("House master contact number is 9811190011")
	speaker.say("Thank you")
	speaker.runAndWait()

def folio():
	speaker.say("Would you like to inquiry about student by saying its folio ID")
	speaker.runAndWait()

def thanks():
	speaker.say('My plasure always at your service')
	speaker.runAndWait()

def history():
	speaker.say("This is brief about BVM history , Birla Vidya Mandir came into existence in 1947, when Shree G. D. Birla bought the estate")
	speaker.say("Before India achieved its independence, Pant wanted to start a public school")
	speaker.say("a donation from Ghanshyam Das Birla, a philanthropist and industrialist, made this possible")	
	speaker.say("Thank you")
	speaker.runAndWait()

def campus():
	speaker.say('BVM campus mainly categories in 1 Dispensary 2 Fields 3 Houses 4 Senior Academic block 5 Junior Academic block ')
	speaker.say('Would you like to know about any ?')
	speaker.say("Thank you")
	speaker.runAndWait()

def fields():
	speaker.say("In our campus we have total two play grounds, three basketball courts and 1 gym hall. ")
	speaker.say("For more information regarding them you can contact field activity incharge  Mister P.R.S. Kirola in the given number 98745661230")
	speaker.say("Thank you")
	speaker.runAndWait()

def house():
	speaker.say("Birla vidya mandir campus has total 10 Houses 5 in junior Section and 5 in seniors Section")
	speaker.say("Junior Houses are Gandhi House,Raman House , Radha Krishnan House,Patel House and Subhash House")
	speaker.say("Senior Houses are Vivekanand House,Tagore House,Tilak House,Punt House and Nehru House")
	speaker.say("Thank you")
	speaker.runAndWait()

def srSchool():
	speaker.say("In Senior Academic block there are total 12 classrooms, 1 library, 1 Lecture room, 1 auditorium, 2 computer lab and 1 lab each for physics, chemistry, bio, accounts and math")
	speaker.say("For more query about senior section you can contact to dean of studies Mistar Rakesh Molasi ")
	speaker.say("Thank you")
	speaker.runAndWait()

def jrSchool():
	speaker.say("In Junior Academic block there are total 12 classrooms, 1 library, 1 snooker room, 1 computer lab")
	speaker.say("For more query about Junior section you can contact to the Head Master Mistar Ajay Sharma")
	speaker.say("Thank you")
	speaker.runAndWait()
	
def dispensary():
	speaker.say("BVM school dispensary is having a Doctor, a Nurse and a Pharmacist")
	speaker.say('dispensary contact number is 9800341210')
	speaker.say("Thank you")
	speaker.runAndWait()

def quit():
	speaker.say("Nice to meet you, have good time, good bye")
	speaker.runAndWait()
	sys.exit(0)


mapping = {
	"greeting":hello,
	"exit":quit,
	"about":about,
	"built":made,
	"addmission":addmission,
	"portfolio":folio,
	"tanmay":tanmay,
	"kartikey":kartikey,
	"umang":umang,
	"raghav":raghav,
	"thanks":thanks,
	"history":history,
	"campus":campus,
	"dispensary":dispensary,
	"jrSchool":jrSchool,
	"srSchool":srSchool,
	"house":house,
	"fields":fields

}

assistant = GenericAssistant('intents.json', intent_methods=mapping)
assistant.train_model()


while True:

	try:
		with speech_recognition.Microphone() as mic:

			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio = recognizer.listen(mic)

			message = recognizer.recognize_google(audio)
			message = message.lower()

		assistant.request(message)

	except speech_recognition.UnknownValueError:
		recognizer = speech_recognition.Recognizer()

