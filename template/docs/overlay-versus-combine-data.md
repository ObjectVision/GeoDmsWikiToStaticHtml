---
title: overlay-versus-combine-data
layout: default
nav_exclude: true
---
*[configuration-examples](configuration-examples) Overlay versus Combine_data*

This script explains the difference between the [overlay](overlay) and the [combine_data](combine_data) operator.

The overlay operator makes values depending on the occurence of a unique combination in multiple [data-item](data-item). The [unique](unique) operator
on the UnionData [subitem](subitem) of the overlay result, results in the set of unique occurences of combinations.

The combine_data operator combines data items and result in index number for the combined unit, the first argument of the [combine](combine) function. This combined unit combines two units and makes entries for each possible combination.

So the overlay function looks at the actual equal combinations in the data items, where the combine_data looks at all possible combinations.

## how to use

It is adviced to use the overlay function if the number of actual unique combinations in the data is much less than the possible combinations (for instance in determining the set of atomic regions in a land use model).

Use the combine_data function if the number of possible combinations is limited and you want to use the same [visualisation-style](visualisation-style) and labels for the same combinations.

## download

- [configuration/data](https://www.geodms.nl/downloads/GeoDMS_Academy/concepts_overlay_versus_combine_data.zip)

## functions

- [overlay](overlay)
- [combine](combine)
- [combine_data](combine_data)