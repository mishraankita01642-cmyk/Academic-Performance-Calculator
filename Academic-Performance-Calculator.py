import tkinter as tk
from tkinter import messagebox


# =========================================================
# COLORS
# =========================================================

BG = "#0f172a"
CARD = "#1e293b"
ROW = "#263449"
ENTRY_BG = "#334155"

TEXT = "#f8fafc"
MUTED = "#94a3b8"

PURPLE = "#8b5cf6"
PURPLE_HOVER = "#7c3aed"

GREEN = "#22c55e"

# New delete button color
DELETE = "#475569"
DELETE_HOVER = "#64748b"


# =========================================================
# GRADE POINTS
# =========================================================

GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0
}


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Academic Performance Calculator")
root.geometry("1050x750")
root.minsize(900, 650)

root.configure(bg=BG)


# =========================================================
# TITLE
# =========================================================

tk.Label(
    root,
    text="🎓 Academic Performance Calculator",
    font=("Arial", 28, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(25, 5))


tk.Label(
    root,
    text="Calculate your SGPA and CGPA for all 8 semesters",
    font=("Arial", 12),
    bg=BG,
    fg=MUTED
).pack(pady=(0, 20))


# =========================================================
# TAB AREA
# =========================================================

tab_bar = tk.Frame(
    root,
    bg=BG
)

tab_bar.pack(
    fill="x",
    padx=30
)


sgpa_tab = tk.Button(
    tab_bar,
    text="SGPA Calculator",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg="white",
    activebackground=PURPLE_HOVER,
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12
)

sgpa_tab.pack(
    side="left"
)


cgpa_tab = tk.Button(
    tab_bar,
    text="CGPA Calculator",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=MUTED,
    activebackground=PURPLE_HOVER,
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12
)

cgpa_tab.pack(
    side="left"
)


# =========================================================
# MAIN CONTENT
# =========================================================

content = tk.Frame(
    root,
    bg=CARD
)

content.pack(
    fill="both",
    expand=True,
    padx=30
)


sgpa_page = tk.Frame(
    content,
    bg=CARD
)

cgpa_page = tk.Frame(
    content,
    bg=CARD
)


# =========================================================
# SWITCH PAGES
# =========================================================

def show_sgpa():

    cgpa_page.pack_forget()

    sgpa_page.pack(
        fill="both",
        expand=True
    )

    sgpa_tab.config(
        bg=PURPLE,
        fg="white"
    )

    cgpa_tab.config(
        bg=CARD,
        fg=MUTED
    )


def show_cgpa():

    sgpa_page.pack_forget()

    cgpa_page.pack(
        fill="both",
        expand=True
    )

    cgpa_tab.config(
        bg=PURPLE,
        fg="white"
    )

    sgpa_tab.config(
        bg=CARD,
        fg=MUTED
    )


sgpa_tab.config(
    command=show_sgpa
)

cgpa_tab.config(
    command=show_cgpa
)


# =========================================================
# ===================== SGPA PAGE =========================
# =========================================================

tk.Label(
    sgpa_page,
    text="📚 Semester SGPA Calculator",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=TEXT
).pack(pady=(25, 5))


tk.Label(
    sgpa_page,
    text="Enter subjects, credits and grades",
    font=("Arial", 11),
    bg=CARD,
    fg=MUTED
).pack(pady=(0, 20))


# =========================================================
# SUBJECT TABLE
# =========================================================

subject_area = tk.Frame(
    sgpa_page,
    bg=CARD
)

subject_area.pack(
    fill="x",
    padx=50
)


# Column widths
subject_area.grid_columnconfigure(0, weight=6)
subject_area.grid_columnconfigure(1, weight=2)
subject_area.grid_columnconfigure(2, weight=2)
subject_area.grid_columnconfigure(3, weight=1)


# =========================================================
# HEADERS
# =========================================================

headers = [
    ("Subject Name", 0),
    ("Credits", 1),
    ("Grade", 2),
    ("", 3)
]


for text, column in headers:

    tk.Label(
        subject_area,
        text=text,
        font=("Arial", 11, "bold"),
        bg=CARD,
        fg=MUTED
    ).grid(
        row=0,
        column=column,
        sticky="ew",
        padx=6,
        pady=(0, 8)
    )


subject_rows = []


# =========================================================
# ADD SUBJECT
# =========================================================

def add_subject():

    row_number = len(subject_rows) + 1

    row = tk.Frame(
        subject_area,
        bg=ROW
    )

    row.grid(
        row=row_number,
        column=0,
        columnspan=4,
        sticky="ew",
        pady=4
    )

    row.grid_columnconfigure(0, weight=6)
    row.grid_columnconfigure(1, weight=2)
    row.grid_columnconfigure(2, weight=2)
    row.grid_columnconfigure(3, weight=1)


    # Subject
    subject = tk.Entry(
        row,
        font=("Arial", 11),
        bg=ENTRY_BG,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    subject.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=(7, 5),
        pady=7,
        ipady=6
    )


    # Credits
    credit = tk.Entry(
        row,
        font=("Arial", 11),
        bg=ENTRY_BG,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    credit.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=5,
        pady=7,
        ipady=6
    )


    # Grade
    grade = tk.StringVar()

    grade.set("Select")


    grade_menu = tk.OptionMenu(
        row,
        grade,
        *GRADE_POINTS.keys()
    )

    grade_menu.config(
        font=("Arial", 10),
        bg=ENTRY_BG,
        fg=TEXT,
        activebackground=PURPLE,
        activeforeground="white",
        relief="flat",
        highlightthickness=0
    )

    grade_menu["menu"].config(
        bg=ENTRY_BG,
        fg=TEXT,
        activebackground=PURPLE,
        activeforeground="white"
    )

    grade_menu.grid(
        row=0,
        column=2,
        sticky="ew",
        padx=5,
        pady=7
    )


    # Delete
    delete = tk.Button(
        row,
        text="×",
        font=("Arial", 14, "bold"),
        bg=DELETE,
        fg=TEXT,
        activebackground=DELETE_HOVER,
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        command=lambda r=row: remove_subject(r)
    )

    delete.grid(
        row=0,
        column=3,
        padx=(5, 7),
        pady=7,
        sticky="ew"
    )


    subject_rows.append(
        (row, subject, credit, grade)
    )


# =========================================================
# REMOVE SUBJECT
# =========================================================

def remove_subject(row):

    for item in subject_rows:

        if item[0] == row:

            subject_rows.remove(item)

            row.destroy()

            refresh_subject_rows()

            break


# =========================================================
# REFRESH ROW NUMBERS
# =========================================================

def refresh_subject_rows():

    for index, item in enumerate(
        subject_rows,
        start=1
    ):

        item[0].grid_configure(
            row=index
        )


# =========================================================
# CALCULATE SGPA
# =========================================================

def calculate_sgpa():

    if len(subject_rows) == 0:

        messagebox.showerror(
            "Error",
            "Please add at least one subject."
        )

        return


    total_credits = 0
    total_points = 0


    try:

        for row, subject, credit, grade in subject_rows:

            subject_name = subject.get().strip()


            if subject_name == "":

                raise ValueError(
                    "Please enter all subject names."
                )


            credits = float(
                credit.get()
            )


            if credits <= 0:

                raise ValueError(
                    "Credits must be greater than 0."
                )


            selected_grade = grade.get()


            if selected_grade not in GRADE_POINTS:

                raise ValueError(
                    f"Please select a grade for {subject_name}."
                )


            grade_point = GRADE_POINTS[
                selected_grade
            ]


            total_credits += credits

            total_points += (
                credits * grade_point
            )


        sgpa = (
            total_points /
            total_credits
        )


        sgpa_result.config(
            text=f"{sgpa:.2f}"
        )


    except ValueError as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


# =========================================================
# SGPA BUTTONS
# =========================================================

button_area = tk.Frame(
    sgpa_page,
    bg=CARD
)

button_area.pack(
    pady=20
)


tk.Button(
    button_area,
    text="+ Add Subject",
    font=("Arial", 11, "bold"),
    bg=ROW,
    fg=TEXT,
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=11,
    command=add_subject
).pack(
    side="left",
    padx=5
)


tk.Button(
    button_area,
    text="Calculate SGPA",
    font=("Arial", 11, "bold"),
    bg=PURPLE,
    fg="white",
    activebackground=PURPLE_HOVER,
    activeforeground="white",
    relief="flat",
    padx=30,
    pady=11,
    command=calculate_sgpa
).pack(
    side="left",
    padx=5
)


# =========================================================
# SGPA RESULT
# =========================================================

sgpa_result_box = tk.Frame(
    sgpa_page,
    bg="#172033"
)

sgpa_result_box.pack(
    pady=5
)


tk.Label(
    sgpa_result_box,
    text="YOUR SGPA",
    font=("Arial", 10, "bold"),
    bg="#172033",
    fg=MUTED
).pack(
    padx=60,
    pady=(15, 0)
)


sgpa_result = tk.Label(
    sgpa_result_box,
    text="0.00",
    font=("Arial", 32, "bold"),
    bg="#172033",
    fg=GREEN
)

sgpa_result.pack(
    padx=60,
    pady=(0, 15)
)


# =========================================================
# ===================== CGPA PAGE =========================
# =========================================================

tk.Label(
    cgpa_page,
    text="🎓 4-Year CGPA Calculator",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=TEXT
).pack(pady=(25, 5))


tk.Label(
    cgpa_page,
    text="Enter SGPA and credits for each semester",
    font=("Arial", 11),
    bg=CARD,
    fg=MUTED
).pack(pady=(0, 20))


semester_area = tk.Frame(
    cgpa_page,
    bg=CARD
)

semester_area.pack(
    fill="x",
    padx=100
)


semester_area.grid_columnconfigure(0, weight=2)
semester_area.grid_columnconfigure(1, weight=2)
semester_area.grid_columnconfigure(2, weight=2)


# =========================================================
# SEMESTER HEADERS
# =========================================================

for text, column in [
    ("Semester", 0),
    ("SGPA", 1),
    ("Credits", 2)
]:

    tk.Label(
        semester_area,
        text=text,
        font=("Arial", 11, "bold"),
        bg=CARD,
        fg=MUTED
    ).grid(
        row=0,
        column=column,
        sticky="ew",
        padx=8,
        pady=(0, 8)
    )


semester_rows = []


# =========================================================
# CREATE 8 SEMESTERS
# =========================================================

for semester_number in range(1, 9):

    row = tk.Frame(
        semester_area,
        bg=ROW
    )

    row.grid(
        row=semester_number,
        column=0,
        columnspan=3,
        sticky="ew",
        pady=3
    )


    row.grid_columnconfigure(
        0,
        weight=2
    )

    row.grid_columnconfigure(
        1,
        weight=2
    )

    row.grid_columnconfigure(
        2,
        weight=2
    )


    tk.Label(
        row,
        text=f"Semester {semester_number}",
        font=("Arial", 11),
        bg=ROW,
        fg=TEXT
    ).grid(
        row=0,
        column=0,
        sticky="ew",
        padx=8,
        pady=6
    )


    sgpa = tk.Entry(
        row,
        font=("Arial", 11),
        bg=ENTRY_BG,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    sgpa.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=8,
        pady=6,
        ipady=5
    )


    credits = tk.Entry(
        row,
        font=("Arial", 11),
        bg=ENTRY_BG,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    credits.grid(
        row=0,
        column=2,
        sticky="ew",
        padx=8,
        pady=6,
        ipady=5
    )


    semester_rows.append(
        (sgpa, credits)
    )


# =========================================================
# CALCULATE CGPA
# =========================================================

def calculate_cgpa():

    total_points = 0
    total_credits = 0


    try:

        for number, (sgpa, credits) in enumerate(
            semester_rows,
            start=1
        ):

            sgpa_text = sgpa.get().strip()
            credit_text = credits.get().strip()


            # Empty semester is allowed
            if not sgpa_text and not credit_text:
                continue


            if not sgpa_text or not credit_text:

                raise ValueError(
                    f"Please complete Semester {number}."
                )


            sgpa_value = float(
                sgpa_text
            )

            credit_value = float(
                credit_text
            )


            if sgpa_value < 0 or sgpa_value > 10:

                raise ValueError(
                    f"Semester {number}: SGPA must be between 0 and 10."
                )


            if credit_value <= 0:

                raise ValueError(
                    f"Semester {number}: Credits must be greater than 0."
                )


            total_points += (
                sgpa_value * credit_value
            )

            total_credits += credit_value


        if total_credits == 0:

            raise ValueError(
                "Please enter at least one semester."
            )


        cgpa = (
            total_points /
            total_credits
        )


        cgpa_result.config(
            text=f"{cgpa:.2f}"
        )


    except ValueError as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


# =========================================================
# CGPA BUTTON
# =========================================================

tk.Button(
    cgpa_page,
    text="Calculate CGPA",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg="white",
    activebackground=PURPLE_HOVER,
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12,
    command=calculate_cgpa
).pack(
    pady=15
)


# =========================================================
# CGPA RESULT
# =========================================================

cgpa_result_box = tk.Frame(
    cgpa_page,
    bg="#172033"
)

cgpa_result_box.pack(
    pady=5
)


tk.Label(
    cgpa_result_box,
    text="YOUR CGPA",
    font=("Arial", 10, "bold"),
    bg="#172033",
    fg=MUTED
).pack(
    padx=60,
    pady=(15, 0)
)


cgpa_result = tk.Label(
    cgpa_result_box,
    text="0.00",
    font=("Arial", 32, "bold"),
    bg="#172033",
    fg=GREEN
)

cgpa_result.pack(
    padx=60,
    pady=(0, 15)
)


# =========================================================
# GRADE INFORMATION
# =========================================================

tk.Label(
    root,
    text="S = 10    A = 9    B = 8    C = 7    D = 6    E = 5    F = 0",
    font=("Arial", 10),
    bg=BG,
    fg=MUTED
).pack(
    pady=10
)


# =========================================================
# DEFAULT SUBJECTS
# =========================================================

for _ in range(4):
    add_subject()


# =========================================================
# START SGPA PAGE
# =========================================================

show_sgpa()


# =========================================================
# RUN
# =========================================================

root.mainloop()