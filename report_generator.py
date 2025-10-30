import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(results, summary, output_path):
    """Generate a PDF report summarizing crypto analysis results and market summary."""
    date_str = datetime.date.today().isoformat()
    file_path = f"{output_path}/crypto_report_{date_str}.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []
    title = Paragraph(f"Crypto Market Report - {date_str}", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Build table with extended metrics: Symbol, Exchange, RSI, MACD, Signal, EMA20, BB High, BB Low, Advice
    table_data = [["Symbol", "Exchange", "RSI", "MACD", "Signal", "EMA20", "BB_High", "BB_Low", "Advice"]]
    table_data += results

    table = Table(table_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))

    summary_title = Paragraph("Market Summary", styles["Heading2"])
    summary_text = Paragraph(summary, styles["BodyText"])
    elements.append(summary_title)
    elements.append(summary_text)

    doc.build(elements)
    return file_path
