---
title: full-discrete-alloc-script
layout: default
nav_exclude: true
---
*[allocation-functions](allocation-functions) full script example*

The discrete [allocation](https://github.com/ObjectVision/LandUseModelling/wiki/Allocation) is used to allocate [land use types](https://github.com/ObjectVision/LandUseModelling/wiki/Land-Use-Types) to [grid](grid) cells with the [allocation-functions](allocation-functions).

The example presents how to configure all [argument](argument) and the function itself.

## script


```cpp

container allocation
{
   unit<fpoint> TestCoords: Range = "[{300000, 0}, {625000, 280000})";
 
   unit<spoint> DomainGrid := 
      range(
         gridset(
             TestCoords
            ,point(  -500f, 500f,   TestCoords)
            ,point(625000f, 10000f, TestCoords)
           , sPoint
        ), point(0s, 0s), point(6s, 6s)
     )
     ,   DialogType = "Map";
   
   container source
   {
      unit<int32> EurM2: Range = "[0, 20)";

      unit <uint8> lu_type: nrofrows = 3
      {
         attribute<string>  Name:           ['Living', 'Working', 'Nature'];
         attribute<string>  PartioningName: ['Living', 'Working', 'Nature'];
         attribute<lu_type> partioning    := id(lu_type);
       }
       attribute<lu_type> landuse (DomainGrid):
       [
        2, 2, 2, 1, null, null,
        2, 2, 0, 0, null, 1,
        2, 0, 0, 1,    1, 1,
        2, 0, 0, 0,    1, 1,
        2, 0, 0, 1, null, 1,
        2, 2, 2, 2,    2, 2
       ];
       container Suitability
       {
          attribute<EurM2> Living (DomainGrid): 
          [
           1,  2,  5, 4,  3, -1,
           2,  5,  8, 9,  7, 3,
           4, 10, 12,13, 12, 6,
           5, 11, 13,14, 12, 6,
           4,  9,  9, 5,  3, 2,
           2,  2,  4, 3,  1, 1
          ];
          attribute<EurM2> Working (DomainGrid):
          [
           1, 1, 2, 3,  4, -6,
           2, 3, 4, 6,  8,  9,
           2, 4, 9,11, 12, 10,
           1, 3, 5, 9, 10,  6,
           2, 4, 5, 5,  3,  2,
           1, 1, 2, 1,  1,  1
          ];
          attribute<EurM2> Nature (DomainGrid):
          [
           3, 3, 3, 2, 2, -2,
           3, 3, 2, 2, 2, 2,
           3, 2, 1, 1, 1, 1,
           3, 2, 1, 1 ,1, 2,
           3, 3, 2, 1, 2, 2,
           3, 3, 3, 3, 3, 3
          ];
       }
       container regMaps
       {
          unit<uint8> p1: nrofrows = 1;
          unit<uint8> p2: nrofrows = 2;

          attribute<p1> p1Map (DomainGrid) := const(0, DomainGrid, p1);
          attribute<p2> p2Map (DomainGrid) := pointRow(id(DomainGrid)) < 4s 
             ? 0[p2] 
             : 1[p2];
       }
       container claim_sources
       {
          unit<float32> Meter := BaseUnit('m', float32);
          unit<float32> Ha    := 10000.0 * Meter * Meter; 

          container p1
          {
             attribute<Ha> Nature_min (regMaps/p1): [12];
             attribute<Ha> Nature_max (regMaps/p1): [20];
             attribute<Ha> Living_min (regMaps/p1): [5];
             attribute<Ha> Living_max (regMaps/p1): [9];
          }
          container p2
          {
             attribute<Ha> Working_min (regMaps/p2): [6,2];
             attribute<Ha> Working_max (regMaps/p2): [10,4];
          }
       }
       parameter<float32> nrHaPerCel := 1[claim_sources/Ha];
       container claims_min
       {
         attribute<uint32> Living  (regMaps/p1)  := uint32(claim_sources/p1/Living_min  / nrHaPerCel);
         attribute<uint32> Working (regMaps/p2)  := uint32(claim_sources/p2/Working_min / nrHaPerCel);
         attribute<uint32> Nature  (regMaps/p1)  := uint32(claim_sources/p1/Nature_min  / nrHaPerCel);
      }
      container claims_max
      {
         attribute<uint32> Living  (regMaps/p1)  := uint32(claim_sources/p1/Living_max  / nrHaPerCel);
         attribute<uint32> Working (regMaps/p2)  := uint32(claim_sources/p2/Working_max / nrHaPerCel);
         attribute<uint32> Nature  (regMaps/p1)  := uint32(claim_sources/p1/Nature_max  / nrHaPerCel);
      }
      container regionSets
      {
         attribute<regMaps/p1> Nature  (DomainGrid) := regMaps/p1Map;
         attribute<regMaps/p1> Living  (DomainGrid) := regMaps/p1Map;
         attribute<regMaps/p2> Working (DomainGrid) := regMaps/p2Map;
      }
      unit<uint16> AtomicRegions := overlay(lu_type/PartioningName, DomainGrid, regionSets);

      attribute<bool> InRegio (DomainGrid):
       [
        True, True, True, True, False, True,
        True, True, True, True, False, True,
        True, True, True, True, True,  True,
        True, True, True, True, True,  True,
        True, True, True, True, False, True,
        True, True, True, True, True,  True
       ];
       
       attribute <bool> FreeLand (DomainGrid) := InRegio;

       container Compacted
       {
          unit<uint32> ADomain := select_with_org_rel(FreeLand = True), label = "allocation domain";
 
         attribute<ADomain> BaseGrid (DomainGrid) := invert(ADomain/org_rel);
 
         container SuitabilityMaps
         {
            attribute<EurM2> Living  (ADomain) := source/Suitability/Living[ADomain/org_rel];
            attribute<EurM2> Working (ADomain) := source/Suitability/Working[ADomain/org_rel];
            attribute<EurM2> Nature  (ADomain) := source/Suitability/Nature[ADomain/org_rel];
         }
         attribute<AtomicRegions> AtomicRegionMap (ADomain) := AtomicRegions/UnionData[ADomain/org_rel];
      }
      parameter<EurM2> treshold := 0[EurM2];
      container FeasibleSolution;
  }
  container allocate_discrete := 
     discrete_alloc(
         source/lu_type/name
        ,source/Compacted/ADomain
        ,source/Compacted/SuitabilityMaps
        ,source/lu_type/partioning
        ,source/lu_type/PartioningName
        ,source/AtomicRegions
        ,source/Compacted/AtomicRegionMap
        ,source/claims_min
        ,source/claims_max
        ,source/treshold
        ,source/FeasibleSolution
        )
   {
     attribute<Source/lu_type> alloc (DomainGrid) := landuse[Source/Compacted/BaseGrid];
   }
}

```