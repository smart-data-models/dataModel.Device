/* (Beta) Export of data model Modbus of the subject dataModel.Device for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Modbus_primaryTable_type AS ENUM ('coil', 'inputRegister', 'holdingRegister', 'discreteInput');
CREATE TYPE Modbus_type AS ENUM ('Modbus');
CREATE TABLE Modbus (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "memoryAddress" TEXT,
  "name" TEXT,
  "owner" JSON,
  "primaryTable" Modbus_primaryTable_type,
  "protocolId" TEXT,
  "seeAlso" JSON,
  "source" TEXT,
  "transactionId" TEXT,
  "type" Modbus_type,
  "unitId" TEXT,
  "value" TEXT
);