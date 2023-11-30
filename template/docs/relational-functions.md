---
title: relational-functions
layout: default
parent: operator
nav_order: 37
---
Relational [operators-and-functions](operators-and-functions) are used to relate [data-item](data-item) of different [domain-unit](domain-unit) like [lookup](lookup) or [rjoin](rjoin) or create new domain units like [unique](unique). 

Selection functions van be found on the separate page: [selection-functions](selection-functions).

- [id](id) - *index numbers*
- [mapping](mapping) - *to map attributes between domain units*

<!-- -->

- [lookup](lookup) - *using a relation to find the relevant entries*
- [rlookup](rlookup) - *using a foreign key attribute to make a relation*
- [rjoin](rjoin) - *using a foreign key to find the relevant entries, combining lookup and rlookup*
- [join_equal_values](join_equal_values) - *find all combinations of A and B wherfe A.x_rel is equal to B.x_rel*
- [join_equal_values_uint8_16_32_64](join_equal_values_uint8_16_32_64) - *find all combinations of A and B wherfe A.x_rel is equal to B.x_rel, resulting in a domain unit with the explicit value type*

<!-- -->

- [index](index) - *an index number based on a sort order*
- [direct_index](direct_index)

<!-- -->

- [invert](invert) - *inverts a relation*

<!-- -->
- [collect_attr_by_org_rel](collect_attr_by_org_rel) - *collects a set of attributes to a new domain unit, using an org_rel attribute (lookup)*
- [collect_attr_by_cond](collect_attr_by_cond) - *collects a set of attributes to a new domain unit, using a condition*
- [collect_by_cond](collect_by_cond) - *collects an attributes to a new domain unit, using a condition*
- [recollect_by_cond](recollect_by_cond) -  *recollects attribute values of a selection back to an original set using the condition for the selection.*

<!-- -->
- [unique](unique) - *configures a new unit, based on the unique values*
- [unique_uint8_16_32_64](unique_uint8_16_32_64) - *configures a new unit, based on the unique values, with a uint8_16_32_64 values unit*
- [union](union) - *obsolete, only in use for backward compatibility*
- [union_unit](union_unit) - *configures a new unit, based on the union of other units*
- [union_unit_uint8_16_32_64](union_unit_uint8_16_32_64) - *configures a new unit, based on the union of other units, with a uint8_16_32_64 values unit*
- [union_data](union_data) - *configures a new attribute, based on the union of other data items*
- [combine](combine) - *configures a new unit, based on the Cartesian product of other units*
- [combine_unit_uint8_16_32_64](combine_unit_uint8_16_32_64) - *configures a new unit, without subitems, based on the Cartesian product of other units, with a uint8_16_32_64 values unit*
- [combine_uint8_16_32_64](combine_uint8_16_32_64) - *configures a new unit, based on the Cartesian product of other units, with a uint8_16_32_64 values unit*
- [combine_data](combine_data) - *configures a new attribute, based on the Cartesian product of other data items*

<!-- -->

- [merge](merge) - *merges the values of a data item, based on an option data item*

<!-- -->

- [overlay](overlay) *- an uint16 domain unit with the unique values of multiple grid attributes*
- [overlay32](overlay32) *- an uint32 domain unit with the unique values of multiple grid attributes*
- [overlay64](overlay64) *- an uint64 domain unit with the unique values of multiple grid attributes*
