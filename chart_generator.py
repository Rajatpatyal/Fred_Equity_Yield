import os
import pandas as pd
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self):

        os.makedirs(
            "output/charts",
            exist_ok=True
        )

    # ==========================================
    # MARKET SNAPSHOT
    # ==========================================

    def market_snapshot_chart(
        self,
        snapshot
    ):

        plt.figure(
            figsize=(12,6)
        )

        metrics = snapshot["Metric"]
        values = snapshot["Value"]

        plt.bar(
            metrics,
            values
        )

        plt.xticks(
            rotation=45
        )

        plt.title(
            "Market Snapshot"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "market_snapshot.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # ECONOMIC HEALTH
    # ==========================================

    def economic_health_chart(
        self,
        score_df
    ):

        subset = score_df[
            score_df["Metric"].isin([
                "Economic Health",
                "Risk Score",
                "Opportunity Score"
            ])
        ]

        plt.figure(
            figsize=(8,6)
        )

        plt.bar(
            subset["Metric"],
            subset["Value"]
        )

        plt.ylim(
            0,
            10
        )

        plt.title(
            "Economic Health Dashboard"
        )

        file = (
            "output/charts/"
            "economic_health.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # RISK VS OPPORTUNITY
    # ==========================================

    def risk_opportunity_chart(
        self,
        score_df
    ):

        risk = float(

            score_df[
                score_df["Metric"]
                ==
                "Risk Score"
            ]["Value"].iloc[0]

        )

        opportunity = float(

            score_df[
                score_df["Metric"]
                ==
                "Opportunity Score"
            ]["Value"].iloc[0]

        )

        plt.figure(
            figsize=(8,6)
        )

        plt.scatter(
            risk,
            opportunity,
            s=300
        )

        plt.xlabel(
            "Risk"
        )

        plt.ylabel(
            "Opportunity"
        )

        plt.title(
            "Risk vs Opportunity"
        )

        plt.grid(True)

        file = (
            "output/charts/"
            "risk_vs_opportunity.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # MARKET REGIME
    # ==========================================

    def regime_chart(
        self,
        score_df
    ):

        regime = score_df[
            score_df["Metric"]
            ==
            "Market Regime"
        ]["Value"].iloc[0]

        score = float(

            score_df[
                score_df["Metric"]
                ==
                "Opportunity Score"
            ]["Value"].iloc[0]

        )

        plt.figure(
            figsize=(8,5)
        )

        plt.bar(
            [regime],
            [score]
        )

        plt.ylim(
            0,
            10
        )

        plt.title(
            "Market Regime"
        )

        file = (
            "output/charts/"
            "market_regime.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # DASHBOARD
    # ==========================================

    def dashboard_chart(
        self,
        score_df
    ):

        metrics = score_df.head(10)

        plt.figure(
            figsize=(12,6)
        )

        plt.barh(
            metrics["Metric"],
            pd.to_numeric(
                metrics["Value"],
                errors="coerce"
            )
        )

        plt.title(
            "Executive Dashboard"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "dashboard.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # GENERATE ALL
    # ==========================================

    def generate_all(
        self,
        snapshot,
        score_df
    ):

        files = []

        files.append(
            self.market_snapshot_chart(
                snapshot
            )
        )

        files.append(
            self.economic_health_chart(
                score_df
            )
        )

        files.append(
            self.risk_opportunity_chart(
                score_df
            )
        )

        files.append(
            self.regime_chart(
                score_df
            )
        )

        files.append(
            self.dashboard_chart(
                score_df
            )
        )

        return files


if __name__ == "__main__":

    print(
        "Chart Engine Loaded"
    )