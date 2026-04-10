PLUGIN_NAME = "pdf"
PLUGIN_DESCRIPTION = "Creates a real PDF file with title and content sections"
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pdf",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Full path where to save the .pdf file"
                },
                "title": {
                    "type": "string",
                    "description": "Document title"
                },
                "sections": {
                    "type": "array",
                    "description": "List of sections, each with 'heading' and 'content'",
                    "items": {
                        "type": "object",
                        "properties": {
                            "heading": {"type": "string"},
                            "content": {"type": "string"}
                        }
                    }
                }
            },
            "required": ["path", "title", "sections"]
        }
    }
}


def run(path: str, title: str, sections: list) -> str:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.enums import TA_CENTER, TA_LEFT

    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=2.5*cm,
        rightMargin=2.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=20,
        textColor=colors.HexColor("#1a1a2e"),
        alignment=TA_CENTER,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=13,
        textColor=colors.HexColor("#16213e"),
        spaceBefore=14,
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        leading=16,
        textColor=colors.HexColor("#333333"),
        spaceAfter=6,
    )

    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.5*cm))

    for section in sections:
        heading = section.get("heading", "")
        content = section.get("content", "")

        if heading:
            story.append(Paragraph(heading, heading_style))

        if content:
            for line in content.split("\n"):
                line = line.strip()
                if line:
                    story.append(Paragraph(line, body_style))

        story.append(Spacer(1, 0.3*cm))

    doc.build(story)
    return f"PDF created: {path}"
