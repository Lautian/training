#!/usr/bin/env python3
import random

UPPER = [
	"bicep_curl,",
	"bicep_curl_half_whole",
	"scoop",
	"shoulder_press",
	"arnold_press",
	"curl_and_press",
	"pullover",
	"tricep_overhead",
	"tricep_pushup",
	"spiderman_pushup",
	"pushup",
	"pushup_step_walk",
	"mountain_climbers",
	"barbell_row",
	"dips",
	"side_raise",
	"front_raise",
	"side_brace",
	"shadow_boxing",
]

LOWER = [
	"squat",
	"squat_jump_step",
	"split_jump_step",
	"squat_jack_elastic",
	"squat_jump",
	"squat_snowboard",
	"lunge_scissors_opt_bounce",
	"dynamic_lunge_opt_step",
	"burpee",
	"jump_rope",
	"jumping_jacks",
	"knee_raise",
	"hip_raise_opt_step",
	"mambo_up_down_step",
	"forward_kick",
	"roundhouse_kick",
	"basic_step",
	"bear_jack_plank",
]

CORE = [
	"plank",
	"plank_high_low",
	"plank_leg_raise",
	"plank_hip_dip",
	"side_plank",
	"basic_crunch",
	"side_crunch_bent_legs",
	"lateral_crunch",
	"oblique_crunch",
	"leg_raises",
	"leg_scissors",
]

def circuit(sets=5, combi=(UPPER, LOWER), avoid_similar=True):
	"""Generate sets sets of combi combinations
	of exercises to be used in a circuit.
	Return the set of exercises as a list of len sets,
	of tuples length combi.
	"""
	random.seed()
	# circuit = []
	circuit = [random.sample(combi_elem, sets) for combi_elem in combi]
	circuit = list(zip(*circuit))
	return circuit

if __name__ == "__main__":
    print(circuit())