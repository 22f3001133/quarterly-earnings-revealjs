import marimo as mo

# This Marimo notebook demonstrates an interactive data analysis
# pipeline with clear data flow and variable dependencies.

app = mo.App()


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import marimo as mo

    # Contact: 22f3001133@ds.study.iitm.ac.in
    # This cell defines core libraries that downstream cells depend on.
    return np, pd, mo


@app.cell
def _(np, pd):
    # Cell 2: Generate a synthetic dataset
    # Data flow: uses np from Cell 1 and produces df for later cells.

    rng = np.random.default_rng(42)
    n = 300

    x = rng.normal(loc=0.0, scale=1.0, size=n)
    noise = rng.normal(loc=0.0, scale=1.0, size=n)
    true_slope = 2.0

    y = true_slope * x + noise

    df = pd.DataFrame({"x": x, "y": y})
    return df, true_slope


@app.cell
def _(mo):
    # Cell 3: Define an interactive slider widget
    # Other cells will depend on slope_slider.value.

    slope_slider = mo.ui.slider(
        start=0.0,
        stop=4.0,
        step=0.1,
        value=2.0,
        label="Hypothesized slope"
    )

    # Expose the widget so it's visible in the UI.
    slope_slider
    return slope_slider


@app.cell
def _(df, slope_slider):
    # Cell 4: Compute model predictions and error metric.
    # Data flow:
    #   - df comes from the synthetic data cell
    #   - slope_slider comes from the UI widget cell
    #   - This cell produces mse and predictions for downstream use.

    slope = slope_slider.value
    y_pred = slope * df["x"]
    mse = ((df["y"] - y_pred) ** 2).mean()
    return mse, slope, y_pred


@app.cell
def _(mo, slope_slider, mse, slope):
    # Cell 5: Dynamic markdown explanation based on widget state.
    # Data flow:
    #   - Reads current slope_slider.value and mse from Cell 4
    #   - Produces a human-readable markdown summary.

    if slope < 2.0:
        relation = "lower than"
        comment = "You are underestimating the true slope."
    elif slope > 2.0:
        relation = "higher than"
        comment = "You are overestimating the true slope."
    else:
        relation = "equal to"
        comment = "You matched the true slope exactly!"

    md = mo.md(
        f"""
### Current Hypothesis

- **Chosen slope:** `{slope:.1f}`
- This is **{relation}** the true slope of `2.0`.

### Model Fit

- **Mean Squared Error (MSE):** `{mse:.3f}`  

{comment}
"""
    )

    md
    return md


@app.cell
def _(mo, df, y_pred, slope):
    # Cell 6: Simple visualization of the relationship.
    # Data flow:
    #   - Uses df and y_pred from earlier cells to plot x vs y and the fitted line.

    import plotly.express as px

    fig = px.scatter(
        df,
        x="x",
        y="y",
        opacity=0.5,
        title=f"Data and fitted line for slope = {slope:.1f}",
    )
    fig.add_traces(px.line(x=df["x"], y=y_pred).data)

    mo.ui.plotly(fig)
    return fig


@app.cell
def _(mo):
    # Cell 7: Introductory markdown (self-documenting notebook).
    intro = mo.md(
        """
# Interactive Data Analysis Notebook

This notebook explores the relationship between variables in a synthetic dataset.

- It uses **Marimo** for interactivity.
- It demonstrates **variable dependencies** between cells.
- It includes an interactive **slider widget** that updates calculations and markdown in real time.
"""
    )

    intro
    return intro


if __name__ == "__main__":
    app.run()
