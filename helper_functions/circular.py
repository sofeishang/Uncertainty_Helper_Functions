# helper_functions/circular.py
import math
import numpy as np

def mindist(angle_1, angle_2):
    if angle_2 > angle_1:
        return (angle_2 - angle_1) if (angle_2 - angle_1) < math.pi else (angle_2 - angle_1) - 2 * math.pi
    else:
        return (angle_2 - angle_1) if (angle_1 - angle_2) < math.pi else (angle_2 - angle_1) + 2 * math.pi

def normalize_pi_neg_pi(angle):
    while angle > math.pi:
        angle -= 2.0 * math.pi
    while angle < -math.pi:
        angle += 2.0 * math.pi
    return angle

def normalize_0_2pi(angle):
    return angle % (2 * math.pi)

def diff(angle_1, angle_2):
    return angle_1 - angle_2

def find_CB(prediction_error, diff_outcome_next_belief, diff_current_belief_next_belief):
    if np.sign(prediction_error) == np.sign(diff_outcome_next_belief):
        return diff_outcome_next_belief
    if (abs(diff_outcome_next_belief) > (0.5 * math.pi)) and (abs(diff_current_belief_next_belief) < (0.5 * math.pi)):
        return (2 * math.pi + diff_outcome_next_belief) if np.sign(prediction_error) > 0 else (-2 * math.pi + diff_outcome_next_belief)
    return diff_outcome_next_belief