<div align="center">

# Plotix

**High-Performance, Pythonic Data Visualization**

[![PyPI version](https://img.shields.io/pypi/v/plotix.svg)](https://pypi.org/project/plotix/)
[![Python Versions](https://img.shields.io/pypi/pyversions/plotix.svg)](https://pypi.org/project/plotix/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Jack111I/Plotix/blob/main/LICENSE)
[![CI](https://github.com/Jack111I/Plotix/actions/workflows/ci.yml/badge.svg)](https://github.com/Jack111I/Plotix/actions)
[![Coverage](https://img.shields.io/codecov/c/github/Jack111I/Plotix)](https://codecov.io/gh/Jack111I/Plotix)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://jack111i.github.io/Plotix)

Plotix is a unified, expressive Python visualization library that wraps Matplotlib and Plotly behind a clean, consistent API — so you spend less time configuring and more time discovering insights.

[Documentation](https://jack111i.github.io/Plotix) · [Examples](#-examples) · [Contributing](#-contributing) · [Changelog](CHANGELOG.md)

</div>

---

## Table of Contents

- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Chart Gallery](#-chart-gallery)
- [Styling & Themes](#-styling--themes)
- [API Reference](#-api-reference)
- [Examples](#-examples)
- [Configuration](#-configuration--themes)
- [Exporting & Interactivity](#-exporting--interactivity)
- [Testing & CI](#-testing--ci)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📦 Installation

```bash
# Stable release (recommended)
pip install plotix

# Latest development build
pip install git+https://github.com/Jack111I/Plotix.git
```

### Optional Extras

| Extra | Command | What it Adds |
|-------|---------|--------------|
| Jupyter | `pip install plotix[jupyter]` | In-cell rendering & notebook integration |
| Plotly | `pip install plotix[plotly]` | Interactive HTML charts via Plotly backend |
| Dev | `pip install plotix[dev]` | Testing, linting, and type-check tools |

---

## 🚀 Quick Start

```python
import plotix as px
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

px.line(x, y, title="Sine Wave", xlabel="x", ylabel="sin(x)", theme="dark")
px.show()
```

> The plot renders with a dark-mode background and a 4-pt line weight out of the box — no boilerplate required.

---

## 🧩 Chart Gallery

Plotix covers the full spectrum of common and scientific chart types through a single, predictable function interface.

| Chart Type | Function | Typical Use Case |
|------------|----------|-----------------|
| Line | `px.line` | Time-series, model diagnostics |
| Bar / Stacked Bar | `px.bar`, `px.bar_stacked` | Economic data, group comparisons |
| Scatter / Bubble | `px.scatter`, `px.bubble` | Correlation studies |
| Histogram | `px.histogram` | Distribution analysis |
| Heatmap / Contour | `px.heatmap`, `px.contour` | 2-D surfaces, correlation matrices |
| Box / Violin | `px.box`, `px.violin` | Statistical summaries |
| 3-D Surface / Wireframe | `px.surface`, `px.wireframe` | Scientific simulations |
| Parallel Coordinates | `px.parallel` | Multivariate datasets |
| Polar / Radial | `px.polar` | Angular data |
| Faceted Grid | `px.group` | Multi-panel figures |

All chart functions accept **pandas DataFrames, NumPy arrays, dicts, or raw Python lists** — no preprocessing required.

---

## 🎨 Styling & Themes

### Built-in Themes

```python
px.set_theme("dark")           # Apply globally for all subsequent plots
px.line(x, y, theme="seaborn") # Override theme for a single chart
px.list_themes()               # Print all available theme names
```

| Theme | Description |
|-------|-------------|
| `default` | Classic scientific look with clean axes |
| `dark` | High-contrast dark-mode background |
| `seaborn` | Seaborn-inspired color palette |
| `plotly` | Plotly-style theme for interactive charts |
| `jupyter` | Light, minimal theme optimized for notebooks |

### Custom Themes

Custom themes follow Matplotlib style dictionary conventions and can be loaded from a JSON file:

```python
px.load_theme("mytheme.json")
px.set_theme("mytheme")
```

You can also set a theme project-wide via a `plotix.cfg` file in your working directory or the `PX_THEME` environment variable.

---

## 📈 API Reference

```python
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
```

### Common Keyword Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `title` | `str` | Chart title |
| `xlabel` / `ylabel` | `str` | Axis labels |
| `theme` | `str` | Theme override for this plot |
| `legend` | `bool` | Show or hide legend |
| `size` | `tuple` | Figure size `(width, height)` in inches |
| `backend` | `str` | `"matplotlib"` (default) or `"plotly"` |
| `hover_data` | `list` | Column names to display on hover (Plotly backend) |

Full parameter documentation is available at [jack111i.github.io/Plotix](https://jack111i.github.io/Plotix).

---

## 📑 Examples

### 1. Multi-Panel Scientific Figure

```python
import plotix as px
import pandas as pd

df = pd.read_csv("data/simulation.csv")

px.subplot(
    1, 3,
    [
        px.line(df["time"], df["temperature"], title="Temperature"),
        px.line(df["time"], df["pressure"],    title="Pressure"),
        px.line(df["time"], df["humidity"],    title="Humidity"),
    ],
    theme="seaborn"
)
px.export("experiment.pdf")
```

### 2. Correlation Heatmap

```python
import plotix as px
import numpy as np

data = np.random.randn(10, 10)
px.heatmap(data, cmap="viridis", title="Correlation Matrix")
px.export("heatmap.svg")
```

### 3. Interactive 3-D Surface (Plotly Backend)

```python
import plotix as px
import numpy as np

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

px.surface(X, Y, Z, backend="plotly", title="Sine Surface")
px.export("surface.html")   # Opens in your default browser
```

### 4. Interactive Scatter with Hover Annotations

```python
import plotix as px

px.scatter(
    df["x"], df["y"],
    backend="plotly",
    title="Interactive Scatter",
    hover_data=["label"]
)
px.show()
```

---

## ⚙️ Configuration & Themes

| Method | Description |
|--------|-------------|
| `px.list_themes()` | Print all available theme names |
| `px.set_theme(name)` | Apply a theme globally |
| `px.load_theme(path)` | Load a custom JSON theme |

**Environment-based configuration:**

```bash
export PX_THEME=dark   # Set default theme via environment variable
```

Or place a `plotix.cfg` file in your project root:

```ini
[plotix]
theme = dark
```

---

## 📤 Exporting & Interactivity

| Format | Command | Notes |
|--------|---------|-------|
| PNG / JPG | `px.savefig("figure.png", dpi=300)` | High-DPI raster output |
| SVG / PDF | `px.savefig("figure.svg")` | Lossless vector output |
| Interactive HTML | `px.export("interactive.html")` | Requires `plotly` extra |
| Jupyter Notebook | `px.show()` | Renders inline in cell output |

---

## 🧪 Testing & CI

Install development dependencies and run the test suite locally:

```bash
pip install plotix[dev]
pytest tests/
```

The repository uses **GitHub Actions** for continuous integration, running the following checks on every push and pull request:

- `flake8` linting and `mypy` type checking
- Full test matrix across **Python 3.9, 3.10, and 3.11**
- Code coverage reporting

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get started:

1. **Fork** this repository
2. **Create a feature branch**: `git checkout -b feature/awesome-chart`
3. **Install dev dependencies**: `pip install plotix[dev]`
4. **Run tests locally**: `pytest tests/`
5. **Push** your branch and **open a Pull Request**

### Style Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) for code formatting
- Use [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)
- Keep imports minimal and explicit

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor guide.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](https://github.com/Jack111I/Plotix/blob/main/LICENSE) for details.

---

<div align="center">

**Plot it. Plot it better.**

If Plotix helps your work, consider giving it a ⭐ — it helps others discover the project.

</div>
