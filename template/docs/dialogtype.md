---
title: dialogtype
layout: default
nav_exclude: true
---
Together with the [dialogdata](dialogdata) property, this property defines how data is visualised. The following options are available:

-   ***Classification***: Defines a ClassBreaks item of a classification scheme. Configure this option for ClassBreaks items, to inform the GeoDMS the attribute is used for class boundaries of classifications and can be viewed/modified with the
    Classification and Palette editor in the GeoDMS GUI. See ClassBreaks item in a classification scheme for more information on ClassBreaks items.
-   ***Palette***: Defines a palette item of a classification scheme. Configure this option for palette items, to inform the GeoDMS the attribute is used for the definition of colors in classifications and can be viewed/modified  with the (Classification and) Palette editor in the GeoDMS GUI. See Visualisation style items in a classification scheme for more information on palette items.
-   ***Labels***: Defines a labels item of a classification scheme. Configure this option for labels items, to inform the GeoDMS the attribute is used for the labels in  classifications and can be viewed/modified with the (Classification and) Palette editor in the GeoDMS GUI. See Labels item in a classification scheme for more information on labels items.
-   ***Map***: This option is configured for domain units, to inform the GeoDMS that all data items with this domain unit can be visualised in a map view. The DialogData property should refer to the attribute with the geographical data configured. If the [feature-attribute](feature-attribute) is called (G)(g)eometry, this property does not have to be configured (since version 7.206).
-   ***SymbolSize***: Defines the size in pixels for point data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [point-visualisation](point-visualisation).
-   ***SymbolWorldSize***: Defines the worldsize in the coordinate system unit for point data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [point-visualisation](point-visualisation).
-   ***SymbolColor***: Defines the color in rgb values for point data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [point-visualisation](point-visualisation).
-   ***SymbolIndex***: Defines the index value in the font for point data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [point-visualisation](point-visualisation).
-   ***SymbolFont***: Defines the font for point data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [point-visualisation](point-visualisation).
-   ***PenWidth***: Defines the width in pixels for arc data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [arc-visualisation](arc-visualisation).
-   ***PenWorldWidth***: Defines the worldwidth in the coordinate system unit for arc data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [arc-visualisation](arc-visualisation).
-   ***PenColor***: Defines the color in rgb values for arc data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [arc-visualisation](arc-visualisation).
-   ***PenStyle***: Defines the style for arc data in the GeoDMS map view.See [visualisation-style](visualisation-style) or [arc-visualisation](arc-visualisation).
-   ***BrushColor***: Defines the color in rgb values for the interior of polyon data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [polygon-visualisation](polygon-visualisation).
-   ***HatchStyle***: Defines the style for the interior of polyon data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [polygon-visualisation](polygon-visualisation).
-   ***LabelText***: Defines the labels as strings for point and polygon data in the GeoDMS map view. See [visualisation-style](visualisation-style) or [label-visualisation](label-visualisation).
-   ***LabelSize***: Defines the size in pixels for labels in the GeoDMS map view. See [visualisation-style](visualisation-style) or [label-visualisation](label-visualisation).
-   ***LabelWorldSize***: Defines the worldsize in the coordinate system unit for labels in the GeoDMS map view. See [visualisation-style](visualisation-style) or [label-visualisation](label-visualisation).
-   ***LabelColor***: Defines the color in rgb values for labels in the GeoDMS map view. See [visualisation-style](visualisation-style) or [label-visualisation](label-visualisation).
-   ***LabelFont***: Defines the font for labels in the GeoDMS map view. See [visualisation-style](visualisation-style) or [label-visualisation](label-visualisation).
-   ***MinPixSize***: Defines the lower limit of the scale range to visualise a layer. See [scale-dependent-visualisation](scale-dependent-visualisation).
-   ***MaxPixSize***: Defines the upper limit of the scale range to visualise a layer. See [scale-dependent-visualisation](scale-dependent-visualisation).