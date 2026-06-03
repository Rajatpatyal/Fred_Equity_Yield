from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


class PDFReportBuilder:

    def __init__(self):

        self.styles = (
            getSampleStyleSheet()
        )

    # ==========================================
    # BUILD REPORT
    # ==========================================

    def build_report(

        self,

        snapshot,

        score_df,

        commentary,

        chart_files,

        output_file

    ):

        doc = SimpleDocTemplate(
            output_file
        )

        styles = self.styles

        elements = []

        # ======================================
        # COVER PAGE
        # ======================================

        elements.append(
            Paragraph(
                "US Equity Market Analytics Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1,30)
        )

        elements.append(
            Paragraph(
                "AI Powered Equity Market Intelligence Platform",
                styles["Heading1"]
            )
        )

        elements.append(
            Spacer(1,20)
        )

        elements.append(
            Paragraph(
                f"Generated: {datetime.now()}",
                styles["Normal"]
            )
        )

        elements.append(
            PageBreak()
        )

        # ======================================
        # EXECUTIVE SUMMARY
        # ======================================

        elements.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        table_data = [
            score_df.columns.tolist()
        ]

        for _, row in score_df.iterrows():

            table_data.append(
                row.astype(str).tolist()
            )

        summary_table = Table(
            table_data
        )

        summary_table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightblue
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(
            summary_table
        )

        elements.append(
            PageBreak()
        )

        # ======================================
        # MARKET SNAPSHOT
        # ======================================

        elements.append(
            Paragraph(
                "Market Snapshot",
                styles["Heading1"]
            )
        )

        snapshot_table = [

            snapshot.columns.tolist()

        ]

        for _, row in snapshot.iterrows():

            snapshot_table.append(

                row.astype(str).tolist()

            )

        tbl = Table(
            snapshot_table
        )

        tbl.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightgreen
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(tbl)

        elements.append(
            PageBreak()
        )

        # ======================================
        # COMMENTARY
        # ======================================

        elements.append(
            Paragraph(
                "AI Market Commentary",
                styles["Heading1"]
            )
        )

        elements.append(

            Paragraph(
                commentary,
                styles["BodyText"]
            )

        )

        elements.append(
            PageBreak()
        )

        # ======================================
        # CHARTS
        # ======================================

        for chart in chart_files:

            elements.append(

                Paragraph(
                    chart,
                    styles["Heading2"]
                )

            )

            elements.append(

                Image(
                    chart,
                    width=500,
                    height=300
                )

            )

            elements.append(
                Spacer(1,20)
            )

        # ======================================
        # PORTFOLIO SECTION
        # ======================================

        elements.append(
            PageBreak()
        )

        elements.append(
            Paragraph(
                "Portfolio Recommendation",
                styles["Heading1"]
            )
        )

        portfolio_text = """

Aggressive Growth Portfolio

50% Technology

20% S&P 500 ETF

15% Growth Stocks

10% International Equity

5% Cash


Balanced Portfolio

40% S&P 500 ETF

20% Dividend Stocks

20% Technology

10% Bonds

10% Cash


Defensive Portfolio

30% S&P 500 ETF

30% Bonds

20% Dividend Stocks

20% Cash

"""

        elements.append(

            Paragraph(
                portfolio_text,
                styles["BodyText"]
            )

        )

        # ======================================
        # BULL / BEAR SCENARIOS
        # ======================================

        elements.append(
            PageBreak()
        )

        elements.append(
            Paragraph(
                "Scenario Analysis",
                styles["Heading1"]
            )
        )

        scenario_text = """

Bull Market Scenario

• Falling inflation

• Stable interest rates

• Strong earnings growth

• Low market volatility


Bear Market Scenario

• Rising inflation

• Increasing interest rates

• Economic slowdown

• Elevated volatility


Base Case

• Moderate growth

• Controlled inflation

• Stable employment

• Positive equity returns

"""

        elements.append(

            Paragraph(
                scenario_text,
                styles["BodyText"]
            )

        )

        # ======================================
        # DISCLAIMER
        # ======================================

        elements.append(
            PageBreak()
        )

        elements.append(
            Paragraph(
                "Disclaimer",
                styles["Heading1"]
            )
        )

        disclaimer = """

This report is generated for educational,
research and portfolio demonstration purposes.

It does not constitute investment advice,
financial advice or trading recommendations.

Investors should conduct independent
research before making investment decisions.

"""

        elements.append(

            Paragraph(
                disclaimer,
                styles["BodyText"]
            )

        )

        # ======================================
        # BUILD PDF
        # ======================================

        doc.build(
            elements
        )

        print(
            f"PDF Saved: {output_file}"
        )


if __name__ == "__main__":

    print(
        "PDF Report Builder Loaded"
    )