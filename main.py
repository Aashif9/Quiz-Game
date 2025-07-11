import win32com.client as wincl
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak("This is Done by Aashif")
spk.Speak("Welcome to Quiz Game")
print("Welcome to Quiz Game")
spk.Speak("Do you want to start the game:")
print("Do you want to start the game:(Y||N):")
score=0
option=input()
while option.lower()=='y':
    spk.Speak("Your first question:")
    print("1. Who is the first Prime Minister of independent India?\nA. Jawaharlal Nehru\nB. Mahatma Gandhi\nC. Sardar Patel\nD. Rajendra Prasad")
    spk.Speak("1. Who is the first Prime Minister of independent India? A. Jawaharlal Nehru B. Mahatma Gandhi C. Sardar Patel D. Rajendra Prasad")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='a':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your second question:")
    print("2. Which Indian state is known as the 'Land of Five Rivers'?\nA. Haryana\nB. Punjab\nC. Gujarat\nD. Rajasthan")
    spk.Speak("2. Which Indian state is known as the Land of Five Rivers? A. Haryana B. Punjab C. Gujarat D. Rajasthan")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your Third question:")
    print("3. What is the national currency of India?\nA. Taka\nB. Rupee\nC. Dinar\nD. Yen")
    spk.Speak("3. What is the national currency of India? A. Taka B. Rupee C. Dinar D. Yen")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your fourth question:")
    print("4. Which city is known as the Silicon Valley of India?\nA. Hyderabad\nB. Mumbai\nC. Bengaluru\nD. Pune")
    spk.Speak("4. Which city is known as the Silicon Valley of India? A. Hyderabad B. Mumbai C. Bengaluru D. Pune")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='c':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your fifth question:")
    print("5. Who is known as the Missile Man of India?\nA. Vikram Sarabhai\nB. A.P.J. Abdul Kalam\nC. Homi Bhabha\nD. C.V. Raman")
    spk.Speak("5. Who is known as the Missile Man of India? A. Vikram Sarabhai B. A.P.J. Abdul Kalam C. Homi Bhabha D. C.V. Raman")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your sixth question:")
    print("6. What is the national sport of India?\nA. Cricket\nB. Hockey\nC. Football\nD. Kabaddi")
    spk.Speak("6. What is the national sport of India? A. Cricket B. Hockey C. Football D. Kabaddi")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your seventh question:")
    print("7. Which is the longest river in India?\nA. Ganga\nB. Yamuna\nC. Brahmaputra\nD. Godavari")
    spk.Speak("7. Which is the longest river in India? A. Ganga B. Yamuna C. Brahmaputra D. Godavari")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='a':
        score+score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your eighth question:")
    print("8. In which year did India become a republic?\nA. 1947\nB. 1950\nC. 1949\nD. 1952")

    spk.Speak("8. In which year did India become a republic? A. 1947 B. 1950 C. 1949 D. 1952")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        break
    spk.Speak("Your ninth question:")
    print("9. Who wrote the Indian National Anthem?\nA. Bankim Chandra Chatterjee\nB. Rabindranath Tagore\nC. Subhash Chandra Bose\nD. Sarojini Naidu")
    spk.Speak("9. Who wrote the Indian National Anthem? A. Bankim Chandra Chatterjee B. Rabindranath Tagore C. Subhash Chandra Bose D. Sarojini Naidu")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='b':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
    spk.Speak("Your tenth question:")
    print("10. How many states are there in India (as of 2024)?\nA. 28\nB. 29\nC. 30\nD. 31")
    spk.Speak("10. How many states are there in India as of 2024? A. 28 B. 29 C. 30 D. 31")
    print("Enter your option:")
    choosen=input()
    if choosen.lower()=='a':
        score=score+100
        spk.Speak("Correct answer")
    else:
        spk.Speak("Wrong Answer")
        break
spk.Speak(f"Your total score:{score}")
print("Your total score:{score}")
spk.Speak("Thanks for participating")