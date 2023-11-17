<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: Gerät    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Allgemeine Beschreibung: **Ein Gerät (Hardware + Software + Firmware), das dazu bestimmt ist, eine bestimmte Aufgabe zu erfüllen (Erfassen der Umgebung, Auslösen usw.) **.    
Version: 0.0.8    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[*]`: Batteriestand des Geräts. Er muss gleich 1,0 sein, wenn die Batterie voll ist. 0,0, wenn die Batterie leer ist. -1 wenn vorübergehend nicht ermittelt werden kann  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturveränderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor: Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form dient. Teilweise durch SAREF definiert. HVAC : Heizungs-, Belüftungs- und Klimaanlagen (HVAC), die für ein angenehmes Raumklima sorgen. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensornetzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufzeichnen oder Abspielen von Multimedia-Inhalten wie Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category wird veraltet sein, stattdessen sollte deviceCategory verwendet werden, um Konflikte mit anderen aqttributes namens category zu vermeiden.  . Model: [https://schema.org/Text](https://schema.org/Text)- `configuration[array]`: Technische Konfiguration des Geräts. Bei diesem Attribut handelt es sich um ein Array von Eigenschaften und deren Werten, die Parameter erfassen, die mit der Konfiguration eines Geräts zu tun haben (Zeitüberschreitungen, Meldezeiträume usw.) und die derzeit nicht durch die in diesem Modell definierten Standardattribute abgedeckt sind  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `controlledAsset[array]`: Liste der von dem Gerät kontrollierten Anlagegüter (Gebäude, Objekt usw.)  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlledProperty[array]`: Alles, was von einem Sensor erfasst, gemessen oder kontrolliert werden kann. Enum:airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, motionActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateFirstUsed[date-time]`: Ein Zeitstempel, der angibt, wann das Gerät zum ersten Mal verwendet wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateInstalled[date-time]`: Ein Zeitstempel, der angibt, wann das Gerät installiert wurde (falls es installiert werden muss)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastCalibration[date-time]`: Ein Zeitstempel, der angibt, wann die letzte Kalibrierung des Geräts stattgefunden hat  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[date-time]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten an die Cloud gemeldet hat  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateManufactured[date-time]`: Ein Zeitstempel, der angibt, wann das Gerät hergestellt wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateObserved[date-time]`: Datum der vom Benutzer definierten beobachteten Einheit  - `depth[number]`: Standort dieses Geräts, dargestellt durch die Tiefe von einem Startpunkt aus. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Eine Beschreibung dieses Artikels  - `deviceCategory[array]`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturveränderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor: Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form dient. Teilweise durch SAREF definiert. HVAC : Heizungs-, Belüftungs- und Klimaanlagen (HVAC), die für ein angenehmes Raumklima sorgen. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensornetzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufzeichnen oder Abspielen von Multimedia-Inhalten wie Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category wird veraltet sein, stattdessen sollte deviceCategory verwendet werden, um Konflikte mit anderen aqttributes namens category zu vermeiden.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: Zustand dieses Geräts aus betrieblicher Sicht. Sein Wert kann herstellerabhängig sein  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction[string]`: Enum:'Einlass, Auslass, Eintritt, Austritt'. Ein Zeitstempel, der angibt, wann das Gerät installiert wurde (falls es installiert werden muss)  . Model: [ https://schema.org/DateTime]( https://schema.org/DateTime)- `distance[number]`: Standort dieses Geräts, dargestellt als Entfernung von einem Ausgangspunkt. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/Distance](https://schema.org/Distance)- `dstAware[boolean]`: Zeigt ein Gerät an, das die Sommerzeit kennt (True). Wenn dies der Fall ist, wird der Zeitstempel automatisch vom Gerät an die Sommerzeit angepasst. Ist dies nicht der Fall (False), muss die Zeitanpassung vom Benutzer vorgenommen werden.  - `firmwareVersion[string]`: Die Firmware-Version dieses Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: Die Hardware-Version dieses Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `ipAddress[array]`: Liste der IP-Adresse des Geräts. Es kann eine durch Kommata getrennte Liste von Werten sein, wenn das Gerät mehr als eine IP-Adresse hat  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `macAddress[string]`: Die MAC-Adresse des Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `mcc[string]`: Diese Eigenschaft identifiziert den Mobile Country Code  . Model: [https://schema.org/Text](https://schema.org/Text)- `mnc[string]`: Diese Eigenschaft identifiziert den Mobile Network Code (MNC) des Netzes, an das das Gerät angeschlossen ist. Der MNC wird in Kombination mit einem Mobile Country Code (MCC) (auch bekannt als "MCC/MNC-Tupel") verwendet, um einen Mobilfunkbetreiber/Carrier eindeutig zu identifizieren, der die öffentlichen GSM-, CDMA-, iDEN-, TETRA- und 3G/4G-Mobilfunknetze sowie einige Satellitenmobilfunknetze nutzt.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels  - `osVersion[string]`: Die Version des Host-Betriebssystems Gerät  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `provider[string]`: Der Anbieter des Geräts  . Model: [https://schema.org/provider](https://schema.org/provider)- `refDeviceModel[*]`: Modell des Geräts  - `relativePosition[string]`: Lage des Geräts in einem Koordinatensystem entsprechend seiner örtlichen Positionierung  - `rssi[number]`: Indikator für die Stärke des empfangenen Signals für ein drahtloses Gerät. Sie muss in dBm oder mW ausgedrückt werden; verwenden Sie Unitcode, um sie anzugeben.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `serialNumber[string]`: Die vom Hersteller vergebene Seriennummer  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `softwareVersion[string]`: Die Softwareversion dieses Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `supportedProtocol[array]`: Unterstützte(s) Protokoll(e) oder Netzwerk(e)  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `type[string]`: NGSI-Entitätstyp. Es muss Gerät sein  - `value[string]`: Ein beobachteter oder gemeldeter Wert. Bei Betätigungsgeräten ist es ein Attribut, das es einer steuernden Anwendung ermöglicht, die Betätigungseinstellung zu ändern. Zum Beispiel kann ein Schalter, der gerade _eingeschaltet_ ist, einen Wert "ein" vom Typ "Text" melden. Um den betreffenden Schalter umzuschalten, muss dieser Attributwert natürlich in 'aus' geändert werden.  . Model: [https://schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `controlledProperty`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Ein Gerät ist ein materieller Gegenstand, der eine gewisse Logik enthält und Daten erzeugt und/oder verbraucht. Es wird immer davon ausgegangen, dass ein Gerät in der Lage ist, elektronisch über ein Netz zu kommunizieren. Dieses Datenmodell wurde teilweise in Zusammenarbeit mit Mobilfunkbetreibern und der [GSMA] (https://www.gsma.com/iot/iot-big-data/) entwickelt. Dieses Datenmodell verwendet Konzepte aus der [SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf), die Teil der [ETSI](http://www.etsi.org) Standards ist.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Device:      
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    batteryLevel:      
      description: Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined      
      oneOf:      
        - maximum: 1      
          minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    category:      
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"      
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
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    configuration:      
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model'      
      items:      
        properties:      
          parameter:      
            type: string      
          value:      
            type: string      
        type: object      
      type: array      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    controlledAsset:      
      description: 'List of the asset(s) (building, object, etc.) controlled by the device'      
      items:      
        oneOf:      
          - format: uri      
            type: string      
          - anyOf:      
              - description: Identifier format of any NGSI entity      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
                x-ngsi:      
                  type: Property      
              - description: Identifier format of any NGSI entity      
                format: uri      
                type: string      
                x-ngsi:      
                  type: Property      
            description: Unique identifier of the entity      
            x-ngsi:      
              type: Property      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    controlledProperty:      
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''      
      items:      
        enum:      
          - airPollution      
          - atmosphericPressure      
          - averageVelocity      
          - batteryLife      
          - batterySupply      
          - cdom      
          - conductance      
          - conductivity      
          - depth      
          - eatingActivity      
          - electricityConsumption      
          - energy      
          - fillingLevel      
          - freeChlorine      
          - gasConsumption      
          - gateOpening      
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
          - trafficFlow      
          - tss      
          - turbidity      
          - uvLampIntensity      
          - uvOrganicLoad      
          - waterConsumption      
          - waterFlow      
          - waterLevel      
          - waterPollution      
          - weatherConditions      
          - weight      
          - windDirection      
          - windSpeed      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateFirstUsed:      
      description: A timestamp which denotes when the device was first used      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateInstalled:      
      description: A timestamp which denotes when the device was installed (if it requires installation)      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastCalibration:      
      description: A timestamp which denotes when the last calibration of the device happened      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastValueReported:      
      description: A timestamp which denotes the last time when the device successfully reported data to the cloud      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateManufactured:      
      description: A timestamp which denotes when the device was manufactured      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: Date of the observed entity defined by the user      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    depth:      
      description: 'Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/depth      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    deviceCategory:      
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"      
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
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    deviceState:      
      description: State of this device from an operational point of view. Its value can be vendor dependent      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    direction:      
      description: 'Enum:''Inlet, Outlet, Entry, Exit''. A timestamp which denotes when the device was installed (if it requires installation)'      
      enum:      
        - Inlet      
        - Outlet      
        - Entry      
        - Exit      
      type: string      
      x-ngsi:      
        model: ' https://schema.org/DateTime'      
        type: Property      
    distance:      
      description: 'Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Distance      
        type: Property      
    dstAware:      
      description: Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user      
      type: boolean      
      x-ngsi:      
        type: Property      
    firmwareVersion:      
      description: The firmware version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    hardwareVersion:      
      description: The hardware version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    ipAddress:      
      description: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address      
      items:      
        oneOf:      
          - format: ipv4      
          - format: ipv6      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    macAddress:      
      description: The MAC address of the device      
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    mcc:      
      description: This property identifies the Mobile Country Code      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    mnc:      
      description: 'This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a ''MCC / MNC tuple'') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    osVersion:      
      description: The version of the host operating system device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    provider:      
      description: The provider of the device      
      type: string      
      x-ngsi:      
        model: https://schema.org/provider      
        type: Property      
    refDeviceModel:      
      description: Model of the device      
      oneOf:      
        - format: uri      
          type: string      
        - anyOf:      
            - description: Identifier format of any NGSI entity      
              maxLength: 256      
              minLength: 1      
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
              type: string      
              x-ngsi:      
                type: Property      
            - description: Identifier format of any NGSI entity      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
          description: Unique identifier of the entity      
          x-ngsi:      
            type: Property      
      x-ngsi:      
        type: Relationship      
    relativePosition:      
      description: Location of this device in a coordinate system according to its local emplacement      
      type: string      
      x-ngsi:      
        type: Property      
    rssi:      
      description: 'Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out. '      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    serialNumber:      
      description: The serial number assigned by the manufacturer      
      type: string      
      x-ngsi:      
        model: https://schema.org/serialNumber      
        type: Property      
    softwareVersion:      
      description: The software version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    supportedProtocol:      
      description: Supported protocol(s) or networks      
      items:      
        enum:      
          - 3g      
          - bluetooth      
          - bluetooth LE      
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
      type: array      
      x-ngsi:      
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be Device      
      enum:      
        - Device      
      type: string      
      x-ngsi:      
        type: Property      
    value:      
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value ''on'' of type ''Text''. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to ''off'''      
      type: string      
      x-ngsi:      
        model: https://schema.org/QuantitativeValue      
        type: Property      
  required:      
    - id      
    - type      
    - controlledProperty      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/Device/schema.json      
  x-model-tags: ""      
  x-version: 0.0.8      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### Gerät NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Device im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "deviceCategory": [  
    "sensor"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "controlledAsset": [  
    "wastecontainer-Osuna-100"  
  ],  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "mcc": "214",  
  "mnc": "07",  
  "batteryLevel": 0.75,  
  "serialNumber": "9845A",  
  "refDeviceModel": "myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "deviceState": "ok",  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "owner": [  
    "http://person.org/leon"  
  ]  
}  
```  
</details>    
#### Gerät NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein Gerät im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "deviceCategory": {  
    "type": "StructuredValue",  
    "value": [  
      "sensor"  
    ]  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 0.75  
  },  
  "dateFirstUsed": {  
    "type": "DateTime",  
    "value": "2014-09-11T11:00:00Z"  
  },  
  "controlledAsset": {  
    "type": "StructuredValue",  
    "value": [  
      "wastecontainer-Osuna-100"  
    ]  
  },  
  "serialNumber": {  
    "type": "Text",  
    "value": "9845A"  
  },  
  "mcc": {  
    "type": "Text",  
    "value": "214"  
  },  
  "value": {  
    "type": "Text",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "refDeviceModel": {  
    "type": "Text",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Number",  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "type": "StructuredValue",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "mnc": {  
    "type": "Text",  
    "value": "07"  
  },  
  "ipAddress": {  
    "type": "StructuredValue",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "deviceState": {  
    "type": "Text",  
    "value": "ok"  
  }  
}  
```  
</details>    
#### Gerät NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Device im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": 0.75,  
  "deviceCategory": [  
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
  "depth": 3,  
  "deviceState": "ok",  
  "direction": "Outlet",  
  "distance": 20,  
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
  "value": "l%3D0.22%3Bt%3D21.2",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Gerät NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein Gerät im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": {  
    "type": "Property",  
    "value": 0.75  
  },  
  "deviceCategory": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld::wastecontainer-Osuna-100"  
    ]  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "dateFirstUsed": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2014-09-11T11:00:00Z"  
    }  
  },  
  "deviceState": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "ipAddress": {  
    "type": "Property",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "mcc": {  
    "type": "Property",  
    "value": "214"  
  },  
  "mnc": {  
    "type": "Property",  
    "value": "07"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Property",  
    "value": 0.86  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "9845A"  
  },  
  "value": {  
    "type": "Property",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
