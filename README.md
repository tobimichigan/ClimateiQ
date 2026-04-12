# ClimateiQ


<p> <img width="1200" height="720" alt="ClimateiQ Web and Mobile Application" src="https://github.com/tobimichigan/ClimateiQ/blob/main/graphical_plots/Slide1.PNG" /></p>
<p>ClimateiQ is a an Enviroment Friendly  App for Policy Makers and Practitioners</p> 
<p>Web Demo: <a href="https://handsonlabs.org/ClimateiQ/ClimateiQ.html" target="_blank"> ClimateiQ Web Demo</a></p>
<p>Mobile Demo: <a href="https://handsonlabs.org/ClimateiQ/ClimateiQMobile.html" target="_blank"> ClimateiQ Mobile Demo</a> </p>

<p> <h1>ABSTRACT</h1></p>

<p>ClimateIQ is a decision-support system that translates regional climate model outputs into actionable, sector-focused guidance for practitioners and policymakers. The platform ingests NA-CORDEX forcing and ERA5 reanalysis data to produce statistically and dynamically downscaled climate projections at ~25 km resolution, implemented as both a field-oriented mobile application and a feature-rich web dashboard. NA-CORDEX ERA5 
Technically, ClimateIQ combines a convolutional neural network for spatial pattern recognition with a long-short-term memory stage for temporal sequencing (CNN–LSTM), producing ensemble projections under five Shared Socioeconomic Pathway (SSP) scenarios for the period 2025–2100. The system emphasizes uncertainty transparency (ensemble spread and configurable confidence intervals), reproducibility (versioned inference weights and ERA5 traceability), and decision-relevance by exposing validation metrics (R², RMSE, cross-validation folds) alongside all operational outputs.
Functionally, the mobile application supports rapid, offline-capable triage workflows and live downscale inference for point coordinates; the web dashboard supports multi-scenario analysis, model diagnostics, and exportable, citation-ready products. Analytical features include multi-layer spatial maps (TAS anomaly, precipitation, heat index, PDSI), a six-sector vulnerability scoreboard (agriculture, water, urban heat/public health, infrastructure, energy, ecosystems), milestone tables for threshold crossing years, and an alerts feed for threshold exceedances. Guidance is provided for both practitioner workflows (site assessments, reservoir yield modeling, urban heat adjustments) and policymaker workflows (rapid briefings, annual adaptation planning, cross-sector coordination).
Limitations are stated explicitly: the 25 km grid cannot resolve sub-urban microclimates; variable coverage excludes some hazard indices; and residual model biases (RMSE ≈ 0.847°C) must be reported. ClimateIQ is presented as a scientific, reproducible bridge from ensemble climate science to operational adaptation planning designed to make uncertainty usable rather than opaque. 
</p>


<p><h1> Selected Model Graphical Plots</h1></p>

<p><h1>plot_11_downscaling_demo.png — “Spatial Downscaling ×4: Regional TAS”</h1>

<p><img width="1200" height="720" alt="plot_11_downscaling_demo.png — “Spatial Downscaling ×4: Regional TAS" src="https://github.com/tobimichigan/ClimateiQ/blob/main/model_results/plot_11_downscaling_demo.png" /></p>

Coarse Bilinear (×1 res) shows the baseline coarse bilinear interpolation of coarse input to fine grid. Hybrid Downscaled (×4)  model’s downscaled prediction (smoothed, realistic regional gradient). Added-Detail Delta (°C), the difference between hybrid downscaled and coarse bilinear (shows where model adds/subtracts detail).
Detailed interpretation

Coarse bilinear is noisy vertically (column/row artifacts) and lacks realistic latitudinal gradient shades visible in hybrid output.
Hybrid output is smooth, captures latitudinal gradient and regional structure with smaller dynamic range (colorbar ±~3°C).
Added-detail delta highlights local corrections (positive and negative) up to large magnitudes (the delta colorbar shows a wide range; check scaling)  this is the learned high-frequency detail the model applied on top of bilinear baseline.</p>

<p><h1>plot_05_metrics_summary.png, “Model Performance across All Splits”</h1>

<p><img width="1200" height="720" alt="plot_05_metrics_summary.png — Model Performance — All Splits" src="https://github.com/tobimichigan/ClimateiQ/blob/main/model_results/plot_05_metrics_summary.png" /></p>

