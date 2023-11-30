---
title: dialogdata
layout: default
nav_exclude: true
---
Used in combination with the [dialogtype](dialogtype) [property](property) to configure information on how to present [data-item](data-item).

If the DialogType property is configured to ***Map***, the DialogData should refer to the data item to which the [geography](geography) data is configured ([feature-attribute](feature-attribute)). This is needed to inform the GeoDMS how to visualise the [geography](geography) domain unit of the requested data item.

The DialogData property can also be configured for a [values-unit](values-unit) describing the [how-to-configure-a-coordinate-system](how-to-configure-a-coordinate-system) used for map views. In that case the DialogData can be configured with one or multiple attribute(s) referring to geographic information. These [attribute](attribute) will then be grouped into a background layer that is by default presented in each map view.

If the feature attribute is called (G)(g)eometry, this property does not have to be configured (since version 7.206).