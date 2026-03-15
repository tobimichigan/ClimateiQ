# ClimateiQ

ClimateiQ is a an Enviroment Friendly  App for Policy Makers and Practitioners 


<p> # ABSTRACT</p>

<p>ClimateIQ is a decision-support system that translates regional climate model outputs into actionable, sector-focused guidance for practitioners and policymakers. The platform ingests NA-CORDEX forcing and ERA5 reanalysis data to produce statistically and dynamically downscaled climate projections at ~25 km resolution, implemented as both a field-oriented mobile application and a feature-rich web dashboard. NA-CORDEX ERA5 
Technically, ClimateIQ combines a convolutional neural network for spatial pattern recognition with a long-short-term memory stage for temporal sequencing (CNN–LSTM), producing ensemble projections under five Shared Socioeconomic Pathway (SSP) scenarios for the period 2025–2100. The system emphasizes uncertainty transparency (ensemble spread and configurable confidence intervals), reproducibility (versioned inference weights and ERA5 traceability), and decision-relevance by exposing validation metrics (R², RMSE, cross-validation folds) alongside all operational outputs.
Functionally, the mobile application supports rapid, offline-capable triage workflows and live downscale inference for point coordinates; the web dashboard supports multi-scenario analysis, model diagnostics, and exportable, citation-ready products. Analytical features include multi-layer spatial maps (TAS anomaly, precipitation, heat index, PDSI), a six-sector vulnerability scoreboard (agriculture, water, urban heat/public health, infrastructure, energy, ecosystems), milestone tables for threshold crossing years, and an alerts feed for threshold exceedances. Guidance is provided for both practitioner workflows (site assessments, reservoir yield modeling, urban heat adjustments) and policymaker workflows (rapid briefings, annual adaptation planning, cross-sector coordination).
Limitations are stated explicitly: the 25 km grid cannot resolve sub-urban microclimates; variable coverage excludes some hazard indices; and residual model biases (RMSE ≈ 0.847°C) must be reported. ClimateIQ is presented as a scientific, reproducible bridge from ensemble climate science to operational adaptation planning designed to make uncertainty usable rather than opaque. 
</p>




<p></p>
