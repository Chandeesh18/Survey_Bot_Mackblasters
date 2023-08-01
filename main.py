import speech_recognition as sr     # For sppech recognition using google ai
import pyttsx3                      # For voice output
import os
import numpy as np                  # To generate random choice

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gender_guesser.detector import Detector 
from nlp_pipeline.chatbot import chatbot

# Download the VADER lexicon
nltk.download('vader_lexicon')
nltk.download('punkt')

class ChatBot():
    def __init__(self):
        print("----- MACKCars Survey Bot -----")
    # Sets Name of chatbot
    def set_name(self,name):
        self.name = name
    # Retuens Name of chatbot
    def get_name(self):
        return self.name
    #quality
    def set_quality(self,quality):
        self.quality = quality
    # Returns quality
    def get_quality(self):
        return self.quality

    def set_performance(self,performance):
        self.performance = performance
    # Returns quality
    def get_performance(self):
        return self.performance

    def set_feel(self,feel):
        self.feel = feel
    # Returns quality
    def get_feel(self):
        return self.feel

    def set_safety(self,safety):
        self.safety = safety
    # Returns quality
    def get_safety(self):
        return self.safety

    def set_recommend(self,recommend):
        self.recommend = recommend
    # Returns quality
    def get_recommend(self):
        return self.recommend

    def set_improvement(self,improvement):
        self.improvement = improvement
    # Returns quality
    def get_improvement(self):
        return self.improvement
    #return sentimental analysis result
    def get_sentiment(self, text):
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        # Positive sentiment: compound score >= 0.05
        # Negative sentiment: compound score <= -0.05
        # Neutral sentiment: -0.05 < compound score < 0.05
        if sentiment_scores['compound'] >= 0.05:
            return "positive"
        elif sentiment_scores['compound'] <= -0.05:
            return "negative"
        else:
            return "neutral"

    # Function to detect emotions based on keywords
    def detect_emotion(self, text):
        text_lower = text.lower()
        if any(keyword in text_lower for keyword in ['happy', 'joy', 'excited', 'satisfied']):
            return "happy"
        elif any(keyword in text_lower for keyword in ['sad', 'unhappy', 'disappointed', 'miserable']):
            return "sad"
        elif any(keyword in text_lower for keyword in ['angry', 'frustrated', 'annoyed', 'mad']):
            return "angry"
        else:
            return "neutral"

    # Return gender based on the name
    def get_gender_from_name(self, name):
        detector = Detector(case_sensitive=False)
        gender = detector.get_gender(name)
        if gender == "male":
            return "male"
        elif gender == "female":
            return "female"
        else:
            return "unknown"

    # Converts Speech to text
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Currently Listening...")
            recognizer.adjust_for_ambient_noise(mic,duration=1)
            audio = recognizer.listen(mic,timeout=15)
            text = "Error"
        try:
            text = recognizer.recognize_google(audio)
            print("Me -> ", text)
            return text

        except sr.RequestError as e:
            print("404 -> Could not request results; {0}".format(e))
            return text

        except sr.UnknownValueError:
            print("404 -> Unknown error occurred")
            return text
    # Converts text to speech
    def text_to_speech(self,text):
        print("AI -> ", text)
        speaker = pyttsx3.init()
        voice = speaker.getProperty('voices')
        speaker.setProperty('voice', voice[1].id)
        speaker.say(text)
        speaker.runAndWait()
    # Returnes NLP response
    def chat(self,text):
        chat = chatbot(text)
        return chat


if __name__ == "__main__":
    ai = ChatBot()

    while True:
        ai.text_to_speech("Hi there i'm here for taking the survey about the car")
        action = int(2)
        
        if action == 2:
            ai.text_to_speech("can you say your name?")

            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_name(name=res)

            ai.text_to_speech("How was the quality of service ?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_quality(quality=res)

            ai.text_to_speech("Are you satisfied with overall performance of your vehicle")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_performance(performance=res)

            ai.text_to_speech("How do you feel about the car?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_feel(feel=res)

            ai.text_to_speech("Are you satisified with the safety features of your vehicle?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_safety(safety=res)

            ai.text_to_speech("Will you recommend others to buy this model?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_recommend(recommend=res)

            ai.text_to_speech("Any suggestion for improvement?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_improvement(improvement=res)

            sentiment_result = ai.get_sentiment(
                f"{ai.get_name()} said, Quality: {ai.get_quality()}, "
                f"Performance: {ai.get_performance()}, Feel: {ai.get_feel()}, "
                f"Safety: {ai.get_safety()}, Recommend: {ai.get_recommend()}, "
                f"Improvement: {ai.get_improvement()}"
            )

            # Detect emotion in the feedback
            emotion_result = ai.detect_emotion(
                f"{ai.get_quality()} {ai.get_performance()} {ai.get_feel()} "
                f"{ai.get_safety()} {ai.get_recommend()} {ai.get_improvement()}"
            )

            ai.text_to_speech(f"The sentiment analysis result for your feedback is {sentiment_result}.")
            ai.text_to_speech(f"The emotion detected in your feedback is {emotion_result}.")
            
             # Get gender from the user's name
            gender = ai.get_gender_from_name(ai.get_name())
            if gender:
                ai.text_to_speech(f"Based on your name, I detected that you are probably {gender}.")
            else:
                ai.text_to_speech("I could not determine your gender from your name.")

            ai.text_to_speech("Thats all about the survey,Great time with you")
            ai.text_to_speech("Have a great day!!")
            ai.text_to_speech("Bye bye")

        break
        #     while True:
        #         res = ai.speech_to_text()
        #         if any(i in res for i in ["thank","thanks"]):
        #             res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
        #         elif any(i in res for i in ["your name","who are you"]):
        #             res = "I'm " + ai.get_name()
        #             ai.text_to_speech(res)
        #         elif any(i in res for i in ["exit","close","quit","bye"]):
        #             break
        #         else:   
        #             if res=="Error":
        #                 res="Sorry, come again?"
        #             else:
        #                 output = ai.chat(res)
        #                 ai.text_to_speech(output)
        # # Good bye text
        # res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
        # ai.text_to_speech(res)
        # break
            
