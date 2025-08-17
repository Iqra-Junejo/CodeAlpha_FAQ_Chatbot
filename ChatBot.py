import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import re
import difflib
import random

class FAQChatbot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 Intelligent FAQ Chatbot - CodeAlpha")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a2e')
        
        # FAQ Database (kept exactly same as your original)
        self.faq_data = {
            'questions': [
                "What is CodeAlpha?",
                "How long is the internship?",
                "What are the internship requirements?",
                "How do I submit my projects?",
                "What certificates will I receive?",
                "Do I need prior experience?",
                "What programming languages are required?",
                "How many tasks do I need to complete?",
                "Can I get a job after the internship?",
                "What is the selection criteria?",
                "How do I contact CodeAlpha?",
                "What are the internship perks?",
                "Is this internship paid?",
                "Can I work remotely?",
                "What kind of projects will I work on?",
                "How do I apply for the internship?",
                "What is the mentorship like?",
                "Can I extend my internship?",
                "What skills will I gain?",
                "How competitive is the selection process?"
            ],
            'answers': [
                "CodeAlpha is a leading software development company dedicated to driving innovation and excellence across emerging technologies. We offer internship programs in various domains including AI, web development, and more.",
                "The internship duration varies by program, but typically ranges from 4-8 weeks. You'll have flexible deadlines to complete your assigned tasks.",
                "To complete the internship, you need to: 1) Complete 2-3 tasks from your domain, 2) Upload code to GitHub, 3) Share progress on LinkedIn, 4) Submit through our form, 5) Create project explanation videos.",
                "You submit projects through the submission form shared in your WhatsApp group. Make sure to upload your complete source code to GitHub in a repository named 'CodeAlpha_ProjectName'.",
                "You'll receive: Internship Offer Letter, QR Verified Completion Certificate, Unique ID Certificate, Letter of Recommendation (based on performance), and resume building support.",
                "No prior experience is required! Our internship is designed for students and beginners. We provide mentorship and guidance throughout the program.",
                "For AI internship: Python is the primary language. You'll work with libraries like TensorFlow, PyTorch, OpenCV, NLTK, and scikit-learn depending on your chosen tasks.",
                "You need to complete a minimum of 2-3 tasks from your domain's task list. Completing only 1 task is considered incomplete and won't qualify for certification.",
                "Yes! We provide job opportunities and placement support for outstanding performers. We also help with resume building and interview preparation.",
                "Selection is based on your application, interest in the domain, and commitment to complete the program. We welcome students from all backgrounds.",
                "Website: www.codealpha.tech, WhatsApp: +91 8052293611, Email: services@codealpha.tech. We're always here to help!",
                "Internship perks include: Offer letter, completion certificate, unique ID certificate, recommendation letter, job opportunities, placement support, and resume building assistance.",
                "This is an unpaid internship focused on providing valuable learning experience, skill development, and career opportunities in the tech industry.",
                "Yes! This is a remote internship. You can work from anywhere and manage your own schedule while meeting the project deadlines.",
                "You'll work on real-world projects like AI chatbots, language translators, object detection systems, music generation, web applications, and mobile apps depending on your domain.",
                "Applications are typically announced on our website and social media. Follow our LinkedIn page @CodeAlpha for updates on new internship batches.",
                "You'll receive expert mentorship from industry professionals. Our mentors guide you through project development, provide feedback, and help solve technical challenges.",
                "Extension depends on your performance and project requirements. Outstanding interns may be offered extended opportunities or advanced projects.",
                "You'll gain hands-on experience in your chosen domain, project management skills, GitHub proficiency, LinkedIn networking, technical documentation, and industry best practices.",
                "The selection process is moderately competitive. We focus more on enthusiasm and willingness to learn rather than just technical expertise."
            ]
        }

        self.create_widgets()
        self.add_welcome_message()
    
    def preprocess(self, text):
        """Lowercase and clean text"""
        return re.sub(r'[^a-zA-Z\s]', '', text.lower())
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root, text="🤖 CodeAlpha FAQ Chatbot",
            font=('Arial', 18, 'bold'), bg='#1a1a2e', fg='#00d4ff'
        )
        title_label.pack(pady=15)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.root, height=20, width=80, font=('Arial', 11),
            bg='#16213e', fg='white', wrap=tk.WORD, state='disabled'
        )
        self.chat_display.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Input area
        input_frame = tk.Frame(self.root, bg='#1a1a2e')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        self.user_input = tk.Entry(
            input_frame, font=('Arial', 12),
            bg='#16213e', fg='white', insertbackground='white', relief='flat'
        )
        self.user_input.pack(side='left', fill='x', expand=True, padx=(0,10))
        self.user_input.bind('<Return>', self.send_message)
        
        send_btn = tk.Button(
            input_frame, text="Send 📤",
            font=('Arial', 11, 'bold'),
            bg='#00d4ff', fg='#1a1a2e',
            command=self.send_message, relief='flat', padx=20
        )
        send_btn.pack(side='right')
    
    def add_welcome_message(self):
        welcome_msg = """👋 Welcome to CodeAlpha FAQ Chatbot!

Ask me about:
• Internship requirements  
• Project submission  
• Certificates  
• Perks & Mentorship  
• Contact info  
"""
        self.display_message("Bot", welcome_msg, "#00d4ff")
    
    def send_message(self, event=None):
        user_msg = self.user_input.get().strip()
        if not user_msg:
            return
        self.display_message("You", user_msg, "#ffffff")
        self.user_input.delete(0, tk.END)
        
        bot_reply = self.get_response(user_msg)
        self.display_message("Bot", bot_reply, "#00d4ff")
    
    def get_response(self, msg):
        msg = self.preprocess(msg)
        questions = [self.preprocess(q) for q in self.faq_data['questions']]
        
        # Find closest match using difflib
        best_match = difflib.get_close_matches(msg, questions, n=1, cutoff=0.3)
        
        if best_match:
            idx = questions.index(best_match[0])
            return self.faq_data['answers'][idx]
        else:
            return random.choice([
                "🤔 I’m not sure about that. Can you rephrase?",
                "I don’t have info on that, please contact CodeAlpha directly.",
                "Hmm... I couldn’t find a match. Try asking in a different way."
            ])
    
    def display_message(self, sender, msg, color):
        self.chat_display.config(state='normal')
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_display.insert(tk.END, f"\n{sender} ({timestamp}):\n", "tag")
        self.chat_display.insert(tk.END, f"{msg}\n", "msg")
        self.chat_display.tag_config("tag", foreground=color, font=('Arial', 10, 'bold'))
        self.chat_display.tag_config("msg", foreground=color, font=('Arial', 11))
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FAQChatbot()
    app.run()
