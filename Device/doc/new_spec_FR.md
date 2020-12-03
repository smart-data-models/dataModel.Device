Entité : Dispositif :  
=====================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Un appareil (matériel + logiciel + micrologiciel) destiné à accomplir une tâche particulière (détection de l'environnement, actionnement, etc.).**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `batteryLevel`: Niveau de la batterie de l'appareil. Il doit être égal à 1,0 lorsque la batterie est pleine. 0,0 lorsque la batterie est vide. -1 lorsque l'on ne peut pas déterminer de façon transitoire.  - `configuration`: La configuration technique de l'appareil. Cet attribut est destiné à être un dictionnaire de propriétés qui saisit les paramètres qui ont trait à la configuration d'un appareil (délais, périodes de rapport, etc.) et qui ne sont pas actuellement couverts par les attributs standard définis par ce modèle.  - `controlledAsset`: Liste du ou des biens (bâtiment, objet, etc.) contrôlés par l'appareil.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateFirstUsed`: Un horodatage qui indique la date de la première utilisation de l'appareil.  - `dateInstalled`: Un horodatage qui indique la date d'installation de l'appareil (si celui-ci doit être installé).  - `dateLastCalibration`: Un horodatage qui indique la date du dernier calibrage de l'appareil.  - `dateLastValueReported`:   - `dateManufactured`: Un horodatage qui indique la date de fabrication de l'appareil.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `depth`: Emplacement de cet appareil représenté par une profondeur à partir d'un point de départ. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html)  - `description`: Une description de cet article  - `deviceState`: État de ce dispositif d'un point de vue opérationnel. Sa valeur peut dépendre du vendeur.  - `direction`: Enum : "Inlet, Outlet, Entry, Exit". Un horodatage qui indique quand l'appareil a été installé (s'il doit être installé).  - `distance`: Emplacement de cet appareil représenté par une distance par rapport à un point de départ. Tous les appareils sont acceptés en code [CEFACT](https://www.unece.org/cefact.html)  - `firmwareVersion`: La version du micrologiciel de cet appareil.  - `hardwareVersion`: La version matérielle de cet appareil.  - `id`:   - `ipAddress`: Liste de l'adresse IP de l'appareil. Il peut s'agir d'une liste de valeurs séparées par des virgules si l'appareil a plus d'une adresse IP.  - `location`:   - `macAddress`: L'adresse MAC de l'appareil  - `mnc`: Cette propriété identifie le code de réseau mobile (MNC) du réseau auquel l'appareil est connecté. Le MNC est utilisé en combinaison avec un code de pays mobile (MCC) (également appelé "tuple MCC / MNC") pour identifier de manière unique un opérateur de téléphonie mobile utilisant les réseaux mobiles terrestres publics GSM, CDMA, iDEN, TETRA et 3G / 4G et certains réseaux mobiles par satellite.  - `name`: Le nom de cet article.  - `osVersion`: La version du système d'exploitation hôte.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `provider`: Le fournisseur de l'appareil.  - `refDeviceModel`: Modèle de l'appareil  - `relativePosition`: Localisation de cet appareil dans un système de coordonnées en fonction de son emplacement local.  - `rssi`: Indicateur de la puissance du signal reçu pour un appareil sans fil. Il doit être exprimé en dBm ou mW, utilisez le code de l'unité pour l'indiquer.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `serialNumber`: Le numéro de série attribué par le fabricant.  - `softwareVersion`: La version logicielle de cet appareil.  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Oroperty. Type d'entité NGSI. Il doit s'agir de Device  - `value`: Une valeur observée ou rapportée. Pour les dispositifs d'actionnement, c'est un attribut qui permet à une application de contrôle de modifier le réglage de l'actionnement. Par exemple, un dispositif de commutation qui est actuellement _on_ peut rapporter une valeur `on` de type `Text`. Evidemment, pour pouvoir basculer l'interrupteur en question, la valeur de cet attribut devra être changée en "off".    
Propriétés requises  
- `category`  - `controlledProperty`  - `id`  - `type`    
Un Dispositif est un objet tangible qui contient une certaine logique et qui est producteur et/ou consommateur de données. Un dispositif est toujours supposé être capable de communiquer électroniquement via un réseau. Ce modèle de données a été partiellement développé en coopération avec les opérateurs de téléphonie mobile et la [GSMA] (https://www.gsma.com/iot/iot-big-data/). Ce modèle de données réutilise des concepts provenant de la partie [SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) des normes [ETSI](http://www.etsi.org).  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
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
## Exemples de charges utiles  
#### Dispositif NGSI V2 valeurs clés Exemple  
Voici un exemple d'appareil au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Dispositif NGSI V2 normalisé Exemple  
Voici un exemple d'un appareil au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Dispositif NGSI-LD valeurs clés Exemple  
Voici un exemple d'appareil au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Dispositif NGSI-LD normalisé Exemple  
Voici un exemple d'un appareil au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
