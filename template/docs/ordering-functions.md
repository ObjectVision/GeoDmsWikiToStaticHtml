---
title: ordering-functions
layout: default
parent: operator
nav_order: 30
---
Ordering [operators-and-functions](operators-and-functions) are used to compare or order [data-item](data-item):

- [eq](eq) (==)
- [eq_or_both_null](eq_or_both_null)
- [float_isnearby](float_isnearby)
- [lt](lt) (\<)
- [lt_or_lhs_null](lt_or_lhs_null)
- [le](le) (\<=)
- [le_or_lhs_null](le_or_lhs_null)
- [gt](gt) (>)
- [gt_or_rhs_null](gt_or_rhs_null)
- [ge](ge) (>=)
- [ge_or_rhs_null](ge_or_rhs_null)
- [ne](ne) (\<\>)
- [ne_or_one_null](ne_or_one_null)

<!-- -->

- [argmax](argmax) - *the order number of the argument with the highest value*
- argmax_uint8_16 - *versions of the [argmax](argmax) function resulting in a uint8/16 data item*
- [argmax_alldefined](argmax_alldefined) - *variant of the [argmax](argmax) with defined values for all defined arguments*
- argmax_alldefined_uint8_16 - *versions of the [argmax_alldefined](argmax_alldefined) function resulting in a uint8/16 data item*
- [argmax_ifdefined](argmax_ifdefined) - *variant of the [argmax](argmax) with defined values for any defined arguments*
- argmax_ifdefined_uint8_16 - *versions of the [argmax_ifdefined](argmax_ifdefined) function resulting in a uint8/16 data item*

<!-- -->

- [argmin](argmin) - *the order number of the argument with the lowest value*
- argmin_uint8_16 - *versions of the [argmin](argmin) function resulting in a uint8/16 data item*
- [argmin_alldefined](argmin_alldefined) - *variant of the [argmin](argmin) with defined values for all defined arguments*
- argmin_alldefined_uint8_16 - *versions of the [argmin_alldefined](argmin_alldefined) function resulting in a uint8/16 data item*
- [argmin_ifdefined](argmin_ifdefined) - *variant of the [argmin](argmin) with defined values for any defined arguments*
- argmin_ifdefined_uint8_16 - *versions of the [argmin_ifdefined](argmin_ifdefined) function resulting in a uint8/16 data item*

<!-- -->

- [max_elem](max_elem) - *the highest value of the arguments*
- [max_elem_alldefined](max_elem_alldefined) - *variant of the [max_elem](max_elem) with defined values for all defined arguments*
- [max_elem_ifdefined](max_elem_ifdefined) - *variant of the [max_elem](max_elem) with defined values for any defined arguments*

<!-- -->

- [min_elem](min_elem) - *the lowest values of the arguments*
- [min_elem_alldefined](min_elem_alldefined) - *variant of the [min_elem](min_elem) with defined values for all defined arguments*
- [min_elem_ifdefined](min_elem_ifdefined) - *variant of the [min_elem](min_elem) with defined values for any defined arguments*

<!-- -->

See also: [aggregation-functions](aggregation-functions) for [min](min) and [max](max)

- [median](median)

<!-- -->

- [sort](sort) - *order the values*
- [reverse](reverse) - *reverse the order of values*