import os

from fred_downloader import FredDownloader
from market_scoring import MarketScoringEngine
from chart_generator import ChartGenerator
from pdf_report_builder import PDFReportBuilder

# =====================================================
# CONFIGURATION
# =====================================================

API_KEY = "1225facd81d80e506c97566c8d388ac8"

OUTPUT_DIR = "output"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# =====================================================
# START
# =====================================================

print("=" * 70)
print("US EQUITY MARKET ANALYTICS PLATFORM")
print("=" * 70)

# =====================================================
# DOWNLOAD DATA
# =====================================================

print("\nDownloading Market Data...")

fred = FredDownloader(
    API_KEY
)

snapshot = (
    fred.get_market_snapshot()
)

if len(snapshot) == 0:

    raise Exception(
        "No market data downloaded."
    )

snapshot.to_csv(

    os.path.join(
        OUTPUT_DIR,
        "market_snapshot.csv"
    ),

    index=False

)

print("\nMarket Snapshot")

print(snapshot)

# =====================================================
# MARKET SCORING
# =====================================================

print(
    "\nRunning Market Intelligence Engine..."
)

engine = (
    MarketScoringEngine()
)

score_df = (
    engine.analyze_market(
        snapshot
    )
)

score_df.to_csv(

    os.path.join(
        OUTPUT_DIR,
        "market_scores.csv"
    ),

    index=False

)

commentary = (
    engine.generate_commentary(
        score_df
    )
)

print("\nMarket Analysis")

print(score_df)

# =====================================================
# CHARTS
# =====================================================

print(
    "\nGenerating Charts..."
)

charts = (
    ChartGenerator()
)

chart_files = (

    charts.generate_all(

        snapshot,

        score_df

    )

)

print("\nGenerated Charts")

for chart in chart_files:

    print(chart)

# =====================================================
# PDF REPORT
# =====================================================

print(
    "\nBuilding PDF Report..."
)

pdf = (
    PDFReportBuilder()
)

pdf.build_report(

    snapshot=
    snapshot,

    score_df=
    score_df,

    commentary=
    commentary,

    chart_files=
    chart_files,

    output_file=
    os.path.join(

        OUTPUT_DIR,

        "US_Equity_Market_Report.pdf"

    )

)

# =====================================================
# SAVE COMMENTARY
# =====================================================

with open(

    os.path.join(
        OUTPUT_DIR,
        "market_commentary.txt"
    ),

    "w"

) as f:

    f.write(
        commentary
    )

# =====================================================
# COMPLETE
# =====================================================

print("\n" + "=" * 70)

print(
    "PROCESS COMPLETED SUCCESSFULLY"
)

print("=" * 70)

print("\nGenerated Files")

print(
    "market_snapshot.csv"
)

print(
    "market_scores.csv"
)

print(
    "market_commentary.txt"
)

for chart in chart_files:

    print(chart)

print(
    "US_Equity_Market_Report.pdf"
)

print(
    "\nOutput Folder:"
)

print(
    os.path.abspath(
        OUTPUT_DIR
    )
)