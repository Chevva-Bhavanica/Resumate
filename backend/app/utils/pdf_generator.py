import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from app.config import settings

def generate_resume_pdf(data: dict, user_name: str) -> str:
    """
    Generate a professional PDF resume from JSON data.
    data might optionally contain: skills, projects, experience.
    """
    output_dir = os.path.join(settings.UPLOAD_DIR, "generated_resumes")
    os.makedirs(output_dir, exist_ok=True)
    
    file_name = f"Resume_{user_name.replace(' ', '_')}.pdf"
    file_path = os.path.join(output_dir, file_name)
    
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CenterTitle', alignment=TA_CENTER, fontSize=24, spaceAfter=20, fontName="Helvetica-Bold"))
    styles.add(ParagraphStyle(name='SectionHeader', fontSize=14, spaceAfter=6, spaceBefore=12, fontName="Helvetica-Bold", textColor="black"))
    styles.add(ParagraphStyle(name='NormalText', fontSize=11, spaceAfter=4, fontName="Helvetica"))

    Story = []

    # Name Title
    Story.append(Paragraph(user_name.upper(), styles["CenterTitle"]))
    Story.append(Spacer(1, 12))
    
    # Contact Info placeholder
    Story.append(Paragraph("Email: candidate@example.com | Phone: (123) 456-7890", styles["NormalText"]))
    Story.append(Spacer(1, 24))

    # Experience section
    if "experience" in data and data["experience"]:
        Story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionHeader"]))
        parts = data["experience"].split('\n')
        for p in parts:
            if p.strip():
                Story.append(Paragraph(p.strip(), styles["NormalText"]))
        Story.append(Spacer(1, 12))

    # Projects section
    if "projects" in data and data["projects"]:
        Story.append(Paragraph("PROJECTS", styles["SectionHeader"]))
        parts = data["projects"].split('\n')
        for p in parts:
            if p.strip():
                Story.append(Paragraph(p.strip(), styles["NormalText"]))
        Story.append(Spacer(1, 12))

    # Skills section
    if "skills" in data and data["skills"]:
        Story.append(Paragraph("SKILLS", styles["SectionHeader"]))
        skills_text = data["skills"]
        Story.append(Paragraph(skills_text, styles["NormalText"]))
        Story.append(Spacer(1, 12))

    doc.build(Story)
    return file_path
