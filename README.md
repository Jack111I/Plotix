High‑Performance, Pythonic Data Visualization

https://github.com/Jack111I/Plotix
📦 Installation
bash
 Copy
# pip (recommended)
pip install plotix

# for the latest development branch
pip install git+https://github.com/Jack111I/Plotix.git

Optional extras

bash
 Copy
pip install plotix[jupyter]      # Jupyter integration
pip install plotix[plotly]      # Plotly backend support

🚀 Quick Start
python
 Copy
import plotix as px
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

px.line(x, y, title="Sine Wave", xlabel="x", ylabel="sin(x)", theme="dark")
px.show()
The plot will appear with a dark‑mode background and a 4‑point thick line.
🧩 Features
Chart	Function	Typical Use‑Case
Line	px.line	Time‑series, model diagnostics
Bar / Stacked Bar	px.bar, px.bar_stacked	Economic data, group comparisons
Scatter / Bubble	px.scatter, px.bubble	Correlation studies
Histogram	px.histogram	Distribution analysis
Heatmap / Contour	px.heatmap, px.contour	2‑D surfaces, correlation matrices
Box / Violin	px.box, px.violin	Statistical summaries
3‑D Surface / Wireframe	px.surface, px.wireframe	Scientific simulations
Parallel Coordinates	px.parallel	Multivariate datasets
Polar / Radial	px.polar	Angular data
Faceted	px.group	Multi‑panel figures
All functions accept pandas, numpy, dict or raw arrays.
🎨 Styling Engine
python
 Copy
px.set_theme("default")           # global theme
px.line(x, y, theme="default")    # override for a single plot
Built‑in Themes
Theme	Description
default	Classic scientific look
dark	Dark‑mode background
seaborn	Seaborn‑style colors
plotly	Plotly‑style theme for interactive charts
jupyter	Light theme for Jupyter

Custom theme – drop a plotix.cfg or set PX_THEME env variable.

📈 API (auto‑generated docs at https://jack111i.github.io/Plotix)
python
 Copy
px.line(x, y, *args, **kwargs)
px.bar(x, y, *args, **kwargs)
px.scatter(x, y, *args, **kwargs)
px.histogram(data, *args, **kwargs)
px.box(data, *args, **kwargs)
px.violin(data, *args, **kwargs)
px.heatmap(matrix, *args, **kwargs)
px.surface(X, Y, Z, *args, **kwargs)
px.parallel(df, *args, **kwargs)
px.polar(theta, r, *args, **kwargs)
Common keyword arguments (title, xlabel, ylabel, theme, legend, size, backend, …) are documented in the full API reference.
📑 Examples
python
 Copy
# 1. Multi‑panel scientific figure
import plotix as px
import pandas as pd

df = pd.read_csv("data/simulation.csv")
px.subplot(
    1, 3,
    [
        px.line(df["time"], df["temperature"], title="Temperature"),
        px.line(df["time"], df["pressure"], title="Pressure"),
        px.line(df["time"], df["humidity"], title="Humidity")
    ],
    theme="seaborn"
)
px.export("experiment.pdf")
python
 Copy
# 2. Heatmap of a correlation matrix
import plotix as px, numpy as np

data = np.random.randn(10, 10)
px.heatmap(data, cmap="viridis", title="Correlation Matrix")
px.export("heatmap.svg")
python
 Copy
# 3. Interactive 3‑D surface (Plotly backend)
import plotix as px, numpy as np

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

px.surface(X, Y, Z, backend="plotly", title="Sine Surface")
px.export("surface.html")   # opens in your browser
⚙️ Configuration & Themes
python
 Copy
px.list_themes()          # shows available themes
px.set_theme("default")   # apply globally
Custom themes can be loaded from JSON files that follow the Matplotlib style dictionary conventions.
python
 Copy
px.load_theme("mytheme.json")
px.set_theme("mytheme")
📤 Exporting & Interactivity
Export	Command	Notes
PNG / JPG	px.savefig("figure.png", dpi=300)	Raster
SVG / PDF	px.savefig("figure.svg")	Vector
Interactive HTML	px.export("interactive.html")	Requires Plotly backend
Jupyter Notebook	px.show()	In‑cell rendering
python
 Copy
px.scatter(df["x"], df["y"],
           backend="plotly",
           title="Interactive Scatter",
           hover_data=["label"])
🧪 Testing & CI
bash
 Copy
# dev dependencies
pip install plotix[dev]

# run tests locally
pytest tests/
The repo is linked to GitHub Actions, running a full lint, type‑check, test matrix (Python 3.9‑3.11) and coverage report on every push.
🤝 Contributing

Fork the repo

Create a feature branch (git checkout -b feature/awesome‑chart)

Run pytest tests/ locally

Push and open a Pull Request

Style: PEP 8, NumPy‑style docstrings, minimal imports.

See CONTRIBUTING.md for details.
📄 License
MIT © Jack111I

https://github.com/Jack111I/Plotix/blob/main/LICENSE
Plot it. Plot it better.

Feel free to star, fork, or open issues – we’re constantly improving Plotix for the data‑science community.
