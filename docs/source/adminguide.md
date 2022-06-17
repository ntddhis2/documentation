Administrator Guide
============================


About this project
-------------

The NTD DHIS2 database project seeks to develop a stand-alone national NTD database using DHIS2 software. This system is designed around the data elements and disaggregations required to complete annual drug donation reporting forms such as the Joint Reporting Form (treatments distributed for LF, Oncho, STH, and SCH), the Epidemiological Reporting Form (epidemiological surveys for LF, Oncho, STH, and SCH to determine baseline endemicity or update endemicity status), and the Trachoma Elimination Monitoring Form (both treatments and endemicity data). These forms can be found here:

Joint Application Package (JRSM, JRF, EPIRF) https://www.who.int/teams/control-of-neglected-tropical-diseases/preventive-chemotherapy/joint-application-package 

Trachoma Elimination Monitoring Form https://www.trachoma.org/zithromax-management-guide 

The NTD database is designed to be a downstream data store, where data will be collected and aggregated by other systems, such as global survey tools, HMIS, or national or partner systems. The NTD database is designed to import annual reporting forms, which are produced through processes outside of this system, and store those data in a central, nationally owned, database. The NTD database could be a resource for completing those forms if data collection and reporting systems and tools are integrated with the NTD database. In this guide we will discuss such integrations.


