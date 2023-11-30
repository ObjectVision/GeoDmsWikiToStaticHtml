---
title: selection-functions
layout: default
parent: operator
nav_order: 38
---
Selection [operators-and-functions](operators-and-functions) are used to create new [domain-unit](domain-unit) with selection of elements from other domain units.

- [select_with_org_rel](select_with_org_rel) or [subset](subset) - *configures a new unit, based on a condition*
- select_uint8_16_32_64_with_org_rel - *versions of the [select_with_org_rel](select_with_org_rel) function, resulting in a unit with the explicit value type*
- [select](select) and [select_data](select_data) - *similar to select_with_org_rel, but faster and less memory intensive in case of dense subsets*
- select_uint8_16_32_64 - *versions of the [select](select) function, resulting in a unit with the explicit value type*
- [select_with_attr_by_org_rel](select_with_attr_by_org_rel) - *similar to select_with_org_rel/subset, resulting in a unit and a set of attributes*
- select_uint8_16_32_64_with_attr_by_org_rel - *versions of the [select_with_attr_by_org_rel](select_with_attr_by_org_rel) function, resulting in a unit with the explicit value type*
- [select_with_attr_by_cond](select_with_attr_by_cond) - *similar to select_with_org_rel, resulting in a unit and a set of attributes*
- select_uint8_16_32_64_with_attr_by_cond - *versions of the [select_with_attr_by_cond](select_with_attr_by_cond) function, resulting in a unit with the explicit value type*
- [select_with_org_rel_with_attr_by_cond](select_with_org_rel_with_attr_by_cond) - *similar to select_with_attr_by_cond: condition is used for all collections, but an org_rel is also produced*
- select_uint8_16_32_64_with_attr_by_cond - *versions of the [select_with_attr_by_cond](select_with_attr_by_cond) function, resulting in a unit with the explicit value type*