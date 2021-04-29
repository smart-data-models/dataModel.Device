Entität: Gerät  
==============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
Globale Beschreibung: **Ein Gerät (Hardware + Software + Firmware), das dazu bestimmt ist, eine bestimmte Aufgabe zu erfüllen (Erfassen der Umgebung, Auslösen usw.).**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `batteryLevel`: Stand der Gerätebatterie. Er muss gleich 1,0 sein, wenn die Batterie voll ist. 0,0, wenn die Batterie leer ist. -1, wenn vorübergehend nicht ermittelt werden kann.  - `category`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturänderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor.  
Aktor : Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator.  
Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form gebaut ist. Teilweise durch SAREF definiert. HVAC : Gerät für Heizung, Lüftung und Klimatisierung (HVAC), das für ein angenehmes Raumklima sorgt. https://w3id.org/saref#HVAC.  
Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensor-Netzwerk. (https://w3id.org/saref#Network.  
Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufnehmen oder Abspielen von Multimedia-Inhalten wie z. B. Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'  - `configuration`: Technische Konfiguration des Geräts. Bei diesem Attribut handelt es sich um ein Array von Eigenschaften und deren Werten, die Parameter erfassen, die mit der Konfiguration eines Gerätes zu tun haben (Timeouts, Meldezeiträume usw.) und die derzeit nicht durch die von diesem Modell definierten Standardattribute abgedeckt sind.  - `controlledAsset`: Liste der Kühlstelle(n) (Gebäude, Objekt usw.), die vom Gerät gesteuert werden.  - `controlledProperty`: Alles, was von einem Sensor erfasst, gemessen oder gesteuert werden kann. Enum:'airPollution, atmosphericPressure, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, gasComsumption, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, tss, turbidity, waterConsumption, waterPollution, weatherConditions, weight, windDirection, windSpeed'  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateFirstUsed`: Ein Zeitstempel, der angibt, wann das Gerät zum ersten Mal verwendet wurde.  - `dateInstalled`: Ein Zeitstempel, der angibt, wann das Gerät installiert wurde (wenn es eine Installation erfordert).  - `dateLastCalibration`: Ein Zeitstempel, der angibt, wann die letzte Kalibrierung des Geräts stattgefunden hat.  - `dateLastValueReported`:   - `dateManufactured`: Ein Zeitstempel, der angibt, wann das Gerät hergestellt wurde.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `depth`: Standort dieses Geräts, dargestellt durch eine Tiefe von einem Startpunkt aus. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html) Code akzeptiert  - `description`: Eine Beschreibung dieses Artikels  - `deviceState`: Zustand dieses Geräts aus betrieblicher Sicht. Sein Wert kann herstellerabhängig sein.  - `direction`: Enum:'Inlet, Outlet, Entry, Exit'. Ein Zeitstempel, der angibt, wann das Gerät installiert wurde (wenn es eine Installation erfordert).  - `distance`: Standort dieses Geräts, dargestellt durch eine Entfernung von einem Startpunkt. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html) Code akzeptiert  - `dstAware`: Zeigt ein Gerät an, das Sommerzeit-bewusst ist (True). Wenn dies der Fall ist, wird der Zeitstempel automatisch vom Gerät an die Sommerzeitänderungen angepasst. Wenn nicht (False), muss die Zeitanpassung vom Benutzer vorgenommen werden.  - `firmwareVersion`: Die Firmware-Version dieses Geräts.  - `hardwareVersion`: Die Hardware-Version dieses Geräts.  - `id`: Eindeutiger Bezeichner der Entität  - `ipAddress`: Liste der IP-Adresse des Geräts. Es kann eine kommagetrennte Liste von Werten sein, wenn das Gerät mehr als eine IP-Adresse hat.  - `location`:   - `macAddress`: Die MAC-Adresse des Geräts  - `mnc`: Diese Eigenschaft identifiziert den Mobile Network Code (MNC) des Netzes, mit dem das Gerät verbunden ist. Der MNC wird in Kombination mit einem Mobile Country Code (MCC) (auch als 'MCC / MNC-Tupel' bezeichnet) verwendet, um einen Mobilfunkbetreiber/Carrier eindeutig zu identifizieren, der die öffentlichen GSM-, CDMA-, iDEN-, TETRA- und 3G / 4G-Mobilfunknetze sowie einige Satellitenmobilfunknetze verwendet.  - `name`: Der Name dieses Elements.  - `osVersion`: Die Version des Host-Betriebssystems Gerät.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `provider`: Der Anbieter des Geräts.  - `refDeviceModel`: Modell des Geräts  - `relativePosition`: Lage dieses Geräts in einem Koordinatensystem entsprechend seiner lokalen Platzierung.  - `rssi`: Indikator für die empfangene Signalstärke für ein drahtloses Gerät. Sie muss in dBm oder mW ausgedrückt werden, verwenden Sie Unitcode, um sie einzustellen.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `serialNumber`: Die vom Hersteller vergebene Seriennummer.  - `softwareVersion`: Die Softwareversion dieses Geräts.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `supportedProtocol`: Unterstützte(s) Protokoll(e) oder Netzwerk(e)  - `type`: NGSI Entity-Typ. Es muss Gerät sein  - `value`: Ein beobachteter oder gemeldeter Wert. Bei Aktorgeräten ist es ein Attribut, das es einer steuernden Anwendung ermöglicht, die Betätigungseinstellung zu ändern. So kann z. B. ein Schaltgerät, das gerade _on_ ist, einen Wert 'on' vom Typ 'Text' melden. Um den betreffenden Schalter umzuschalten, muss dieser Attributwert natürlich auf 'aus' geändert werden.    
Erforderliche Eigenschaften  
- `category`  - `controlledProperty`  - `id`  - `type`    
Ein Device ist ein greifbares Objekt, das eine gewisse Logik enthält und Produzent und/oder Konsument von Daten ist. Es wird immer davon ausgegangen, dass ein Device in der Lage ist, elektronisch über ein Netzwerk zu kommunizieren. Dieses Datenmodell wurde teilweise in Zusammenarbeit mit Mobilfunkbetreibern und der [GSMA](https://www.gsma.com/iot/iot-big-data/) entwickelt. Dieses Datenmodell verwendet Konzepte wieder, die aus dem [SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) Teil der [ETSI](http://www.etsi.org) Standards stammen.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    batteryLevel:    
      description: 'Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. \nactuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. \nMeter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. \nNetwork : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. \nMultimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
      items:    
        enum:    
          - actuator    
          - beacon    
          - endgun    
          - HVAC    
          - implement    
          - irrSection    
          - irrSystem    
          - meter    
          - multimedia    
          - network    
          - sensor    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    configuration:    
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model.'    
      items:    
        properties:    
          parameter:    
            type: string    
          value:    
            type: string    
        type: object    
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
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, gasComsumption, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, tss, turbidity, waterConsumption, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        enum:    
          - airPollution    
          - atmosphericPressure    
          - cdom    
          - conductance    
          - conductivity    
          - depth    
          - eatingActivity    
          - electricityConsumption    
          - energy    
          - fillingLevel    
          - gasComsumption    
          - heading    
          - humidity    
          - light    
          - location    
          - milking    
          - motion    
          - movementActivity    
          - noiseLevel    
          - occupancy    
          - orp    
          - pH    
          - power    
          - precipitation    
          - pressure    
          - refractiveIndex    
          - salinity    
          - smoke    
          - soilMoisture    
          - solarRadiation    
          - speed    
          - tds    
          - temperature    
          - tss    
          - turbidity    
          - waterConsumption    
          - waterPollution    
          - weatherConditions    
          - weight    
          - windDirection    
          - windSpeed    
        type: string    
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
        description: 'Property. Model:''https://schema.org/Text''. The MAC address of the device.'    
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
    supportedProtocol:    
      description: 'Supported protocol(s) or networks'    
      items:    
        enum:    
          - 3g    
          - bluetooth    
          - 'bluetooth LE'    
          - cat-m    
          - coap    
          - ec-gsm-iot    
          - gprs    
          - http    
          - lwm2m    
          - lora    
          - lte-m    
          - mqtt    
          - nb-iot    
          - onem2m    
          - sigfox    
          - ul20    
          - websocket    
        type: string    
      type: Property    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
    type:    
      description: 'NGSI Entity type. It has to be Device'    
      enum:    
        - Device    
      type: Property    
    value:    
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value ''on'' of type ''Text''. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to ''off''.'    
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
## Beispiel-Nutzlasten  
#### Gerät NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Device im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Gerät NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Gerät im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### Gerät NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Device im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Gerät NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Gerät im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "batteryLevel": 0.75,  
  "category": [  
    "sensor"  
  ],  
  "controlledAsset": [  
    "urn:ngsi-ld::wastecontainer-Osuna-100"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "deviceState": "ok",  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "mcc": "214",  
  "mnc": "07",  
  "owner": [  
    "http://person.org/leon"  
  ],  
  "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "serialNumber": "9845A",  
  "type": "Device",  
  "value": "l%3D0.22%3Bt%3D21.2"  
}  
```  
