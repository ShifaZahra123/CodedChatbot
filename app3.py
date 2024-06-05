import streamlit as st
import re
import random

class RuleBot:
    ### Potential Negative Responses
    negative_responses = ("no", "nope", "nah", "not a chance", "sorry")
    ### Exit Conversation Keywords
    exit_commands = ("quit", "exit", "bye", "later", "pause", "goodbye")
    ### Random starter
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Does Earth have a leader?",
        "What do you like to do in your free time?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )
    ### Logic of the entire code
    def __init__(self):
        self.alienbabble = {
            'describe_plannet_intent': r'.*\byour planet\b.*',
            'answer_why_intent': r'why\sare.*',
            'about_lcwu': r'.*\blcwu\b.*',
            'about_lcwuadmissions': r'.*\blcwuadmissions\b.*'
        }

    def greet(self, name):
        self.name = name
        return random.choice(self.random_questions)

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply in command:
                return True
        return False

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == 'describe_plannet_intent':
                    return self.describe_plannet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_lcwu':
                    return self.about_lcwu()
                elif intent == 'about_lcwuadmissions':
                    return self.about_lcwuadmissions()
        return self.no_match_intent()

    def describe_plannet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.\n",
                     "I am from Opidipus, the capital of the Wayward Galaxies.\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace.\nI am here to collect data on your planet and its inhabitants.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)

    def about_lcwu(self):
        responses = ("Lahore College for Women University is Asia's biggest women's university.\n",
                     "Its teachers are known for being talented, cooperative, and skilled.\n")
        return random.choice(responses) + " Would you like to know more about LCWU?\n"

    def about_lcwuadmissions(self):
        responses = ("Admissions at LCWU are currently ongoing.\n",
                     "The process of accepting applications or allowing people to enroll in LCWU is currently happening.\n",
                     "Individuals have the opportunity to apply or enroll at this time.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Please tell me more.\n", "Tell me more.\n", "Why did you say that?\n", "I see. Can you elaborate?\n",
                     "Interesting. Can you tell me more?\n", "I see.\n", "How did you think?\n", "Why?\n",
                     "How do you think I feel when you say that?\n")
        return random.choice(responses)

AlienBot = RuleBot()

def main():
    st.title("Chat with RuleBot")
    
    # Initialize session state variables
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "history" not in st.session_state:
        st.session_state.history = []
    if "step" not in st.session_state:
        st.session_state.step = "greet"

    if st.session_state.step == "greet":
        st.session_state.name = st.text_input("What is your name?")
        if st.session_state.name:
            greeting = AlienBot.greet(st.session_state.name)
            st.session_state.history.append(f"RuleBot: {greeting}")
            st.session_state.step = "chat"

    if st.session_state.step == "chat":
        user_input = st.text_area("You: ", key="user_input")
        if st.button("Send"):
            if user_input:
                st.session_state.history.append(f"You: {user_input}")
                bot_response = AlienBot.match_reply(user_input.lower())
                st.session_state.history.append(f"RuleBot: {bot_response}")

    for line in st.session_state.history:
        st.write(line)

if __name__ == "__main__":
    main()
