# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.01] — 2026-07-09

### Added

#### Core analysis package (`surf/`)

- **`probability_surface.py`** — Gaussian position-probability density and
  confidence surfaces per shoreline year; per-pixel change-probability raster
  for each year pair (Bhattacharyya overlap coefficient); fixed-length
  shoreline segmentation with PROB_CHANGE and MAGNITUDE attributes.
- **`rate_of_change.py`** — End Point Rate (EPR) and Linear Regression Rate
  (LRR) statistics along a configurable dense transect grid; rate-change
  polygons attributed with MAGNITUDE, RATE, and PROB_CHANGE.
- **`water_level.py`** — NOAA CO-OPS Tides & Currents API lookup for water-
  level stage at each site and shoreline acquisition date; covers both marine
  and Great Lakes stations; CSV output for uncertainty-budget integration.
- **`config.py`** — `acquisition_date` field on `ShorelineYear` for
  water-level queries; full `validate_config()` with structured error messages.
- **`pipeline.py`** — Automatic CRS normalization across shoreline years when
  files are in different projected systems; defensive guard against fewer than
  2 shoreline years reaching EPR/LRR computation.
- `surf water-levels` and `surf gui` CLI subcommands.
- Nearest-transect net-distance lookup for magnitude attribution on
  change-probability segments.

#### GUI application (`gui_app/`)

- Rebuilt tkinter/ttk desktop application (`SURFApp`) with **Settings**,
  **Sites**, and **Log** tabs; YAML config save/load round-trip.
- Background-thread pipeline execution with live log streaming.
- `build_exe.py` — PyInstaller `--onedir` build script; builds in system temp
  to avoid OneDrive file locks; automatic replacement of the pyproj-bundled
  `proj.db` with the system version to fix PROJ minor-version mismatches.
- GDAL/PROJ environment variable fix for frozen executables.

#### QGIS processing plugin (`qgis_plugin/surf_qgis/`)

- `SURFPlugin`, `SURFProvider`, `SURFAlgorithm`, `SURFDialog` — full QGIS
  Processing plugin exposing the pipeline as a native algorithm; results
  loaded onto the map canvas on completion.

#### Documentation and packaging

- Continuous probability-surface and rate-of-change example YAML configs.
- Six-panel composite figure and GUI-tab screenshots.
- JOSS manuscript draft (`paper.md` / `paper.bib`).
- PyPI package (`shoreline-surf`); published to PyPI.
- DOI: [10.5281/zenodo.21286139](https://doi.org/10.5281/zenodo.21286139)

### Changed

- **Package renamed** from `ShorelineUncertainty` / `shoreline-uncertainty`
  to `SURF` / `shoreline-surf` throughout all source files, build scripts,
  class names, CLI entry points, and distribution artifacts.
- **Default CRS** set to `EPSG:3175` (NAD83 / Great Lakes Albers).
- **Default raster cell size** set to 0.5 m.
- Legacy ArcGIS Pro scripts: hardcoded absolute paths replaced with `# TODO:`
  placeholders; `@author` block updated with current contact information.

### Fixed

- **12 TiB raster allocation** — CRS mismatch between 1938 (Hotine Oblique
  Mercator) and 2010 (EPSG:26989) Allegan shapefiles caused `_union_bounds`
  to span incompatible coordinate spaces. Fixed by normalising all shoreline
  years to a common CRS before any spatial math.
- **PROJ database version mismatch in PyInstaller bundle** — bundled `proj.db`
  (minor version 4) incompatible with conda PROJ DLL (requires ≥ 6). Fixed
  by replacing bundled database with system copy post-build.
- **`ValueError: end_point_rate needs at least 2 shoreline years`** — stale
  `shoreline_uncertainty.egg-info` removed; defensive guard added in pipeline.
- **File truncation by OneDrive sync daemon** — multiple source files silently
  truncated mid-function; all restored.
- Stale `build/ShorelineUncertainty/` and `build_exe/ShorelineUncertainty/`
  PyInstaller artifacts removed.

---

## [1.0] — 2026-07-08

Initial release of the shoreline change uncertainty analysis program, based on
the research methods of Wernette et al. (2017, 2020).

### Added

- **`uncertainty.py`** — RMSE95 positional uncertainty from base-map,
  georeferencing, and interpretation error components (FGDC 1998).
- **`epsilon_bands.py`** — Overlapping Double Buffer (ODB) significance test
  (Ps = Area(Intersection)/Area(Union)); Perkal-style iterative buffer-growth
  variant.
- **`transects.py`** — Shore-normal transect generation; shoreline
  intersection; wide/long table output.
- **`raster_output.py`** — GeoTIFF similarity-index and significant-change
  rasters from ODB buffer geometry unions.
- **`critical_areas.py`** — Perkal-band critical-area identification.
- **`comparison.py`** — Professional-delineation comparison statistics.
- **`config.py`** — YAML-driven `RunConfig` / `SiteConfig` / `ShorelineYear`
  dataclasses; `load_config()`.
- **`pipeline.py`** — End-to-end `run_pipeline()` / `run_site()` with
  per-stage gating.
- **`cli.py`** — `surf run` entry point.
- **`io_utils.py`** — CRS normalization; vector and raster I/O helpers.
- 144-test pytest suite covering all modules.
- Example YAML configurations and Allegan, Michigan shoreline data (1938 and
  2010) from Wernette et al. (2017).
- `README.md`, `MIGRATION.md`, `LICENSE` (MIT).
- DOI: [10.5281/zenodo.21285653](https://doi.org/10.5281/zenodo.21285653)

---

[1.01]: https://github.com/pwernette/shoreline-surf/releases/tag/1.01
[1.0]: https://github.com/pwernette/shoreline-surf/releases/tag/1.0
