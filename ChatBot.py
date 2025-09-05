import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import re
import difflib
import random

class FAQChatbot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 Cybersecurity FAQ Chatbot")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a2e')
        
        # Cybersecurity FAQ Database
        self.faq_data = {
            'questions': [
                "What is cybersecurity?",
                "Why is cybersecurity important?",
                "What are common cyber threats?",
                "How can I protect my passwords?",
                "What is phishing?",
                "What is two-factor authentication (2FA)?",
                "How can I secure my Wi-Fi?",
                "What is a firewall?",
                "What is malware?",
                "How do I recognize a phishing email?",
                "What is ransomware?",
                "How often should I update my software?",
                "What is social engineering?",
                "What is encryption?",
                "How can I browse safely online?",
                "What are the best practices for email security?",
                "How do I protect myself on social media?",
                "What is a VPN and why use it?",
                "What should I do if I suspect a cyber attack?",
                "What careers are there in cybersecurity?"
            ],
            'answers': [
                "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks, unauthorized access, and damage.",
                "It is important because it helps safeguard sensitive data, financial information, and critical infrastructure from cybercriminals.",
                "Common threats include malware, phishing, ransomware, denial-of-service attacks, and insider threats.",
                "Use strong, unique passwords, enable two-factor authentication, and avoid reusing the same password across accounts.",
                "Phishing is a type of cyber attack where attackers trick users into revealing sensitive information by posing as trusted entities, usually via email or messages.",
                "Two-factor authentication (2FA) adds an extra security layer by requiring a second form of verification (like an SMS code or app confirmation) in addition to your password.",
                "Secure Wi-Fi by changing the default router password, enabling WPA3 or WPA2 encryption, and hiding the network SSID if possible.",
                "A firewall is a security system that monitors and controls incoming and outgoing network traffic based on security rules.",
                "Malware is malicious software designed to disrupt, damage, or gain unauthorized access to a computer system.",
                "Check for suspicious senders, poor grammar, urgent messages asking for action, or links/attachments you weren’t expecting.",
                "Ransomware is malware that encrypts your files and demands payment (usually in cryptocurrency) to unlock them.",
                "Update your software regularly, ideally enabling automatic updates to patch vulnerabilities as soon as fixes are released.",
                "Social engineering is the manipulation of people into sharing confidential information by exploiting human psychology rather than hacking systems.",
                "Encryption is the process of converting data into a coded format to prevent unauthorized access.",
                "Use HTTPS websites, avoid clicking unknown links, don’t download from suspicious sources, and use an updated browser and antivirus.",
                "Avoid opening suspicious attachments, verify senders, and don’t click on unknown links. Enable spam filters and use encryption when needed.",
                "Limit personal information shared, enable privacy settings, avoid public profiles, and be cautious of unknown friend requests.",
                "A VPN (Virtual Private Network) hides your IP address and encrypts your internet connection, improving privacy and security online.",
                "Disconnect your device from the internet, run antivirus scans, change passwords, and contact your IT/security team or a cybersecurity professional.",
                "Cybersecurity careers include roles like security analyst, penetration tester, incident responder, SOC analyst, and ethical hacker."
            ]
        }

        self.create_widgets()
        self.add_welcome_message()
    
    def preprocess(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text.lower())
    
    def create_widgets(self):
        title_label = tk.Label(
            self.root, text="🔐 Cybersecurity FAQ Chatbot",
            font=('Arial', 18, 'bold'), bg='#1a1a2e', fg='#00d4ff'
        )
        title_label.pack(pady=15)
        
        self.chat_display = scrolledtext.ScrolledText(
            self.root, height=20, width=80, font=('Arial', 11),
            bg='#16213e', fg='white', wrap=tk.WORD, state='disabled'
        )
        self.chat_display.pack(padx=20, pady=10, fill='both', expand=True)
        
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
        welcome_msg = """👋 Welcome to the Cybersecurity FAQ Chatbot!

Ask me about:
• Cyber threats & attacks  
• Password & email safety  
• Phishing & social engineering  
• VPNs, firewalls & encryption  
• Cybersecurity careers  
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
        
        best_match = difflib.get_close_matches(msg, questions, n=1, cutoff=0.3)
        
        if best_match:
            idx = questions.index(best_match[0])
            return self.faq_data['answers'][idx]
        else:
            return random.choice([
                "🤔 I’m not sure about that. Can you rephrase?",
                "I don’t have info on that, please check with a cybersecurity expert.",
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
