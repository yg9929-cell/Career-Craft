import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Career Craft - Team Portfolio")
root.geometry("1000x700")
root.configure(bg="#0b0f19")

BG = "#0b0f19"
CARD = "#172033"
ACCENT = "#a78bfa"
WHITE = "#ffffff"
MUTED = "#b8b8c8"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "..", "images")

members = [
    {
        "name": "G Yoshitha",
        "image": os.path.join(IMAGE_DIR, "profile.jpeg"),
        "role": "B.Tech CSE Student"
    },
    {
        "name": "M Shalini",
        "image": os.path.join(IMAGE_DIR, "shalini.jpeg"),
        "role": "B.Tech CSE Student"
    },
    {
        "name": "R Rehan",
        "image": os.path.join(IMAGE_DIR, "rehan.jpeg"),
        "role": "B.Tech CSE Student"
    }
]

image_references = []


# ---------------- COMMON FUNCTIONS ----------------

def clear_window():
    global image_references
    image_references = []

    root.unbind_all("<MouseWheel>")

    for widget in root.winfo_children():
        widget.destroy()


def open_link(url):
    webbrowser.open(url)


def add_heading(parent, title):
    tk.Label(
        parent,
        text=title,
        font=("Arial", 21, "bold"),
        fg=ACCENT,
        bg=BG
    ).pack(anchor="w", pady=(20, 8))


def add_card(parent, title, content):
    card = tk.Frame(
        parent,
        bg=CARD,
        padx=22,
        pady=18
    )
    card.pack(fill="x", pady=8)

    tk.Label(
        card,
        text=title,
        font=("Arial", 16, "bold"),
        fg=WHITE,
        bg=CARD,
        anchor="w"
    ).pack(fill="x", pady=(0, 8))

    tk.Label(
        card,
        text=content,
        font=("Arial", 11),
        fg=MUTED,
        bg=CARD,
        justify="left",
        anchor="w",
        wraplength=780
    ).pack(fill="x")


def add_link(parent, text, url):
    link = tk.Label(
        parent,
        text=text,
        font=("Arial", 11, "underline"),
        fg=ACCENT,
        bg=CARD,
        cursor="hand2"
    )
    link.pack(anchor="w", pady=4)
    link.bind("<Button-1>", lambda event: open_link(url))


# ---------------- SCROLLABLE PAGE ----------------

