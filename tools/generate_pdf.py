import os
from fpdf import FPDF

ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC_DIR = os.path.join(ROOT, "public")
ASSETS_DIR = os.path.join(ROOT, "assets")
PHP_DIR = os.path.join(ROOT, "php")
os.makedirs(PUBLIC_DIR, exist_ok=True)

# Utility to add a titled section
class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

pdf = PDF(format="A4")
pdf.set_auto_page_break(auto=True, margin=15)

# Cover page
pdf.add_page()
pdf.set_font("Helvetica", "B", 22)
pdf.cell(0, 12, "PHP Programming Tasks Report", ln=1, align="C")

pdf.ln(10)
pdf.set_font("Helvetica", "", 12)
pdf.multi_cell(0, 8, "This document contains two PHP programs with structured sections: AIM, Problem Statement, Constraints, Procedure, Program, Output (with screenshots), and Conclusion.")

# Helper to add a section title

def section_title(title: str):
    pdf.set_font("Helvetica", "B", 14)
    pdf.ln(4)
    pdf.cell(0, 8, title, ln=1)

# Helper to add a paragraph

def para(text: str):
    pdf.set_font("Helvetica", "", 12)
    available_w = pdf.w - pdf.l_margin - pdf.r_margin
    pdf.multi_cell(available_w, 7, text)

# Helper to add code block from file

def code_block_from_file(path: str):
    pdf.set_font("Courier", size=10)
    available_w = pdf.w - pdf.l_margin - pdf.r_margin
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            # Replace tabs to ensure consistent width
            line = line.rstrip("\n").replace("\t", "    ")
            # Use a small non-breaking space if the line would be empty
            txt = line if line.strip() != "" else "\u00A0"
            pdf.multi_cell(available_w, 5, txt)

# Task 1 page
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Task 1: Largest of Three Numbers (Nested if)", ln=1)

section_title("AIM")
para("Write a PHP program to find the largest of three numbers using nested if statements.")

section_title("Problem Statement")
para("Given three numbers, determine the largest value using nested if logic without using arrays or built-in max functions.")

section_title("Constraints")
para("- Use nested if statements.\n- Assume numeric inputs.\n- Do not use library functions like max().")

section_title("Procedure")
para("1. Define three numeric variables.\n2. Use nested if statements to compare the numbers pairwise.\n3. Store the maximum in a variable.\n4. Print the input numbers and the largest number.")

section_title("Program")
code_block_from_file(os.path.join(PHP_DIR, "task1_largest.php"))

section_title("Output")
img1 = os.path.join(ASSETS_DIR, "task1_output.png")
if os.path.exists(img1):
    # Scale image to page width with margins
    page_width = pdf.w - 2 * pdf.l_margin
    pdf.image(img1, w=page_width)
else:
    para("[Output screenshot missing]")

section_title("Conclusion")
para("The program accurately identifies the largest of the three numbers using nested if statements.")

# Task 2 page
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Task 2: Reverse a String using strrev()", ln=1)

section_title("AIM")
para("Write a PHP program to reverse a string using the built-in strrev() function.")

section_title("Problem Statement")
para("Given an input string, compute and display its reverse using strrev().")

section_title("Constraints")
para("- Use PHP's strrev() for reversal.\n- Assume UTF-8 input without combining characters.")

section_title("Procedure")
para("1. Define an input string.\n2. Call strrev() to reverse it.\n3. Print the input string and the reversed string.")

section_title("Program")
code_block_from_file(os.path.join(PHP_DIR, "task2_reverse.php"))

section_title("Output")
img2 = os.path.join(ASSETS_DIR, "task2_output.png")
if os.path.exists(img2):
    page_width = pdf.w - 2 * pdf.l_margin
    pdf.image(img2, w=page_width)
else:
    para("[Output screenshot missing]")

section_title("Conclusion")
para("The program successfully reverses the given string using strrev().")

out_path = os.path.join(PUBLIC_DIR, "report.pdf")
pdf.output(out_path)
print(f"Wrote {out_path}")
