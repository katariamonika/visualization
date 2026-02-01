import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
csv_path = base_dir / "ttc_lrt_delays.csv"

df = pd.read_csv(csv_path)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])

daily_delay = (
    df.groupby("Date", as_index=False)["Min Delay"]
      .sum()
      .rename(columns={"Min Delay": "Total Delay Minutes"})
      .sort_values("Date")
)

plt.figure()
plt.plot(daily_delay["Date"], daily_delay["Total Delay Minutes"])
plt.title("TTC LRT Daily Total Delay Minutes")
plt.xlabel("Date")
plt.ylabel("Total delay minutes")
plt.xticks(rotation=45)
plt.tight_layout()

out_png = Path(__file__).resolve().parent / "visualization_1_line.png"
plt.savefig(out_png, dpi=300)
plt.close()
