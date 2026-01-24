# Ken French Data Library Pipeline

This pipeline downloads and processes the Fama-French 25 portfolios from Ken French's Data Library.

## Data Source

The data is publicly available from [Ken French's Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

## Reference

Fama, Eugene F., and Kenneth R. French. "The cross-section of expected stock returns."
The Journal of Finance 47.2 (1992): 427-465.

## Outputs

- `ftsfr_french_portfolios_25_daily_size_and_bm.parquet`: Daily 25 portfolios sorted by Size and Book-to-Market
- `ftsfr_french_portfolios_25_daily_size_and_op.parquet`: Daily 25 portfolios sorted by Size and Operating Profitability
- `ftsfr_french_portfolios_25_daily_size_and_inv.parquet`: Daily 25 portfolios sorted by Size and Investment

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```bash
   doit
   ```

3. View the generated documentation in `docs/index.html`

## Portfolio Construction

The portfolios are formed on the intersection of:
- **Size**: Market equity (5 quintiles)
- **Characteristic**: Book-to-Market, Operating Profitability, or Investment (5 quintiles)

This creates 5x5 = 25 portfolios for each characteristic combination.

## Academic References

### Primary Papers

- **Fama and French (1992)** - "The cross-section of expected stock returns"
  - The Journal of Finance 47.2 (1992): 427-465

- **Fama and French (1993)** - "Common risk factors in the returns on stocks and bonds"
  - Journal of Financial Economics 33 (1993): 3-56
  - Foundational work on size and value factors

### Key Findings

- Size (SMB) and value (HML) factors capture significant cross-sectional variation in stock returns
- The 25 portfolios provide test assets for evaluating asset pricing models
