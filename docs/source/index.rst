Administrator Guide
===================================

What is the NTD DHIS2 database?
------------

The NTD DHIS2 database is a national NTD database that can be accessed by authorized Ministry of Health users and Partners by going to https://ethiopia.integratedntddb.org/. The NTD DHIS2 database uses DHIS2 (https://www.dhis2.org/) software as a data warehouse that integrates with external systems to provide one single source for all NTD programmatic data (Image 1). Under this model, no data is entered into the NTD DHIS2 database directly, rather, the data come from integrations with a wide range of external systems. Such as:

* Epidemiological surveys - Tropical Data, ESPEN Collect, EPHI
* MDA Treatments - HMIS indicators
* Stock - PFSA?
* Morbidity management - HMIS indicators
* Drug procurement tracking - NTDeliver
* WASH - mWater


NTD DHIS2 database vs HMIS?
------------

The national Health Management Information System (HMIS) is a data collection system designed to collect key health indicators from health facilities across the country on a wide range of health conditionals in order to support planning, management, and decision-making.

The NTD DHIS2 database is a data warehouse that connects to a wide range of external databases to create a single data repository of all NTD programmatic data in Ethiopia. Some data, such as the routine reporting of MDA treatments and morbidity management come through HMIS facility-based reporting. Other data, such as the event data associated with epidemiological surveys, comes through integration with global systems, such as Tropical Data, or through national systems, such as electronic data collection tools implemented by the Ethiopia Public Health Institute (EPHI). Altogether, these NTD data allow the NTD program to plan, manage, and report on NTD control and elimination programming.


Getting started
------------

Hosting
~~~~~~~~~~~~~

The NTD DHIS2 Database[1] for Ethiopia is currently hosted by BAO Systems[2], a leading DHIS2 cloud hosting provider.  BAO Systems provides nightly backups of the database and server administration support for server upgrades and is managed through their management portal (see Figure 1 below). The monthly fees for this service are billed annually at  $144/month. The current service contract with BAO Systems expired on November 30th, 2020.  If necessary, moving this database to another cloud hosting provider or even an on-premise server within the FMOH is possible with the support of a DHIS2 server administrator.