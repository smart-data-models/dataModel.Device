<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Dispositif  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un appareil (matériel + logiciel + micrologiciel) destiné à accomplir une tâche particulière (détection de l'environnement, actionnement, etc.).  
version : 0.0.9  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[*]`: Niveau de la batterie de l'appareil. Il doit être égal à 1,0 lorsque la batterie est pleine. 0,0 lorsque la batterie est vide. -1 lorsqu'il n'est pas possible de déterminer le niveau de la batterie de manière transitoire  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Capteur : Dispositif qui détecte et réagit à des événements ou à des changements dans l'environnement physique, tels que la lumière, le mouvement ou les changements de température. https://w3id.org/saref#Sensor. Actionneur : Dispositif chargé de déplacer ou de contrôler un mécanisme ou un système. https://w3id.org/saref#Actuator. Compteur : Dispositif construit pour détecter et afficher avec précision une quantité sous une forme lisible par un être humain. Partiellement défini par SAREF. CVC : Appareil de chauffage, de ventilation et de climatisation (CVC) qui assure le confort de l'environnement intérieur. https://w3id.org/saref#HVAC. Réseau : Dispositif utilisé pour connecter d'autres dispositifs dans un réseau, tel qu'un concentrateur, un commutateur ou un routeur dans un réseau local ou un réseau de capteurs. (https://w3id.org/saref#Network. Multimédia : Un appareil conçu pour afficher, stocker, enregistrer ou lire des contenus multimédias tels que de l'audio, des images, des animations, de la vidéo. Enum : "actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor". Raw category sera déprécié, utilisez deviceCategory à la place pour éviter les conflits avec d'autres aqttributes nommés category.  . Model: [https://schema.org/Text](https://schema.org/Text)- `configuration[array]`: Configuration technique de l'appareil. Cet attribut est destiné à être un tableau de propriétés et de valeurs qui saisissent des paramètres liés à la configuration d'un appareil (délais, périodes de rapport, etc.) et qui ne sont pas actuellement couverts par les attributs standard définis par le présent modèle.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `controlledAsset[array]`: Liste des biens (bâtiment, objet, etc.) contrôlés par le dispositif  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlledProperty[array]`: Tout ce qui peut être détecté, mesuré ou contrôlé. Enum :'pollution de l'air, pression atmosphérique, vitesse moyenne, autonomie de la batterie, alimentation de la batterie, cdom, conductance, conductivité, profondeur, activité alimentaire, consommation d'électricité, énergie, niveau de remplissage, chlore libre, consommation de gaz, ouverture de la porte, cap, humidité, lumière, emplacement, traite, mouvement, activité de mouvement, niveau de bruit, occupation, orp, pH, puissance, précipitation, pression, indice de réfraction, salinité, fumée, humidité du sol, rayonnement solaire, vitesse, tds, température, flux de circulation, tss, turbidité, consommation d'eau, flux d'eau, niveau d'eau, pollution de l'eau, conditions météorologiques, poids, direction du vent, vitesse du vent".  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateFirstUsed[date-time]`: Un horodatage indiquant la date de la première utilisation de l'appareil.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateInstalled[date-time]`: Un horodatage qui indique quand le dispositif a été installé (s'il nécessite une installation).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastCalibration[date-time]`: Un horodatage qui indique la date du dernier étalonnage de l'appareil.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[date-time]`: Un horodatage qui indique la dernière fois que l'appareil a transmis avec succès des données au nuage.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateManufactured[date-time]`: Un horodatage indiquant la date de fabrication de l'appareil.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateObserved[date-time]`: Date de l'entité observée définie par l'utilisateur  - `depth[number]`: Emplacement de ce dispositif représenté par une profondeur à partir d'un point de départ. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: Une description de l'article  - `deviceCategory[array]`: Capteur : Dispositif qui détecte et réagit à des événements ou à des changements dans l'environnement physique, tels que la lumière, le mouvement ou les changements de température. https://w3id.org/saref#Sensor. Actionneur : Dispositif chargé de déplacer ou de contrôler un mécanisme ou un système. https://w3id.org/saref#Actuator. Compteur : Dispositif construit pour détecter et afficher avec précision une quantité sous une forme lisible par un être humain. Partiellement défini par SAREF. CVC : Appareil de chauffage, de ventilation et de climatisation (CVC) qui assure le confort de l'environnement intérieur. https://w3id.org/saref#HVAC. Réseau : Dispositif utilisé pour connecter d'autres dispositifs dans un réseau, tel qu'un concentrateur, un commutateur ou un routeur dans un réseau local ou un réseau de capteurs. (https://w3id.org/saref#Network. Multimédia : Un appareil conçu pour afficher, stocker, enregistrer ou lire des contenus multimédias tels que de l'audio, des images, des animations, de la vidéo. Enum : "actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor". Raw category sera déprécié, utilisez deviceCategory à la place pour éviter les conflits avec d'autres aqttributes nommés category.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: État de cet appareil d'un point de vue opérationnel. Sa valeur peut dépendre du fournisseur  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction[string]`: Enum : "Inlet, Outlet, Entry, Exit". Un horodatage indiquant la date d'installation du dispositif (s'il doit être installé).  . Model: [ https://schema.org/DateTime]( https://schema.org/DateTime)- `distance[number]`: Emplacement de cet appareil représenté par une distance à partir d'un point de départ. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [https://schema.org/Distance](https://schema.org/Distance)- `dstAware[boolean]`: Indique que l'appareil est conscient de l'heure d'été (True). Si c'est le cas, l'horodatage est automatiquement ajusté par l'appareil pour refléter les changements d'heure d'été. Si ce n'est pas le cas (Faux), l'utilisateur doit s'occuper de l'ajustement de l'heure.  - `firmwareVersion[string]`: La version du micrologiciel de cet appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: La version du matériel de cet appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `ipAddress[array]`: Liste des adresses IP de l'appareil. Il peut s'agir d'une liste de valeurs séparées par des virgules si l'appareil a plus d'une adresse IP.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `macAddress[string]`: L'adresse MAC de l'appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `mcc[string]`: Cette propriété identifie l'indicatif de pays de la téléphonie mobile  . Model: [https://schema.org/Text](https://schema.org/Text)- `mnc[string]`: Cette propriété identifie le code de réseau mobile (MNC) du réseau auquel l'appareil est connecté. Le MNC est utilisé en combinaison avec un code de pays mobile (MCC) (également connu sous le nom de "tuple MCC / MNC") pour identifier de manière unique un opérateur de téléphonie mobile utilisant les réseaux mobiles terrestres publics GSM, CDMA, iDEN, TETRA et 3G / 4G et certains réseaux mobiles par satellite.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément  - `osVersion[string]`: La version du système d'exploitation de l'hôte  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `provider[string]`: Le fournisseur du dispositif  . Model: [https://schema.org/provider](https://schema.org/provider)- `refDeviceModel[*]`: Modèle de l'appareil  - `relativePosition[string]`: Emplacement de ce dispositif dans un système de coordonnées en fonction de son emplacement local  - `rssi[number]`: Indicateur de l'intensité du signal reçu pour un appareil sans fil. Il doit être exprimé en dBm ou en mW, utilisez unitcode pour le définir.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `serialNumber[string]`: Le numéro de série attribué par le fabricant  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `softwareVersion[string]`: La version du logiciel de cet appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `supportedProtocol[array]`: Protocole(s) ou réseaux pris en charge  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'un appareil  - `value[string]`: Valeur observée ou signalée. Pour les dispositifs d'actionnement, il s'agit d'un attribut qui permet à une application de contrôle de modifier le réglage de l'actionnement. Par exemple, un dispositif de commutation qui est actuellement _on_ peut signaler une valeur "on" de type "Text". Il est évident que pour faire basculer l'interrupteur en question, la valeur de cet attribut devra être changée en "off  . Model: [https://schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `controlledProperty`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Un dispositif est un objet tangible qui contient une certaine logique et qui est producteur et/ou consommateur de données. Un appareil est toujours supposé être capable de communiquer électroniquement par l'intermédiaire d'un réseau. Ce modèle de données a été partiellement développé en coopération avec les opérateurs de téléphonie mobile et la [GSMA] (https://www.gsma.com/iot/iot-big-data/). Ce modèle de données réutilise des concepts provenant de l'[Ontologie SAREF](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) qui fait partie des normes de l'[ETSI](http://www.etsi.org).  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
        description: Every type of device that can be included in the array    
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
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    configuration:    
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model'    
      items:    
        properties:    
          parameter:    
            description: Name of the parameter in the configuration of the device    
            type: string    
            x-ngsi:    
              type: Property    
          value:    
            description: Value of the parameter in the configuration of the device    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    controlledAsset:    
      description: 'List of the asset(s) (building, object, etc.) controlled by the device'    
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
        model: https://schema.org/Text    
        type: Property    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        description: Every possible property controlled by the device    
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
        x-ngsi:    
          type: Property    
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
        description: Every type of device that can be included in the array    
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
        x-ngsi:    
          type: Property    
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
      description: Model of the device    
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
        description: Every type of protocols that can be used by the device    
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
        x-ngsi:    
          type: Property    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/Device/schema.json    
  x-model-tags: ""    
  x-version: 0.0.9    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Device NGSI-v2 key-values Exemple  
Voici un exemple de dispositif au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Dispositif NGSI-v2 normalisé Exemple  
Voici un exemple de dispositif au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Device NGSI-LD key-values Exemple  
Voici un exemple de dispositif au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Dispositif NGSI-LD normalisé Exemple  
Voici un exemple de dispositif au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
