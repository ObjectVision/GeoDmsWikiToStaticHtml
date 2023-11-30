---
title: tablechopper-(read-ascii-file)
layout: default
nav_exclude: true
---
*[configuration-examples](configuration-examples) TableChopper*

The TableChopper is a scriptblock using the [str-storagemanager](str-storagemanager) and a set of GeoDMS functions to  **read** data from a delimited 
[ascii-files](ascii-files).

Delimited ASCII_Files are often [csv](csv) files. The [gdal.vect](gdal.vect) [storagemanager](storagemanager) is advised to read these files, use the TableChopper for very large files or for files with other separators as comma or semicolon.

To write data to delimited ASCII Files, use the [tablecomposer-(write-ascii-file)](tablecomposer-(write-ascii-file)).

## example
<pre>
container TableChopper
{
   parameter&lt;string&gt;  filename := '%projdir%/data/TableChopper.csv';
   unit&lt;uint8&gt;        domain : nrofrows = 5;
   parameter&lt;string&gt;  fieldseparator := ';';

   parameter&lt;string&gt; filedata
   :   StorageType = "str"
   ,   StorageName = "=filename";

   parameter&lt;string&gt; headerline := readLines(filedata, void, 0);

   unit&lt;uint32&gt;field := Range(uint32, 0, strcount(headerline, fieldseparator) + 1)
   {
      attribute&lt;string&gt; name := ReadArray(headerline , field, string, 0);
   }
        
   attribute&lt;string&gt; bodylines (domain) := readLines(filedata, domain, headerline/ReadPos);

   container data := for_each_nedv(
          field/name
         ,'ReadElems(
             BodyLines
            ,string
           ,'+ MakeDefined(field/name[id(field)-1] + '/ReadPos','const(0, domain)')+'
         )'
         ,domain
         ,string
      );
}
</pre>
## explanation

- The *filename* [parameter](parameter) refers to the ASCII file being read.
- The uint8 configured [domain-unit](domain-unit) *domain* is used as domain_unit for the resulting attributes, in the example with a [cardinality](cardinality) of 5.
- The *fieldseparator* parameter configures the separator used in the ASCII file between the fields.

When the TableChopper is used as a template to read multiple files, these first three items are often used as [case-parameter](case-parameter).

- The *filedata* string parameter refers to all the data from the ASCII file. It is read with the Str StorageManager.
- The parameter *headerline* will read the first line from the filedata parameter.
- The domain unit *field* is configured with as [subitem](subitem) *name*. This name attribute contains the names of the fields read from the header of the ASCII file.
- The *bodylines* attribute will read the other (none header) lines from the filedata parameter.

The resulting data container will result in a subitem for each field. The bodylines attribute is split up in the separate values per field. The resulting [tree-item](tree-item) are all string attributes. Use conversion functions to convert the string values to desired [values-unit](values-unit) / [value-type](value-type).