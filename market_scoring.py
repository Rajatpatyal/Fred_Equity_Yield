import pandas as pd


class MarketScoringEngine:

    def __init__(self):
        pass

    # ==============================================
    # GET VALUE
    # ==============================================

    def get_value(
        self,
        snapshot,
        metric,
        default=None
    ):

        row = snapshot[
            snapshot["Metric"] == metric
        ]

        if len(row) == 0:
            return default

        return float(
            row.iloc[0]["Value"]
        )

    # ==============================================
    # MARKET ANALYSIS
    # ==============================================

    def analyze_market(
        self,
        snapshot
    ):

        sp500 = self.get_value(
            snapshot,
            "S&P 500",
            0
        )

        nasdaq = self.get_value(
            snapshot,
            "NASDAQ",
            0
        )

        dow = self.get_value(
            snapshot,
            "Dow Jones",
            0
        )

        vix = self.get_value(
            snapshot,
            "VIX",
            20
        )

        inflation = self.get_value(
            snapshot,
            "Inflation",
            300
        )

        unemployment = self.get_value(
            snapshot,
            "Unemployment",
            4
        )

        fedfunds = self.get_value(
            snapshot,
            "Fed Funds",
            4.5
        )

        treasury10 = self.get_value(
            snapshot,
            "10Y Treasury",
            4.5
        )

        # =====================================
        # VOLATILITY SCORE
        # =====================================

        volatility_score = max(
            0,
            10 - (vix / 4)
        )

        # =====================================
        # INFLATION SCORE
        # =====================================

        inflation_score = max(
            0,
            10 - ((inflation - 250) / 20)
        )

        # =====================================
        # EMPLOYMENT SCORE
        # =====================================

        employment_score = max(
            0,
            10 - unemployment
        )

        # =====================================
        # RATE SCORE
        # =====================================

        rate_score = max(
            0,
            10 - fedfunds
        )

        # =====================================
        # ECONOMIC HEALTH
        # =====================================

        economic_health = (

            inflation_score * 0.3

            +

            employment_score * 0.4

            +

            rate_score * 0.3

        )

        # =====================================
        # RISK SCORE
        # =====================================

        risk_score = (

            (10 - volatility_score)

            +

            (10 - employment_score)

            +

            (10 - rate_score)

        ) / 3

        # =====================================
        # OPPORTUNITY SCORE
        # =====================================

        opportunity_score = (

            economic_health * 0.5

            +

            volatility_score * 0.5

        )

        # =====================================
        # MARKET REGIME
        # =====================================

        regime = "Bullish"

        if risk_score > 5:

            regime = "Neutral"

        if risk_score > 7:

            regime = "Bearish"

        # =====================================
        # RESULT
        # =====================================

        results = pd.DataFrame({

            "Metric":[

                "S&P 500",

                "NASDAQ",

                "Dow Jones",

                "VIX",

                "Inflation",

                "Unemployment",

                "Fed Funds",

                "10Y Treasury",

                "Economic Health",

                "Risk Score",

                "Opportunity Score",

                "Market Regime"

            ],

            "Value":[

                round(sp500,2),

                round(nasdaq,2),

                round(dow,2),

                round(vix,2),

                round(inflation,2),

                round(unemployment,2),

                round(fedfunds,2),

                round(treasury10,2),

                round(economic_health,2),

                round(risk_score,2),

                round(opportunity_score,2),

                regime

            ]

        })

        return results

    # ==============================================
    # MARKET COMMENTARY
    # ==============================================

    def generate_commentary(
        self,
        score_df
    ):

        regime = score_df[
            score_df["Metric"]
            ==
            "Market Regime"
        ]["Value"].iloc[0]

        opportunity = float(

            score_df[
                score_df["Metric"]
                ==
                "Opportunity Score"
            ]["Value"].iloc[0]

        )

        risk = float(

            score_df[
                score_df["Metric"]
                ==
                "Risk Score"
            ]["Value"].iloc[0]

        )

        commentary = f"""

US Equity Market Analysis

Current market regime is classified as {regime}.

Opportunity Score is {opportunity:.2f}
out of 10.

Risk Score is {risk:.2f}
out of 10.

Economic indicators suggest that
investors should maintain diversified
equity exposure while monitoring
interest rates, inflation and market
volatility.

Technology and large-cap growth
stocks continue to benefit from
favorable economic conditions when
volatility remains below historical
averages.

"""

        return commentary


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    sample = pd.DataFrame({

        "Metric":[

            "S&P 500",
            "NASDAQ",
            "Dow Jones",
            "VIX",
            "Inflation",
            "Unemployment",
            "Fed Funds",
            "10Y Treasury"

        ],

        "Value":[

            7600,
            27000,
            51000,
            16,
            332,
            4.3,
            4.5,
            4.4

        ]

    })

    engine = MarketScoringEngine()

    result = engine.analyze_market(
        sample
    )

    print(result)

    print(
        engine.generate_commentary(
            result
        )
    )