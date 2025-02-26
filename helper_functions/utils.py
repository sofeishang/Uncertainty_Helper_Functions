# helper_functions/utils.py
import numpy as np
import json
import regex as re

def inverse_logit(x):
    return 1 / (1 + np.exp(-x))

def logit(x):
    return np.log(x / (1 - x))

def convert_psychopy_circle2unit_circle_deg(arc_angles):
    temp_angles = json.loads(arc_angles)
    temp_angles[0] = np.deg2rad(temp_angles[0])
    temp_angles[1] = np.deg2rad(temp_angles[1])
    temp_angles[0] = (math.pi / 2 - temp_angles[0]) % (2 * math.pi)
    temp_angles[1] = (math.pi / 2 - temp_angles[1]) % (2 * math.pi)
    return [np.rad2deg(temp_angles[0]), np.rad2deg(temp_angles[1])]

def sub_offset(block_label, coin_angle, offset_lowV_lowN, offset_lowV_highN, offset_highV_lowN, offset_highV_highN):
    if block_label == "HighVolatility_LowNoise":
        return coin_angle - offset_highV_lowN
    if block_label == "HighVolatility_HighNoise":
        return coin_angle - offset_highV_highN
    if block_label == "LowVolatility_LowNoise":
        return coin_angle - offset_lowV_lowN
    if block_label == "LowVolatility_HighNoise":
        return coin_angle - offset_lowV_highN

def bin_slot_column(df, slot_column='slot', num_bins=14):
    col_name = 'slot_bin_' + str(num_bins)
    df[col_name] = pd.cut(df[slot_column], bins=num_bins, labels=range(1, num_bins + 1))
    return df

def extract_id(i):
    return re.sub(r'^.*?_', '', i)