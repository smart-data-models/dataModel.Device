/* (Beta) Export of data model Device of the subject dataModel.Device for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE direction_type AS ENUM ('Inlet', 'Outlet', 'Entry', 'Exit');CREATE TYPE Device_type AS ENUM ('Device');
CREATE TABLE Device (address json, alternateName text, areaServed text, batteryLevel json, category json, configuration json, controlledAsset json, controlledProperty json, dataProvider text, dateCreated timestamp, dateFirstUsed timestamp, dateInstalled timestamp, dateLastCalibration timestamp, dateLastValueReported timestamp, dateManufactured timestamp, dateModified timestamp, dateObserved timestamp, depth text, description text, deviceCategory json, deviceState text, direction direction_type, distance text, dstAware text, firmwareVersion text, hardwareVersion text, id text, ipAddress json, location json, macAddress text, mcc text, mnc text, name text, osVersion text, owner json, provider text, refDeviceModel text, relativePosition text, rssi text, seeAlso json, serialNumber text, softwareVersion text, source text, supportedProtocol json, type Device_type, value text);