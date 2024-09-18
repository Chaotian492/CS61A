import math


def gain(size, class_two):
    yes_1 = class_two[0] / size
    no_2 = class_two[1] / size

    return -(yes_1 * math.log2(yes_1) + no_2 * math.log2(no_2))


def gini(size, a_size, a_yes, aout_yes):
    a_probability = a_yes / a_size
    a_frequency = a_size / size
    a_gini = a_frequency * (2 * a_probability * (1 - a_probability))

    aout_prob = aout_yes / (size - a_size)
    aout_freq = (size - a_size) / size
    aout_gini = aout_freq * (2 * aout_prob * (1 - aout_prob))
    return a_gini + aout_gini
