---
title: feasibilitytest
layout: default
nav_exclude: true
---
The Feasibility Test is a test within the DiscreteAlloc function that tests whether the claims are compatible with the amount of grid cells per region. It does not take into account that some cells may have a suitability below the threshold. Assuming that all cells are suitable enough for each land use type, the question whether a feasible allocation results exists can be reduced to the same question with all suitabilities being zero, which can be simplified by aggregating all cells per atomic region. Based on this assumption and reduction, the feasibility test attempts to make a Linear Assignment of all land units of each atomic region to all claims that include that region such that all claimed restrictions are met.