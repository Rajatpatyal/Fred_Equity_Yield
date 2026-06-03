import requests
import pandas as pd
import time


class FredDownloader:

    def __init__(self, api_key):

        self.api_key = api_key

        self.base_url = (
            "https://api.stlouisfed.org/fred/series/observations"
        )

    # =====================================================
    # DOWNLOAD SINGLE SERIES
    # =====================================================

    def get_series(self, series_id):

        params = {

            "series_id": series_id,

            "api_key": self.api_key,

            "file_type": "json"

        }

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = requests.get(
                    self.base_url,
                    params=params,
                    timeout=30
                )

                # FRED RATE LIMIT
                if response.status_code == 429:

                    wait_time = (
                        2 * (attempt + 1)
                    )

                    print(
                        f"Rate limited. Waiting {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                    continue

                response.raise_for_status()

                data = response.json()

                if "observations" not in data:

                    print(
                        f"Invalid response for {series_id}"
                    )

                    print(data)

                    return None

                df = pd.DataFrame(
                    data["observations"]
                )

                if len(df) == 0:

                    return None

                df["date"] = pd.to_datetime(
                    df["date"]
                )

                df["value"] = pd.to_numeric(
                    df["value"],
                    errors="coerce"
                )

                df = df.dropna()

                return df

            except Exception as e:

                print(
                    f"Error downloading {series_id}: {e}"
                )

                time.sleep(2)

        return None

    # =====================================================
    # MARKET SNAPSHOT
    # =====================================================

    def get_market_snapshot(self):

        series = {

            "SP500": "S&P 500",

            "NASDAQCOM": "NASDAQ",

            "DJIA": "Dow Jones",

            "VIXCLS": "VIX",

            "FEDFUNDS": "Fed Funds",

            "UNRATE": "Unemployment",

            "CPIAUCSL": "Inflation",

            "DGS10": "10Y Treasury"

        }

        rows = []

        total = len(series)

        count = 0

        for sid, label in series.items():

            count += 1

            print(
                f"[{count}/{total}] Downloading {label}"
            )

            df = self.get_series(
                sid
            )

            if df is None:

                print(
                    f"Skipped {label}"
                )

                continue

            latest = (
                df
                .sort_values("date")
                .iloc[-1]
            )

            rows.append({

                "Metric":
                label,

                "Value":
                latest["value"],

                "Date":
                latest["date"]

            })

            # Avoid FRED rate limit
            time.sleep(1)

        snapshot = pd.DataFrame(
            rows
        )

        return snapshot

    # =====================================================
    # SAVE SNAPSHOT
    # =====================================================

    def save_snapshot(
        self,
        filename="market_snapshot.csv"
    ):

        df = self.get_market_snapshot()

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"\nSaved: {filename}"
        )

        return df


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    API_KEY = "1225facd81d80e506c97566c8d388ac8"

    fred = FredDownloader(
        API_KEY
    )

    snapshot = fred.save_snapshot()

    print("\nMarket Snapshot")

    print(snapshot)

    print(
        "\nRows:",
        len(snapshot)
    )