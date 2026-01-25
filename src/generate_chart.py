"""Generate interactive HTML chart for Ken French Data Library."""

import pandas as pd
import plotly.express as px
import os
from pathlib import Path

# Get the project root (one level up from src/)
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "_data"
OUTPUT_DIR = PROJECT_ROOT / "_output"


def generate_french_portfolios_chart():
    """Generate Fama-French portfolio returns time series chart."""
    # Load French portfolio returns data
    df = pd.read_parquet(DATA_DIR / "ftsfr_french_portfolios_25_daily_size_and_bm.parquet")

    # Sample to monthly for better visualization if daily data
    df['ds'] = pd.to_datetime(df['ds'])

    # Get a subset of unique_ids for cleaner visualization (first 5)
    unique_ids = df['unique_id'].unique()[:5]
    df_subset = df[df['unique_id'].isin(unique_ids)]

    # Create line chart
    fig = px.line(
        df_subset.sort_values("ds"),
        x="ds",
        y="y",
        color="unique_id",
        title="Fama-French 25 Portfolios (Size and Book-to-Market)",
        labels={
            "ds": "Date",
            "y": "Return",
            "unique_id": "Portfolio"
        }
    )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save chart
    output_path = OUTPUT_DIR / "french_portfolios_replication.html"
    fig.write_html(str(output_path))
    print(f"Chart saved to {output_path}")

    return fig


def generate_french_cumulative_returns_chart():
    """Generate Fama-French portfolio cumulative returns time series chart."""
    # Load French portfolio returns data
    df = pd.read_parquet(DATA_DIR / "ftsfr_french_portfolios_25_daily_size_and_bm.parquet")

    df['ds'] = pd.to_datetime(df['ds'])

    # Get the same subset of unique_ids as the returns chart (first 5)
    unique_ids = df['unique_id'].unique()[:5]
    df_subset = df[df['unique_id'].isin(unique_ids)]

    # Calculate cumulative returns
    df_subset = df_subset.sort_values(['unique_id', 'ds'])
    df_subset['cumulative'] = df_subset.groupby('unique_id')['y'].transform(
        lambda x: (1 + x).cumprod()
    )

    # Create line chart
    fig = px.line(
        df_subset,
        x="ds",
        y="cumulative",
        color="unique_id",
        title="Fama-French 25 Portfolios Cumulative Returns (Size and Book-to-Market)",
        labels={
            "ds": "Date",
            "cumulative": "Cumulative Return (Growth of $1)",
            "unique_id": "Portfolio"
        }
    )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        yaxis_type="log"
    )

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save chart
    output_path = OUTPUT_DIR / "french_portfolios_cumulative_returns.html"
    fig.write_html(str(output_path))
    print(f"Chart saved to {output_path}")

    return fig


if __name__ == "__main__":
    generate_french_portfolios_chart()
    generate_french_cumulative_returns_chart()
