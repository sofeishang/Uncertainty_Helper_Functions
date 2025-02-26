# Uncertainty_Helper_Functions

# Helper Functions Package

This package provides a set of helper functions for handling circular data, plotting, and various utilities.

## Installation

To install the package, navigate to the root directory and run:

```
pip install .
```

## Modules

### Circular Functions (`circular.py`)
- `mindist(angle_1, angle_2)`: Computes the minimum distance between two angles.
- `normalize_pi_neg_pi(angle)`: Normalizes an angle to be within [-π, π].
- `normalize_0_2pi(angle)`: Normalizes an angle to be within [0, 2π].
- `diff(angle_1, angle_2)`: Computes the difference between two angles.
- `find_CB(prediction_error, diff_outcome_next_belief, diff_current_belief_next_belief)`: Adjusts circular differences.

### Plotting Functions (`plotting.py`)
- `plot_param_trait(effect, trait, data_frame, *export_path_fig)`: Plots the relationship between a trait and effect.
- `plot_block_trait(trait, outcome_var, data_frame, *export_path_fig)`: Plots relationships across experimental blocks.
- `plot_model3_param_trait(effect, variable, trait, data_frame, *export_path_fig)`: Regression plot for model parameters.
- `plot_model3_project3_param_trait(effect, variable, trait, data_frame, *export_path_fig)`: Similar, but project-specific.
- `plot_alpha_beta_project3_param_trait(effect, variable, trait, data_frame, *export_path_fig)`: Plots for alpha-beta model parameters.

### Utility Functions (`utils.py`)
- `inverse_logit(x)`: Computes the inverse logit transformation.
- `logit(x)`: Computes the logit function.
- `convert_psychopy_circle2unit_circle_deg(arc_angles)`: Converts angles from PsychoPy to unit circle coordinates.
- `sub_offset(block_label, coin_angle, offset_lowV_lowN, offset_lowV_highN, offset_highV_lowN, offset_highV_highN)`: Adjusts coin angles based on block labels.
- `bin_slot_column(df, slot_column='slot', num_bins=14)`: Bins a column into equal intervals.

## Usage

Import the package in Python:

```python
from helper_functions import circular, plotting, utils
```

