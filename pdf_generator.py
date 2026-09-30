from io import BytesIO
from pathlib import Path

from fpdf import FPDF

from document_utils.text_utils import (
    sanitize_text
)


BASE_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"


class LegalEasePDF(FPDF):

    def __init__(self, document_title):
        super().__init__()

        self.document_title = document_title

        self.set_auto_page_break(
            auto=True,
            margin=18
        )

    def header(self):

        if LOGO_PATH.exists():

            try:

                self.image(
                    str(LOGO_PATH),
                    x=85,
                    y=8,
                    w=40
                )

                self.ln(22)

            except Exception:
                self.ln(5)

        else:

            self.ln(5)

        self.set_font(
            "Helvetica",
            "B",
            14
        )

        self.cell(
            0,
            10,
            sanitize_text(
                self.document_title
            ),
            align="C"
        )

        self.ln(12)

        self.set_draw_color(
            100,
            100,
            100
        )

        self.line(
            15,
            self.get_y(),
            195,
            self.get_y()
        )

        self.ln(8)

    def footer(self):

        self.set_y(-15)

        self.set_font(
            "Helvetica",
            "",
            8
        )

        self.cell(
            0,
            5,
            "LegalEase - AI-assisted legal document draft",
            align="C"
        )

        self.ln(4)

        self.cell(
            0,
            5,
            f"Page {self.page_no()}",
            align="C"
        )


def format_pdf(
    text: str,
    doc_type: str,
    terms=None
) -> bytes:

    text = sanitize_text(text)

    pdf = LegalEasePDF(
        document_title=doc_type
    )

    pdf.add_page()

    pdf.set_font(
        "Helvetica",
        "",
        11
    )

    lines = text.splitlines()

    for line in lines:

        clean_line = sanitize_text(line)

        if not clean_line:
            pdf.ln(3)
            continue

        # Heading
        if (
            clean_line.isupper()
            or clean_line.endswith(":")
        ):

            pdf.set_font(
                "Helvetica",
                "B",
                12
            )

            pdf.multi_cell(
                0,
                7,
                clean_line
            )

            pdf.ln(1)

            pdf.set_font(
                "Helvetica",
                "",
                11
            )

        # Numbered sections
        elif clean_line.startswith(
            (
                "1.",
                "2.",
                "3.",
                "4.",
                "5.",
                "6.",
                "7.",
                "8.",
                "9."
            )
        ):

            pdf.set_font(
                "Helvetica",
                "B",
                11
            )

            pdf.multi_cell(
                0,
                6,
                clean_line
            )

            pdf.set_font(
                "Helvetica",
                "",
                11
            )

        # Bullet
        elif clean_line.startswith(
            ("-", "*", "•")
        ):

            bullet_text = clean_line[
                1:
            ].strip()

            pdf.multi_cell(
                0,
                6,
                "- " + bullet_text
            )

        else:

            pdf.multi_cell(
                0,
                6,
                clean_line
            )

        pdf.ln(1)

    # Terms
    if terms:

        pdf.ln(5)

        pdf.set_font(
            "Helvetica",
            "B",
            12
        )

        pdf.cell(
            0,
            8,
            "KEY TERMS"
        )

        pdf.ln(9)

        pdf.set_font(
            "Helvetica",
            "",
            10
        )

        for index, term in enumerate(
            terms,
            start=1
        ):

            clean_term = sanitize_text(
                term
            )

            pdf.multi_cell(
                0,
                6,
                f"{index}. {clean_term}"
            )

    output = pdf.output()

    if isinstance(output, str):
        output = output.encode("latin-1")

    return bytes(output)