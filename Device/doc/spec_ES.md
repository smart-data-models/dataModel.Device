Entidad: Dispositivo  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
Descripción global: **Un aparato (hardware + software + firmware) destinado a realizar una tarea particular (detectar el entorno, actuar, etc.).**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `batteryLevel`: Nivel de la batería del dispositivo. Debe ser igual a 1.0 cuando la batería está llena. 0,0 cuando la batería está vacía. -1 cuando no se puede determinar transitoriamente.  - `configuration`: La configuración técnica del dispositivo. Este atributo está destinado a ser un diccionario de propiedades que captan parámetros que tienen que ver con la configuración de un dispositivo (tiempos de espera, períodos de reporte, etc.) y que no están actualmente cubiertos por los atributos estándar definidos por este modelo.  - `controlledAsset`: Lista de los bienes (edificio, objeto, etc.) controlados por el dispositivo.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateFirstUsed`: Una marca de tiempo que denota cuando el dispositivo fue usado por primera vez.  - `dateInstalled`: Un sello de tiempo que denota cuando el dispositivo fue instalado (si requiere instalación).  - `dateLastCalibration`: Una marca de tiempo que denota cuándo fue la última calibración del dispositivo.  - `dateLastValueReported`:   - `dateManufactured`: Un sello de tiempo que denota cuando el dispositivo fue fabricado.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `depth`: La ubicación de este dispositivo representada por una profundidad desde un punto de partida. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html)  - `description`: Una descripción de este artículo  - `deviceState`: Estado de este dispositivo desde el punto de vista operacional. Su valor puede depender del proveedor.  - `direction`: Enum:'Entrada, Salida, Entrada, Salida'. Una marca de tiempo que denota cuándo se instaló el dispositivo (si requiere instalación).  - `distance`: La ubicación de este dispositivo representada por una distancia desde un punto de partida. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html)  - `dstAware`: Indica un dispositivo que es consciente del horario de verano (Verdadero). En caso de que lo sea, el dispositivo ajusta automáticamente la marca de tiempo para reflejar los cambios de DST. Si no es así (Falso) los ajustes de tiempo deben ser atendidos por el usuario.  - `firmwareVersion`: La versión de firmware de este dispositivo.  - `hardwareVersion`: La versión de hardware de este dispositivo.  - `id`: Identificador único de la entidad  - `ipAddress`: Lista de la dirección IP del dispositivo. Puede ser una lista de valores separada por comas si el dispositivo tiene más de una dirección IP.  - `location`:   - `macAddress`: La dirección MAC del dispositivo  - `mnc`: Esta propiedad identifica el Código de Red Móvil (MNC) de la red a la que está conectado el dispositivo. El MNC se utiliza en combinación con un Indicativo de País para Móvil (MCC) (también conocido como 'MCC / MNC tuple') para identificar de forma exclusiva a un operador de telefonía móvil / portador que utiliza las redes móviles terrestres públicas GSM, CDMA, iDEN, TETRA y 3G / 4G y algunas redes móviles por satélite.  - `name`: El nombre de este artículo.  - `osVersion`: La versión del dispositivo del sistema operativo anfitrión.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `provider`: El proveedor del dispositivo.  - `refDeviceModel`: Modelo del dispositivo  - `relativePosition`: Ubicación de este dispositivo en un sistema de coordenadas de acuerdo a su ubicación local.  - `rssi`: Indicador de intensidad de la señal recibida para un dispositivo habilitado para la tecnología inalámbrica. Debe ser expresada en dBm o mW, use el código de unidad para establecerlo.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `serialNumber`: El número de serie asignado por el fabricante.  - `softwareVersion`: La versión de software de este dispositivo.  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Oroperty. Tipo de entidad NGSI. Tiene que ser un dispositivo  - `value`: Un valor observado o comunicado. En el caso de los dispositivos de accionamiento, es un atributo que permite a una aplicación de control cambiar el ajuste de accionamiento. Por ejemplo, un dispositivo de interruptor que está actualmente _on_ puede reportar un valor "on" de tipo "Texto". Obviamente, para conmutar el interruptor referido, este valor de atributo tendrá que ser cambiado a "off".    
Propiedades requeridas  
- `category`  - `controlledProperty`  - `id`  - `type`    
Un dispositivo es un objeto tangible que contiene cierta lógica y es productor y/o consumidor de datos. Se supone siempre que un dispositivo es capaz de comunicarse electrónicamente a través de una red. Este modelo de datos se ha desarrollado parcialmente en cooperación con los operadores de telefonía móvil y la [GSMA] (https://www.gsma.com/iot/iot-big-data/). Este modelo de datos reutiliza conceptos procedentes de la parte de la [Ontología SAREF](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) de las normas del [ETSI](http://www.etsi.org).  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    batteryLevel:    
      description: 'Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery ìs empty. -1 when transiently cannot be determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    configuration:    
      description: 'Device''s technical configuration. This attribute is intended to be a dictionary of properties which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
    controlledAsset:    
      description: 'List of the asset(s) (building, object, etc.) controlled by the device.'    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: &device_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFirstUsed:    
      description: 'A timestamp which denotes when the device was first used.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateInstalled:    
      description: 'A timestamp which denotes when the device was installed (if it requires installation).'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastCalibration:    
      description: 'A timestamp which denotes when the last calibration of the device happened.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastValueReported:    
      description: ""    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: 'https://schema.org/DateTime.A timestamp which denotes the last time when the device successfully reported data to the cloud..'    
    dateManufactured:    
      description: 'A timestamp which denotes when the device was manufactured.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      description: 'Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
    description:    
      description: 'A description of this item'    
      type: Property    
    deviceState:    
      description: 'State of this device from an operational point of view. Its value can be vendor dependent.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    direction:    
      description: 'Enum:''Inlet, Outlet, Entry, Exit''. A timestamp which denotes when the device was installed (if it requires installation).'    
      enum:    
        - Inlet    
        - Outlet    
        - Entry    
        - Exit    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/DateTime'    
    distance:    
      description: 'Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Distance    
    dstAware:    
      description: 'Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user.'    
      type: Property    
    firmwareVersion:    
      description: 'The firmware version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hardwareVersion:    
      description: 'The hardware version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: *device_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    ipAddress:    
      description: 'List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address.'    
      items:    
        oneOf:    
          - format: ipv4    
          - format: ipv6    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    macAddress:    
      description: 'The MAC address of the device'    
      items:    
        pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    mnc:    
      description: 'This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a ''MCC / MNC tuple'') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    osVersion:    
      description: 'The version of the host operating system device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *device_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    provider:    
      description: 'The provider of the device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/provider    
    refDeviceModel:    
      description: 'Model of the device'    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *device_-_properties_-_id_-_anyof    
          description: 'Property. Unique identifier of the entity'    
      type: Relationship    
    relativePosition:    
      description: 'Location of this device in a coordinate system according to its local emplacement.'    
      type: Property    
    rssi:    
      description: 'Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out. '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/serialNumber    
    softwareVersion:    
      description: 'The software version of this device.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'Oroperty. NGSI Entity type. It has to be Device'    
      enum:    
        - Device    
      type: string    
    value:    
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value `on`of type `Text`. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to `off`.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/QuantitativeValue    
  required:    
    - id    
    - type    
    - category    
    - controlledProperty    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Dispositivo NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un dispositivo en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": ["sensor"],  
  "controlledProperty": ["fillingLevel", "temperature"],  
  "controlledAsset": ["wastecontainer-Osuna-100"],  
  "ipAddress": ["192.14.56.78"],  
  "mcc": "214",  
  "mnc": "07",  
  "batteryLevel": 0.75,  
  "serialNumber": "9845A",  
  "refDeviceModel": "myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "deviceState": "ok",  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "owner": ["http://person.org/leon"]  
}  
```  
#### Dispositivo NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un dispositivo en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": {  
    "value": ["sensor"]  
  },  
  "batteryLevel": {  
    "value": 0.75  
  },  
  "dateFirstUsed": {  
    "type": "DateTime",  
    "value": "2014-09-11T11:00:00Z"  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "value": ["wastecontainer-Osuna-100"]  
  },  
  "serialNumber": {  
    "value": "9845A"  
  },  
  "mcc": {  
    "value": "214"  
  },  
  "value": {  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "value": ["fillingLevel", "temperature"]  
  },  
  "owner": {  
    "value": ["http://person.org/leon"]  
  },  
  "mnc": {  
    "value": "07"  
  },  
  "ipAddress": {  
    "value": ["192.14.56.78"]  
  },  
  "deviceState": {  
    "value": "ok"  
  }  
}  
```  
#### Dispositivo NGSI-LD claves-valores Ejemplo  
Aquí hay un ejemplo de un dispositivo en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "batteryLevel": 0.75,  
 "category": ["sensor"],  
 "controlledAsset": ["urn:ngsi-ld::wastecontainer-Osuna-100"],  
 "controlledProperty": ["fillingLevel", "temperature"],  
 "dateFirstUsed": {"@type": "DateTime", "@value": "2014-09-11T11:00:00Z"},  
 "deviceState": "ok",  
 "id": "urn:ngsi-ld:Device:device-9845A",  
 "ipAddress": ["192.14.56.78"],  
 "mcc": "214",  
 "mnc": "07",  
 "owner": ["http://person.org/leon"],  
 "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
 "rssi": 0.86,  
 "serialNumber": "9845A",  
 "type": "Device",  
 "value": "l%3D0.22%3Bt%3D21.2"}  
```  
#### Dispositivo NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un dispositivo en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Device:device-9845A",  
    "type": "Device",  
    "category": {  
        "type": "Property",  
        "value": [  
            "sensor"  
        ]  
    },  
    "batteryLevel": {  
        "type": "Property",  
        "value": 0.75  
    },  
    "dateFirstUsed": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2014-09-11T11:00:00Z"  
        }  
    },  
    "controlledAsset": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld::wastecontainer-Osuna-100"  
        ]  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "9845A"  
    },  
    "mcc": {  
        "type": "Property",  
        "value": "214"  
    },  
    "value": {  
        "type": "Property",  
        "value": "l%3D0.22%3Bt%3D21.2"  
    },  
    "refDeviceModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345"  
    },  
    "rssi": {  
        "type": "Property",  
        "value": 0.86  
    },  
    "controlledProperty": {  
        "type": "Property",  
        "value": [  
            "fillingLevel",  
            "temperature"  
        ]  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "http://person.org/leon"  
        ]  
    },  
    "mnc": {  
        "type": "Property",  
        "value": "07"  
    },  
    "ipAddress": {  
        "type": "Property",  
        "value": [  
            "192.14.56.78"  
        ]  
    },  
    "deviceState": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "distance": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "MTR"  
    },  
    "depth": {  
        "type": "Property",  
        "value": 3,  
        "unitCode": "MTR"  
    },  
    "direction": {  
        "type": "Property",  
        "value": "Outlet"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