![NTD DHIS2 database to aggregate all NTD programmatic data](https://www.dropbox.com/s/xosw8210pn2fhyr/Full%20data%20flow.PNG)


Introduction
-------------

### Is the NTD DHIS2 database a good fit for your use case?

The NTD DHIS2 database is designed to help national programmes to implement a NTD database, at national level, which stores all programmatic data that are reported on annual reporting forms. These data can be augmented to include data which could be programmatically important but not captured on annual reporting forms. Examples of such data could be research data, entomology data, human resource and training data, and budget data. The addition of these data is outside of the scope of this document. For guidance, please see the DHIS2 fundamentals or other training on how to add new data elements and category combinations along with data entry forms.

The NTD DHIS2 database is a good fit for national programmes who want to have a single database, which is accessible at national, sub-national, and global levels, and can provide data visualizations of these data to encourage engagement and use. The NTD DHIS2 database is not meant to compete with national health management information systems (HMIS), which likely also uses DHIS2 software. Rather, the NTD DHIS2 database is designed to aggregate data from HMIS, survey, research, and other sources, into a single database.

```{note}
To learn more about the DHIS2 data model click [here](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-238/understanding-the-data-model/about-data-dimensions.html).
```

### Does the NTD DHIS2 database affect how I collect or report data?

It is unlikely that the NTD DHIS2 database affects how you collect or report data. The NTD DHIS2 database is integrated with a number of systems that will automatically pull data into the database without any changes to the existing workflow. For example, if you are conducting a Trachoma Impact Survey (TIS) using Tropical Data, these survey results will be automatically shared with the NTD DHIS2 database through system integration with Tropical Data. Another example is reporting numbers treated during an MDA. Numbers treated are reported in HMIS by the Health Information Technology Department. These treatment data will be automatically added to the NTD DHIS2 database through system integration with HMIS. If you have questions about who specific data are included in the NTD DHIS2 database, please contact the M&E Advisor at the FMOH.

Getting started
-------------

### Software

To get started you will need to have a DHIS2 database running on either your local computer or accessible from a central server. 
You will need the NTD DHIS2 database meta data [LINK], which defines the data elements and category combinations needed to store annual reporting form data.
You will need a list of administrative units and the admin hierarchy. These data will be matched against the data you import to satisfy the “where” dimension of DHIS2 databases.
You will need to add the following DHIS2 apps from the app store:
X
Y
Z
Additionally, WHO is working on metadata packages that might be another source for adding indicators to the NTD DHIS2 database. You can find a list of those metadata packages here: https://dhis2.org/who/ 


### Hosting

The NTD DHIS2 Database[^myref] for Ethiopia is currently hosted by BAO Systems[^myref2], a leading DHIS2 cloud hosting provider.  BAO Systems provides nightly backups of the database and server administration support for server upgrades and is managed through their management portal (see Figure 1 below). The monthly fees for this service are billed annually at  $144/month. The current service contract with BAO Systems expired on November 30th, 2020.  If necessary, moving this database to another cloud hosting provider or even an on-premise server within the FMOH is possible with the support of a DHIS2 server administrator.

[^myref]: https://ethiopia.integratedntddb.org/
[^myref2]: https://www.baosystems.com/ 

![Portal](/_static/bao.png)

### Data model

The NTD DHIS2 data model consists of 11 datasets


| Dataset Name | Description | Data Collection Period | Organization Unit Level |
| ----------- | ----------- | ----------- | ----------- |
| ESPEN Forecast| Impact Assessment forecasts and MDA forecasts at the district level populated from the ESPEN Portal.| Annual| Woreda|
| Implementation Partners| Implementation partners fro NTD, MDA and WASH| Annual| Woreda|
| Integrated NTD Reporting Form| The FMOH reporting form for tracking NTD across the 5 PC NTDs| Annual| Woreda|
| Integrated NTD Reporting Form (Pre 2018) | The FMOH reporting form for tracking NTD across the 5 PC NTDs used prior to 2018| Monthly| Woreda|
| Joint Reporting Form (JRF)| Treatment data across drug packages used for WHO reporting| Annual| Woreda|
| Joint Request for Select Medicines (JRSM)| Treatment planning across drug packaged used for WHO reporting| Annual| Woreda|
| LF Morbidity Management and Disability Prevention| Country level MMDP summary statistics for Lymphedema    and Hydrocele| Annual| Country|
| National Demographics| National annual projection percentages for population growth and presac/sac and adult population percentages| Annual| Country|
| Sanitation Microplanning| Sanitation microplanning data supported by UNICEF| Annual| Woreda|
| Trachoma Data| Survey statistics and Treatment data fro Trachoma used for IT reporting.| Annual| Woreda|
| Tropical Data| Survey statistics and Treatment data fro Trachoma used for IT reporting imported from Tropical Data| Annual| Woreda|


### User Roles

There are currently 4 types of users in the system including National Data Manager, Regional Data Manager. These roles for the NTD Database for DHIS2 are based on the recommendations for user management in a health system.


| Role| Tasks| Configuration| 
| ------- | ------- | ------- |
| National Data Manager| Review data across all regions <br/><br/> Use data analytics apps for analysis and reporting| Data capture and maintenance organization units in the user’s profile set to country level <br/><br/>User role in the user’s profile set to Data Manager <br/><br/>User group set to National Dashboard Users|
| Regional Data Manager| Review data across one region <br/><br/>Use data analytics apps for analysis and reporting| Data capture and maintenance organization units in the user’s profile set to a specific regional level <br/><br/> User role in the user’s profile set to Data Manager <br/><br/> User group set to **Regional Dashboard Users**|
| District Data Officer| Enters data across one region <br/><br/>Use data analytics apps for analysis and reporting| Data capture and maintenance organization units in the user’s profile set to district level <br/><br/> User role in the user’s profile set to **Data Entry Officer** |
| System Administrator| Edit Metadata <br/><br/> Add new users| Data capture and maintenance organization units in the user’s profile set to country level <br/><br/>User role in the user’s profile set to **Superuser**|


Metadata Download
-------------

There are two metadata packages to support the basic configuration offered in this the NTD Database


| Package Name |DHIS2 Version| Package Version| Metadata| Updated| 
| ------- | ------- | ------- | ------- | ------- |
| ESPEN Forecast|2.35.10 | V1.0| [Download Package](https://raw.githubusercontent.com/ntddhis2/ntddb-metadata/master/metadata.json)| 18 May 2022 |


Data Import
-------------

The NTD Database supports data import from several different data sources including Microsoft Excel, Tropical Data, ESPEN Portal, and NTD Deliever.

### Microsoft Excel
	
Using the [Data Import Wizard](https://apps.dhis2.org/app/190583b7-e39b-4e52-a1c9-c7641aeaa833) app, this annual JRF, EPIRF, JRSM, TEMF, and WASH Excel workbook can be imported directly into the database.


| File| Dataset/Program| Mapping Name| Example Import| 
| ------- | ------- | ------- | ------- |
| Joint Request Form | Joint Reporting Form| Joint Reporting Form| [JRF 2018 Import File.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/JRF%25202018%2520Import%2520File.csv&sa=D&source=editors&ust=1651510003066674&usg=AOvVaw16OJqOIz20XUoGg0q0fKOa)| 
| EPIRF| LF Morbidity management and disability prevention| EPIRF LF Morbidity - All Years| [EPIRF 2016 Import File.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/EPIRF%2520Aggregate%2520All%2520Years%2520Import%2520File.csv&sa=D&source=editors&ust=1651510003068158&usg=AOvVaw0Ys3dxEP4aHPPKTOkJ5ZDm) | 
| JRSM| Joint Request for Select Medicines| Joint Request for Select Medicines| [JRSM 2018 Import File.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/JRSM%25202018%2520Import%2520File.csv&sa=D&source=editors&ust=1651510003069473&usg=AOvVaw2Yx7s-tRW-jDKFLx80Cid-)| 
| TEMF| Trachoma Data| Trachoma Elimination Monitoring Form (TEMF)| [TEMF 2018 Import File.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/TEMF%25202018%2520Import%2520File.csv&sa=D&source=editors&ust=1651510003071112&usg=AOvVaw1NjtXQI9t26otZ-lvprZoP)| 
| Unicef Sanitation Microplanning| Sanitation Microplanning| Sanitary Microplanning at the Woreda Level| [unicef-wash-import-file.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/Excel/unicef-wash-import-file.csv&sa=D&source=editors&ust=1651510003073219&usg=AOvVaw1Gb4G95ngaN4Rp8hKuJtS7)| 
| STH| ESPEN STH EPI RF| STH Survey Import from ESPEN| [sth import for espen.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/sth%2520import%2520for%2520espen.csv&sa=D&source=editors&ust=1651510003074585&usg=AOvVaw0eVQZKSR15ABZjLYp5zRef)| 
| SCH| ESPEN SCH EPI RF| SCH Survey Import from ESPEN| [sch import for espen.csv](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/CSV/sch%2520import%2520for%2520espen.csv&sa=D&source=editors&ust=1651510003075789&usg=AOvVaw0uKQjdKIMgTPtdzTpGU0Oc)| 


1. If it’s not already, install the Data Import Prepare the import file. All imported data need to conform to the value type of each data element. For example, data elements defined as Integers should be whole numbers.
1. Create the Mapping. In DHIS2, navigate to the Data Import Wizard and select Aggregate from the menu and click on the appropriate mapping for the file type being imported.  When prompted for an import file,  sel
1. Review the import data and Import Summary screen and make corrections to the mapping or the data import file as needed.


![Data Import Screenshot](/_static/import1.png)

![The Second Data Import Screenshot](/_static/import2.png)


### Tropical Data

Tropical Data is an online database of Trachoma survey data started by the Global Trachoma Mapping Project (GTMP). The NTD DHIS2 database pulls data from Tropical Data. This process works by executing a script which exports data using the Tropical Data API and then transforms it into a file that can be imported. This script and its documentation can be found [here](https://www.google.com/url?q=https://github.com/ntddhis2/ntd-dhis2-notebooks/blob/master/Tropical%2520Data/Import%2520Tropical%2520Data.ipynb&sa=D&source=editors&ust=1651510003077434&usg=AOvVaw2m5M-xfeXii-rIRfx956l6) in NTD DHIS2 database code repository.

### WHO ESPEN Portal

The [ESPEN Portal](https://espen.afro.who.int/.) is an electronic platform designed to enable health ministries and stakeholders to share, and exchange subnational program data, in support of the NTD control and elimination goals. The Expanded Special Project for Elimination of Neglected Tropical Diseases (ESPEN) was established as a partnership between WHO Regional Office for Africa (AFRO), the Member States and NTD partners The NTD DHIS2 database pulls data from ESPEN Portal. This process works by executing a script which exports data using the ESPEN Portal API and then transforms it into a file that can be imported. This script and its documentation can be found [here](https://github.com/ntddhis2/ntd-dhis2-notebooks/tree/master/ESPEN%20Portal) in the NTD DHIS2 database code repository.

### NTDeliver

[NTDeliver](https://www.ntdeliver.com/about) is an online platform that centralizes and coordinates information from a variety of sources to better monitor and evaluate the NTD supply chain. The NTD DHIS2 database provides a view to the NTDeliver country summary report with a link provided on the Reports dashboard.

Questions
-------------
For questions on the DHIS2 for NTD, please post visit the [DHIS2 Community of Practice](https://community.dhis2.org/).