Grouped bar charts for multiple metrics across TRAIN/VAL/TEST/HOLDOUT: RMSE (~0.83 scaled), MAE (~0.512), R² (~0.998), Pearson r (~0.999), and “Within 1°C pct” (~0.879).
Interpretation
All splits show near-identical performance indicates consistency across splits.
“Within 1°C” ≈ 87.9%: the model predicts within ±1°C for roughly 88% of samples a practical accuracy metric for climate downscaling. </p>

<h1>plot_06_holdout_deep.png, “Holdout (Unseen) Data , shows Deep Evaluation”</h1>

<p><img width="1200" height="720" alt="plot Holdout (Unseen) Data — Deep Evaluation" src="https://github.com/tobimichigan/ClimateiQ/blob/main/model_results/plot_06_holdout_deep.png" /></p>

Shows (6 panels) on a single Dashboard:
Pred vs Actual scatter (top-left; R²=0.9981).
Residual histogram (top-middle) with mean µ and σ annotated (µ≈0.089, σ≈0.830).
Residual Q–Q plot (top-right)  tests normality of residuals.
CDF of absolute error with a dashed line at 1°C and annotation “87.9% within 1°C” (bottom-left).
Error percentile curve (bottom-middle)  shows percentile vs absolute error.
Time series snippet: first 600 samples of Actual vs Pred (bottom-right).



<p><h1>ClimateIQ:The Climate Downscaling AI Pipeline and  The GraphCast Fine-Tuned AI Model</h1>

<p><img width="1200" height="720" alt="ClimateIQ:The Climate Downscaling AI Pipeline and  The GraphCast Fine-Tuned AI Model " src="https://github.com/tobimichigan/ClimateiQ/blob/main/graphical_plots2/Slide1.PNG" /></p>

<p>ClimateiQ’s overall contribution is that it turns climate science into a practical decision-support system instead of leaving it as raw model output. The project combines climate-data ingestion, downscaling, uncertainty reporting, and user-facing visualization into one workflow that is explicitly aimed at practitioners and policymakers. According to the algorithmic approach, it ingests NA-CORDEX and ERA5 data, produces downscaled projections at about 25 km resolution, supports five SSP scenarios from 2025 to 2100, and exposes outputs through both a mobile app and a web dashboard. That makes the software valuable as an end-to-end climate intelligence pipeline rather than just a forecasting model.
A major benefit of the project is that it improves usability and trust at the same time. The repo emphasizes uncertainty transparency, reproducibility, and decision relevance by reporting validation metrics such as R², RMSE, and cross-validation folds alongside operational outputs. It also packages the results into sector-oriented products such as spatial maps, vulnerability scoring, milestone tables, and threshold alerts, which helps users move from “what does the model say?” to “what action should we take?” In practice, that is a strong contribution for climate adaptation work, because it bridges the gap between technical modeling and real-world planning.
The notebooks show that the project’s contribution deepened over time from a working prototype into a more scientifically rigorous pipeline. The updated notebook adds stratified temperature sampling, spatial block cross-validation, a local-mean baseline, heteroscedastic uncertainty modeling, and tail fine-tuning for difficult temperature ranges. It also adds terrain and coastal proxy features, removes a multicollinear latitude feature, and applies a variance-stabilizing log transform. Those changes are important because they make the model less biased, more robust to spatial leakage, and better suited to climate data’s uneven distributions and spatial autocorrelation.
Another benefit is operational flexibility. The repository presents both a field-oriented mobile workflow and a richer web dashboard, and it explicitly notes that the mobile side can support rapid, offline-capable triage and point-based inference. That matters for real deployment because climate users often work in constrained environments where internet access, compute capacity, or specialist support may be limited. By supporting exportable, citation-ready products and offline-friendly workflows, ClimateiQ becomes more practical for agencies, NGOs, and local practitioners.
The project also contributes a strong foundation for future scaling. Its modular structure, GraphCast-related integration, and notebook evolution show a pathway toward more advanced climate AI systems that can be adapted to other regions, variables, and decision contexts. The benefit here is not just one improved climate app; it is a reusable architecture for climate downscaling and environmental intelligence that can be extended as datasets, methods, and user needs grow. </p>
