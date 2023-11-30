---
title: postgis
layout: default
nav_exclude: true
---
## Database: PostgreSQL/PostGIS

Data can be read from [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) databases with the [gdal.vect](gdal.vect)  [storagemanager](storagemanager). 
The [PostGIS](https://en.wikipedia.org/wiki/PostGIS) extension need to be installed to read vector data.

Example:

<pre>
container PostGreSQL
 :  StorageName = "PG:host='localhost' port='5432' user='dms' password='dms' dbname='geo'"
 ,  StorageType = "gdal.vect"
 {
    container administrative
    {
        unit&lt;uint32&gt; municipality: SqlString = "SELECT geom, name FROM cbs.munic ORDER BY code"
        {
            attribute&lt;point_rd&gt; geom (polygon);
            attribute&lt;string&gt;   name;
        }        
    }
}
</pre>

The database geo is configured to the container PostgresSQL. The [storagename](storagename) must configure the parameters: host, port, user, password and dbname.

Within a subcontainer administrative, a [domain-unit](domain-unit) is configured called municipality.

The [attribute](attribute) geom (the [feature-attribute](feature-attribute) with the polygon geometry) and the name of the municipality are read from the database.

In the [sqlstring](sqlstring) property the fields geom and name are selected. Their source name in the database (FROM clause) is cbs.munic in which cbs indicates the scheme name and munic the table name in the scheme. The ORDER BY clause guarantees all municipalities are always read in the same sequence (ordered by code) from the database.