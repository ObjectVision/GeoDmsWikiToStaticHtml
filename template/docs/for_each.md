---
title: for_each
layout: default
nav_exclude: true
---
*[metascript-functions](metascript-functions) for_each*

## syntax

- for_each_n[e][i][t][d[n]v[n]|x[n]][l][d][a[t]][s][c][u]

_Starting from 7.163 the for_each function is in a process of being substituted by the [for_each_ind](for_each_ind) function, more variants of the for_each function group will become obsolete with the new GeoDMS versions._

## definition

The for_each group represents a family of functions, used to **generate a set of [tree-item](tree-item)** for each element of a [domain-unit](domain-unit).

The specific function name is dependent on the postfixes used in the for_each function name.

The possible names for the specific function are derived from the following notation:<BR>
for_each_n[e|t][d[n]v[n]][l][d][a[t]][s][c][u].

In this notation the name characters within brackets are optional.

The | character indicates one of the two namecharacters split by this | character need to be selected.

The namecharacters specified need to match with the relevant postfixes.
They represent:

- **n**: **[tree-item-name](tree-item-name)** for each new item;
- **e**: **[expression](expression)** for each new item;
- **i**: **[integritycheck](integritycheck)** for each new item;
- **t**: **[template](template)** instantiated for each new item;
- **d**\[n\]: **domain unit** for each item, with optional a n for the name of the [container](container) where the domain units can be found, in case a set of different domain units are requested;
- **v**\[n\]: **[values-unit](values-unit)** for each item, with optional a n for the name of the container where the values units can be found, in case a set of different values units are requested;
- **x**\[n\]: **[value-type](value-type)** for the creating [unit](unit).
- **l**: **label** [property](property) for each new item;
- **d**: **description** property for each new item;
- **a**: **[storagename](storagename)** for each new item, with an optional t for the storage type;
- **s**: **[sqlstring](sqlstring)** for each new item.
- **c**: **[cdf](cdf)** for each new item(this property can since version 7.163 only be configured using the [for_each_ind](for_each_ind) function
- **u**: **url** property for each new item(this property can since version 7.163 only be configured using the for_each_ind function

## description

A for_each function is used to derive a set of new tree items, based on the occuring values of [data-item](data-item) in a domain unit.

Different data items of this same domain unit can be used to specify the name, label, description etc. for the new set of tree items.

A template is used if the new items also request [subitem](subitem). Often an expression is configured for the new items, in case for this expression elements from the origin domain unit are needed, the expression is usually [indirect-expression](indirect-expression).

If as domain unit a [parameter](parameter) is configured, a values unit is also obligatory and vice versa.

If a template is ONLY used to configure the domain unit and values unit for the resulting tree items, it is advised to use the domain unit and values unit [argument](argument) in stead of a template (as in the example).

The [attribute](attribute) used for naming the new items should contain values that are allowed as item names. If not, an error is generated. Use the [asitemname](asitemname) function if your item names do not meet this condition.




## be aware

The evaluation of a for_each is executed when the meta/scheme information is generated in the [geodms-gui](geodms-gui). If for this evaluation (large) primary files are read, this becomes times consuming. Expanding tree items in the treeview becomes slow. Therefor we advice to use the contents of large primary data file (or complex calculations) as little as possible in the arguments of a for_each function.   

## examples


### Example 1
```
container regions := for_each_nedvld(> 
       Relational/Region/Name                 // name
      ,'Relational/Region/NrInhabitants[rel]' // expression
      ,void                                   // domain unit
      ,uint32                                 // values unit
      ,Relational/Region/Label                // label
      ,Relational/Region/Descr                // description
   );
```

| Name         | rel | NrInhabitants | Label | Descr |
|--------------|----:|--------------:|-------|-------|
| NoordHolland | 0   | 550           |       |       |
| ZuidHolland  | 1   | 1025          |       |       |
| Utrecht      | 2   | 300           |       |       |
| NoordBrabant | 3   | 300           |       |       |
| Gelderland   | 4   | 0             |       |       |

*result: Container regions with a parameter for each province, with as value the NrInhabitants for this province. The name, expression, domain and values unit, label and description for these parameters are determined by the for_each_nedvld function.*

### Example 2
```
container FactorData := for_each_ndvnda( 
       MetaData/Factors/Name                      // name
      ,Geography/Albers1kmGrid                    // domain unit
      ,Units                                      // container with configuration of values units
      ,MetaData/Factors/ValuesUnit                // values units
      ,MetaData/Factors/Descr                     // description
      ,'%sourceDataProjDir%/'+FileName+'.tif'     // storage name
  );   
```

*result: container Factordata with an attribute for each factor. These factors are read from .tif storages. The name, domain and values unit, description, storagename and cdf for these attributes are determined by the for_each_ndvndacu function. The values units read from the data item: MetaData/Factors/ValuesUnit(fourth argument) need to be direct subitems of the Units(third argument) container.*

### Example 3
```
container RegionGrids := for_each_nedvn(
       UniqueRegionRefs/Values                             // name
      ,'JrcFactorData/' + URR/Values + '[domain/grid_rel]' // expression
      ,domain                                              // domain unit
      ,Geography/Regions                                   // container with configuration of values units
      ,UniqueRegionRefs/Values                             // values units
); 
```

*result: container RegionGrids with an attribute for each UniqueRegionRefs. The name, expression, domain and values unit for these attributes are determined by the for_each_nedvn function. The values units read from the data item: UniqueRegionRefs/Values(fifth argument) need to be direct subitems of the Geography/Regions(fourth argument) container.*


### Example 4
```
container Distmatrices_100m := for_each_nex(
    Matrix/name
   ,'Distmatrices/Impl_100m/' + Matrix/name + '/PotRange'
   ,spoint
);
```

### Example 5
```
container Read_Shapefiles := for_each_nxat(
    Classifications/Services/name
   ,uint32
   ,'%ProjDir%/Data/cor/'+ Corridor_name +'/src/' + Services/name +'_' + Corridor_name +'_bb_200km.shp'
   ,"gdal.vect"
);
```


### Example 6

If you write an expression in the IntegrityCheck, you can use 'this' to refer to itself. This is preferred. 

```
container ReadOpbrengsten_perOP  := 
	for_each_neidv(OP/name
		, 'ReadOpbrengsten_perOP_UNCHECKED/'+OP/name
		, '(all(IsNull(this)))'
		, AdminDomain
		, EUR
	);
```


### Example 7
In case the full for_each result needs to be written to the same storage, define StorageName and StorageType at the container level of the for_each statement:
```
container test :=
   for_each_nedv(
	info/names
	,'reference/' + info/names
	,reference
	,int32
   ), StorageName = "%LocalDataProjDir%/WLO/Y1980.csv", StorageType = "gdalwrite.vect";
```