def create_scrollable_page():
    canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(
        root,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = tk.Frame(canvas, bg=BG)

    scroll_frame.bind(
        "<Configure>",
        lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw",
        width=960
    )

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root.bind_all("<MouseWheel>", on_mousewheel)

    return scroll_frame


# ---------------- HOME PAGE ----------------

def show_home():
    clear_window()

    heading = tk.Label(
        root,
        text="CAREER CRAFT",
        font=("Arial", 30, "bold"),
        fg=ACCENT,
        bg=BG
    )
    heading.pack(pady=(25, 5))

    subtitle = tk.Label(
        root,
        text="Meet Our Team",
        font=("Arial", 17),
        fg=WHITE,
        bg=BG
    )
    subtitle.pack(pady=5)

    container = tk.Frame(root, bg=BG)
    container.pack(expand=True)

    for member in members:
        card = tk.Frame(
            container,
            bg=CARD,
            padx=25,
            pady=20
        )
        card.pack(side="left", padx=15, pady=20)

        try:
            image = Image.open(member["image"])
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            image_references.append(photo)

            tk.Label(
                card,
                image=photo,
                bg=CARD
            ).pack(pady=8)

        except Exception:
            tk.Label(
                card,
                text="Image not found",
                fg=MUTED,
                bg=CARD,
                width=18,
                height=8
            ).pack(pady=8)

        tk.Label(
            card,
            text=member["name"],
            font=("Arial", 17, "bold"),
            fg=WHITE,
            bg=CARD
        ).pack(pady=5)

        tk.Label(
            card,
            text=member["role"],
            font=("Arial", 11),
            fg=MUTED,
            bg=CARD
        ).pack(pady=5)

        tk.Button(
            card,
            text="View Portfolio",
            font=("Arial", 11, "bold"),
            bg=ACCENT,
            fg=BG,
            relief="flat",
            padx=15,
            pady=8,
            command=lambda m=member: show_profile(m)
        ).pack(pady=10)


# ---------------- YOSHITHA'S PROFILE ----------------

def show_yoshitha_profile():
    clear_window()
    page = create_scrollable_page()

    back_button = tk.Button(
        page,
        text="← Back to Team",
        command=show_home,
        bg=ACCENT,
        fg=BG,
        relief="flat",
        padx=15,
        pady=7
    )
    back_button.pack(anchor="w", padx=25, pady=15)

    hero = tk.Frame(page, bg=CARD, padx=25, pady=25)
    hero.pack(fill="x", padx=25, pady=10)

    tk.Label(
        hero,
        text="Hello, welcome to my portfolio!",
        font=("Arial", 18, "bold"),
        fg=ACCENT,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="I'm Yoshitha",
        font=("Arial", 30, "bold"),
        fg=WHITE,
        bg=CARD
    ).pack(anchor="w", pady=5)

    tk.Label(
        hero,
        text="B.Tech CSE Student",
        font=("Arial", 14),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="Learning, creating and growing every day.",
        font=("Arial", 12),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w", pady=8)

    try:
        image = Image.open(os.path.join(IMAGE_DIR, "profile.jpeg"))
        image = image.resize((170, 170))
        photo = ImageTk.PhotoImage(image)
        image_references.append(photo)

        tk.Label(
            hero,
            image=photo,
            bg=CARD
        ).pack(anchor="e", pady=10)

    except Exception:
        pass

    add_heading(page, "About Me")

    add_card(
        page,
        "Who I Am",
        "I am Yoshitha, a B.Tech Computer Science Engineering student "
        "interested in learning technology and developing my skills."
    )

    add_card(
        page,
        "Academic Background",
        "Currently pursuing my second year of B.Tech in Computer "
        "Science Engineering at SRM University."
    )

    add_card(
        page,
        "Passion for Technology",
        "I enjoy exploring technology, programming and learning "
        "new concepts."
    )

    add_card(
        page,
        "Interests",
        "Programming, technology, dance, chess and yoga."
    )

    add_card(
        page,
        "Strengths",
        "Teamwork, communication, adaptability and willingness to learn."
    )

    add_card(
        page,
        "Career Goals",
        "To improve my technical knowledge, build useful projects "
        "and grow as a software professional."
    )

    add_heading(page, "Education")

    add_card(
        page,
        "2025–2029 | SRM University",
        "B.Tech in Computer Science Engineering."
    )

    add_card(
        page,
        "2023–2025 | Narayana Junior College",
        "Higher Secondary Education."
    )

    add_card(
        page,
        "2018–2023 | The Accord",
        "School Education."
    )

    add_card(
        page,
        "2013–2018 | Ravindra Bharathi",
        "School Education."
    )

    add_heading(page, "Achievements")

    add_card(
        page,
        "English Competition",
        "Secured second prize in an English competition."
    )

    add_card(
        page,
        "Group Discussion",
        "Developed communication and group discussion skills."
    )

    add_card(
        page,
        "Dance Competition",
        "Won a dance competition."
    )

    add_card(
        page,
        "Sports Achievement",
        "Participated in sports activities and competitions."
    )

    add_card(
        page,
        "Olympiad",
        "Participated in Olympiad competitions."
    )

    add_heading(page, "Projects")

    add_card(
        page,
        "Smart Parking Finder",
        "A web-based project developed using HTML, CSS and JavaScript."
    )
    add_link(
        page,
        "GitHub Project",
        "https://github.com/yg9929-cell/Smart_Parking_Finder"
    )

    add_card(
        page,
        "Personal Expense Tracker",
        "A project developed using HTML, CSS and JavaScript."
    )
    add_link(
        page,
        "GitHub Project",
        "https://github.com/yg9929-cell/Personal_Expense_Tracker"
    )

    add_card(
        page,
        "Library Management System",
        "A Java-based project for managing library records."
    )
    add_link(
        page,
        "GitHub Project",
        "https://github.com/yg9929-cell/Library_Management_System"
    )

    add_heading(page, "Activities & Interests")

    add_card(
        page,
        "Activities",
        "Participated in school science and social science project "
        "competitions and volunteering activities."
    )

    add_card(
        page,
        "Interests",
        "Dance, chess and yoga."
    )

    add_heading(page, "Technical Skills")

    add_card(
        page,
        "Programming Languages",
        "C, C++, Java and Python (basic knowledge)."
    )

    add_card(
        page,
        "Web Technologies",
        "HTML, CSS and JavaScript."
    )

    add_card(
        page,
        "Soft Skills",
        "Teamwork and communication."
    )

    add_heading(page, "Contact")

    contact = tk.Frame(page, bg=CARD, padx=22, pady=18)
    contact.pack(fill="x", padx=25, pady=8)

    add_link(
        contact,
        "Email",
        "https://mail.google.com/mail/?view=cm&fs=1&to=yoshithagattath@gmail.com"
    )

    add_link(
        contact,
        "GitHub",
        "https://github.com/yg9929-cell"
    )

    add_link(
        contact,
        "LinkedIn",
        "https://www.linkedin.com/in/yoshitha-gattath-717771448/"
    )

    add_link(
        contact,
        "Instagram",
        "https://www.instagram.com/yoshitha_8452/"
    )
    # ---------------- SHALINI'S PROFILE ----------------

def show_shalini_profile():
    clear_window()
    page = create_scrollable_page()

    tk.Button(
        page,
        text="← Back to Team",
        command=show_home,
        bg=ACCENT,
        fg=BG,
        relief="flat",
        padx=15,
        pady=7
    ).pack(anchor="w", padx=25, pady=15)

    hero = tk.Frame(page, bg=CARD, padx=25, pady=25)
    hero.pack(fill="x", padx=25, pady=10)

    tk.Label(
        hero,
        text="Welcome to my portfolio!",
        font=("Arial", 18, "bold"),
        fg=ACCENT,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="I'm M Shalini",
        font=("Arial", 30, "bold"),
        fg=WHITE,
        bg=CARD
    ).pack(anchor="w", pady=5)

    tk.Label(
        hero,
        text="B.Tech CSE Student",
        font=("Arial", 14),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="Curiosity leads me to new possibilities.",
        font=("Arial", 12),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w", pady=8)

    try:
        image = Image.open(os.path.join(IMAGE_DIR, "shalini.jpeg"))
        image = image.resize((170, 170))
        photo = ImageTk.PhotoImage(image)
        image_references.append(photo)

        tk.Label(
            hero,
            image=photo,
            bg=CARD
        ).pack(anchor="e", pady=10)

    except Exception:
        pass

    add_heading(page, "About Me")

    add_card(
        page,
        "Who I Am",
        "I am Shalini, a B.Tech Computer Science Engineering student. "
        "I enjoy learning new things, exploring technology and developing my skills."
    )

    add_card(
        page,
        "Academic Background",
        "Currently pursuing B.Tech in Computer Science Engineering "
        "at SRM University."
    )

    add_card(
        page,
        "Passion for Technology",
        "I enjoy exploring new technologies, programming concepts "
        "and problem-solving."
    )

    add_card(
        page,
        "Interests",
        "Technology, Programming and Creative Learning."
    )

    add_card(
        page,
        "Strengths",
        "Quick Learning, Adaptability and Teamwork."
    )

    add_card(
        page,
        "Career Goals",
        "Develop Technical Skills, Build Projects and achieve Continuous Growth."
    )

    add_heading(page, "Education")

    add_card(
        page,
        "2025–2029 | SRM University",
        "B.Tech in Computer Science Engineering (Currently Pursuing)."
    )

    add_card(
        page,
        "2023–2025 | Velammal Vidhyashram, Guduvancheri",
        "Class 11 and Class 12."
    )

    add_card(
        page,
        "2022 | Velammal Vidhyashram, Guduvancheri",
        "Class 10."
    )

    add_heading(page, "Achievements & Activities")

    add_card(
        page,
        "Technical Events",
        "Participated in technical events and activities to explore "
        "technology and develop technical skills."
    )

    add_card(
        page,
        "Volunteering & Event Coordination",
        "Participated in volunteering and event coordination activities, "
        "developing teamwork and organisational skills."
    )

    add_card(
        page,
        "Creative Hobbies",
        "Enjoys creative activities and learning new things."
    )

    add_heading(page, "Projects")

    add_card(
        page,
        "Library Management System",
        "A Python application for managing library records and book "
        "information using a database.\n\nTechnologies: Python, DBMS and MySQL."
    )

    add_card(
        page,
        "Hotel Management System",
        "A Python project designed to manage hotel information "
        "and operations.\n\nTechnology: Python."
    )

    add_heading(page, "Technical Skills")

    add_card(
        page,
        "Programming Languages",
        "Python, C++, C and Java."
    )

    add_card(
        page,
        "Database",
        "MySQL and DBMS."
    )

    add_card(
        page,
        "Project & Task Management",
        "Agile/Scrum, Jira, Trello, Asana and Resource Allocation."
    )

    add_heading(page, "Contact")

    contact = tk.Frame(page, bg=CARD, padx=22, pady=18)
    contact.pack(fill="x", padx=25, pady=8)

    add_link(
        contact,
        "Email",
        "mshalini3111@gmail.com"
    )

    add_link(
        contact,
        "GitHub",
        "https://github.com/mshalini3111"
    )


# ---------------- REHAN'S PROFILE ----------------

def show_rehan_profile():
    clear_window()
    page = create_scrollable_page()

    tk.Button(
        page,
        text="← Back to Team",
        command=show_home,
        bg=ACCENT,
        fg=BG,
        relief="flat",
        padx=15,
        pady=7
    ).pack(anchor="w", padx=25, pady=15)

    hero = tk.Frame(page, bg=CARD, padx=25, pady=25)
    hero.pack(fill="x", padx=25, pady=10)

    tk.Label(
        hero,
        text="Welcome to my portfolio!",
        font=("Arial", 18, "bold"),
        fg=ACCENT,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="I'm R Rehan",
        font=("Arial", 30, "bold"),
        fg=WHITE,
        bg=CARD
    ).pack(anchor="w", pady=5)

    tk.Label(
        hero,
        text="B.Tech CSE Student",
        font=("Arial", 14),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w")

    tk.Label(
        hero,
        text="Driven by ideas, inspired by innovation.",
        font=("Arial", 12),
        fg=MUTED,
        bg=CARD
    ).pack(anchor="w", pady=8)

    try:
        image = Image.open(os.path.join(IMAGE_DIR, "rehan.jpeg"))
        image = image.resize((170, 170))
        photo = ImageTk.PhotoImage(image)
        image_references.append(photo)

        tk.Label(
            hero,
            image=photo,
            bg=CARD
        ).pack(anchor="e", pady=10)

    except Exception:
        pass

    add_heading(page, "About Me")

    add_card(
        page,
        "Who I Am",
        "I am Rehan, a B.Tech Computer Science Engineering student "
        "interested in technology, programming and exploring new ideas."
    )

    add_card(
        page,
        "Cybersecurity Enthusiast",
        "I am interested in cybersecurity and have a foundation in "
        "network security, threat monitoring and vulnerability scanning."
    )

    add_card(
        page,
        "Practical Experience",
        "I have explored home lab projects, security log analysis "
        "and defensive security tools."
    )

    add_card(
        page,
        "Core Focus",
        "Network Security, Threat Monitoring and Vulnerability Scanning."
    )

    add_card(
        page,
        "Strengths",
        "Analytical Skills, Proactive Mindset and Problem Solving."
    )

    add_card(
        page,
        "Career Goals",
        "To develop my cybersecurity skills and work towards "
        "an entry-level cybersecurity role."
    )

    add_heading(page, "Education")

    add_card(
        page,
        "SRM University",
        "Currently pursuing B.Tech in Computer Science Engineering."
    )

    add_heading(page, "Achievements")

    add_card(
        page,
        "Cybersecurity Labs",
        "Completed multiple hands-on cybersecurity lab activities."
    )

    add_card(
        page,
        "Vulnerability Assessment",
        "Practised vulnerability assessment using industry-standard tools."
    )

    add_card(
        page,
        "Security Projects",
        "Worked on personal cybersecurity projects."
    )

    add_card(
        page,
        "Continuous Learning",
        "Interested in learning modern attack and defence techniques."
    )

    add_heading(page, "Projects")

    add_card(
        page,
        "Network Vulnerability Scanner",
        "A Python project that identifies open ports and services "
        "and generates security reports.\n\nTechnologies: Python, Socket Programming and Nmap."
    )

    add_card(
        page,
        "Network Packet Analyzer",
        "A project to inspect network traffic for protocol analysis "
        "and troubleshooting.\n\nTechnologies: Python, Scapy and Wireshark."
    )

    add_card(
        page,
        "Port Scanner",
        "A Python project that identifies open ports and active services.\n\n"
        "Technologies: Python, TCP and Multithreading."
    )

    add_card(
        page,
        "Password Strength Analyzer",
        "Evaluates password complexity and provides recommendations.\n\n"
        "Technology: Python."
    )

    add_card(
        page,
        "Secure Login System",
        "A login system with password hashing, login attempt limitations "
        "and basic session management."
    )

    add_card(
        page,
        "Web Security Testing Lab",
        "Practises security assessments in intentionally vulnerable "
        "applications.\n\nTools: OWASP Juice Shop and DVWA."
    )

    add_heading(page, "Technical Skills")

    add_card(
        page,
        "Programming Languages",
        "Python, C, C++, Java and SQL."
    )

    add_card(
        page,
        "Networking",
        "TCP/IP, DNS, HTTP/HTTPS and Subnetting."
    )

    add_card(
        page,
        "Cybersecurity",
        "Network Security, Vulnerability Assessment, Web Security "
        "and Security Auditing."
    )

    add_card(
        page,
        "Soft Skills",
        "Problem Solving, Critical Thinking, Communication "
        "and Team Collaboration."
    )

    add_heading(page, "Contact")

    contact = tk.Frame(page, bg=CARD, padx=22, pady=18)
    contact.pack(fill="x", padx=25, pady=8)

    add_link(
        contact,
        "Email",
        "https://mail.google.com/mail/?view=cm&fs=1&to=rehanx750@gmail.com"
    )

    add_link(
        contact,
        "GitHub",
        "https://github.com/rehanx750-cyber"
    )

    add_link(
        contact,
        "LinkedIn",
        "https://www.linkedin.com/in/r-rehan-1851783aa?utm_source=share_via&utm_content=profile&utm_medium=member_android"
    )
    # ---------------- PROFILE NAVIGATION ----------------

def show_profile(member):

    if member["name"] == "G Yoshitha":
        show_yoshitha_profile()

    elif member["name"] == "M Shalini":
        show_shalini_profile()

    elif member["name"] == "R Rehan":
        show_rehan_profile()


# ---------------- START APPLICATION ----------------

show_home()
root.mainloop()