import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
csv_path = base_dir / "ttc_lrt_delays.csv"

df = pd.read_csv(csv_path)

station_summary = (
    df.groupby("Station", as_index=False)["Min Delay"]
      .sum()
      .rename(columns={"Min Delay": "Total Delay Minutes"})
      .sort_values("Total Delay Minutes", ascending=False)
      .head(10)
)

out_csv = Path(__file__).resolve().parent / "bar_top10_stations.csv"
station_summary.to_csv(out_csv, index=False)
