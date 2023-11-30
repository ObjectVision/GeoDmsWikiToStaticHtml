---
title: table-view
layout: default
nav_exclude: true
---
_[user-guide-geodms-gui](user-guide-geodms-gui)_ - table view

## Table View

All [data-item](data-item) can be visualized in table view. One table presents [data-item](data-item) or a set of data items of the same [domain-unit](domain-unit). The table is the default view for items that cannot be visualized in a [map-view](map-view), these items can be:
- Data items for which the domain unit cannot be georeferenced, in the [treeview](treeview) indicated by the icon: ![](../assets/img/GUI/tv_table.bmp) 
- Containers with data items as [subitem](subitem)s (first level subitems). The first data item of this container determines the domain unit of the Table, all data items that have this same common domain unit are added to the table. These items are indicated by the icon: ![](../assets/img/GUI/tv_container_table.bmp)
 

![](../assets/img/GUI/tableview.png)<br>
_example of a table for a selection of municipalities in a region_

This table presents 4 columns ([attribute](attribute) for the [domain-unit](domain-unit): cbs_gemeente (selection of 13 municipality). The name and [cardinality](cardinality) of this domain is presented in the title of the view.

For tables with attributes a first column is always automatically added, called _id_. This column presents the [index-numbers](index-numbers) of the domain (for [parameter](parameter), such a column is not added). In this table, after the index number a name of the municipality is presented, between brackets). This can be achieved by configuring a label string attribute as [subitem](subitem) of the domain unit. In tables where [relation](relation) to this domain are presented, these labels are also shown. 

## activate table view  

As with the map view, a new table can be activated for a tree item, or the tree item can be added to an already opened table (if this opened view is of the same domain unit as the requested data item). The following table shows the possible actions to visualize a tree item in a Table and the results of the actions.

|action|no active table for the requested domain|active table for the requested domain|active table for other domain|
|------|------------------|----------------|----------------|
|**Double click** on active [tree-item](tree-item) (if Table is default viewer, indicated by the ![](../assets/img/GUI/tv_table.bmp) or ![](../assets/img/GUI/tv_container_table.bmp) icon)|New Table window with the requested data item or all the subitems at the first level of the found domain.|Data item or subitems at the first level with the same domain unit are added to the active table. |New Table window with the requested data item or all the subitems at the first level of the found domain.|
|Main/pop-up menu option **Default View** (only if the Table is the default viewer, indicated by the ![](../assets/img/GUI/tv_table.bmp) or ![](../assets/img/GUI/tv_container_table.bmp) icon) on active [tree-item](tree-item)|New Table window with the requested data item or all the subitems at the first level of the found domain.|Data item or subitems at the first level with the same domain unit are added to the active table. |New Table window with the requested data item or all the subitems at the first level of the found domain.|
|Main/pop-up menu option **Table View** on active [tree-item](tree-item)|New Table window with the requested data item or all the subitems at the first level of the found domain.|Data item or subitems at the first level with the same domain unit are added to the active table. |New Table window with the requested data item or all the subitems at the first level of the found domain.|
|**Ctrl-D** on active [tree-item](tree-item)|New Table window with the requested data item or all the subitems at the first level of the found domain.|Data item or subitems at the first level with the same domain unit are added to the active table. |New Table window with the requested data item or all the subitems at the first level of the found domain.|
|**Drag and drop** active [tree-item](tree-item) to view area/active Table View|New Table window with the requested data item or all the subitems at the first level of the found domain.|Data item or subitems at the first level with the same domain unit are added to the active table. |New Table window with the requested data item or all the subitems at the first level of the found domain.|

## working with tables

The **width** of the columns can be adapted by moving the mouse to the header row, on the border between two columns. A mouse pointer with two arrows appear. Click with the left mouse button, keep this button pressed and move the mouse to the left or the right to change the size of the columns.

The **sequence of columns** can be adapted with drag and drop on the column header. Click with left mouse button on a header, keep the mouse pressed and move the mouse to the requested position.

In the table, a cell or a column can get the **focus**. Click on a cell or a column header to set the focus. Also, a focus rectangle can be used to set the focus to multiple cells. Therefore, first set the focus to one cell and use a left mouse-click or the arrow keys to enlarge the focus rectangle (colored black). Still in a focus rectangle, there is always one focus cell (colored blue). 

By double clicking on a cell, a [valueinfo](valueinfo) window appears.

## menu
![](../assets/img/GUI/popupmenu_table.png)<br>

With a right mouse click on the label a pop-up menu for the column is activated, with the following options:
- **Sort on _layer_** on data item name: sort values ascending or descending.
- **Relative Display (as % or total)**: present the numeric values as percentage of the total.
- **GoTo (Ctrl-G): take clipboard contents as row number and go there** : paste the contents of the clipboard, interpret it as row number and jump to this row in the table. 
- **FindNextValue (Ctrl-F): take clipboard contents as value and search for it, starting after the current position** : paste the contents of the clipboard, interpret it as search value number and jump to the first cell in the table, starting from the current position. 
- **Value info for row _x_ of _layer_**: active the value info for the cell with the focus.
- **Remove _layer_**: remove the column from the table.
- **Ramp Values**: ramp the values of a distribution, mainly relevant in classifications. This option is only available for not derived, numeric data items with more than one entry.


## tools

|tool|description|
|----|-----|
| ![](../assets/img/GUI/tb_save.bmp)| save to file as semicolon delimited text.|
| ![](../assets/img/GUI/tb_vcopy.bmp)| copy as semicolon delimited text to the clipboard.|
| ![](../assets/img/GUI/tb_copy.bmp)| copy the visible contents as image to the clipboard.|
| | |
| ![](../assets/img/GUI/tb_table_show_first_selected.bmp)| show the first selected row.|
| ![](../assets/img/GUI/tb_table_select_row.bmp)| select row(s) by mouse-click (use Shift to add or Ctrl to deselect).|
| ![](../assets/img/GUI/tb_select_all.bmp)| select all elements in the active layer.|
| ![](../assets/img/GUI/tb_select_none.bmp)| deselect all elements in the active layer.|
| ![](../assets/img/GUI/tb_show_selected_features.bmp)| show only selected elements.|
| | |
| ![](../assets/img/GUI/groupby.png)| groupby the hightlighted columns.|
