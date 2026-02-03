import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from utils.colors import info, success, error
from utils.logger import log


def collect_text_reports():
    files = []
    for f in os.listdir("reports"):
        if f.endswith(".txt"):
            files.append(os.path.join("reports", f))
    return files


def generate_report():
    text_reports = collect_text_reports()

    if not text_reports:
        error("No scan reports found to include.")
        return

    pdf_name = "reports/Final_Security_Report.pdf"
    doc = SimpleDocTemplate(pdf_name, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Termux Cyber Framework – Security Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    for file in text_reports:
        story.append(Paragraph(f"<b>Source:</b> {file}", styles["Heading2"]))
        story.append(Spacer(1, 10))

        try:
            with open(file, "r") as f:
                for line in f:
                    story.append(Paragraph(line.strip(), styles["Normal"]))
        except Exception as e:
            story.append(Paragraph(f"Error reading file: {e}", styles["Normal"]))

        story.append(Spacer(1, 20))

    doc.build(story)

    success(f"PDF report created: {pdf_name}")
    log("Generated final PDF report")
