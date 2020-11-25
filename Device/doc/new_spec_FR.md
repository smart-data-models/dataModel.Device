Entité : Dispositif :  
=====================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Un appareil (matériel + logiciel + micrologiciel) destiné à accomplir une tâche particulière (détection de l'environnement, actionnement, etc.).**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `batteryLevel`:   - `configuration`:   - `controlledAsset`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateFirstUsed`:   - `dateInstalled`:   - `dateLastCalibration`:   - `dateLastValueReported`:   - `dateManufactured`:   - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `depth`:   - `description`: Une description de cet article  - `deviceState`:   - `direction`:   - `distance`:   - `firmwareVersion`:   - `hardwareVersion`:   - `id`:   - `ipAddress`:   - `location`:   - `macAddress`:   - `mnc`:   - `name`: Le nom de cet article.  - `osVersion`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `provider`:   - `refDeviceModel`:   - `relativePosition`:   - `rssi`:   - `seeAlso`:   - `serialNumber`:   - `softwareVersion`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: NGSI Type d'entité  - `value`:   ## Modèle de données description des biens  
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
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
    configuration:    
      type: object    
    controlledAsset:    
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
      type: array    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFirstUsed:    
      format: date-time    
      type: string    
    dateInstalled:    
      format: date-time    
      type: string    
    dateLastCalibration:    
      format: date-time    
      type: string    
    dateLastValueReported:    
      format: date-time    
      type: string    
    dateManufactured:    
      format: date-time    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      type: number    
    description:    
      description: 'A description of this item'    
      type: Property    
    deviceState:    
      type: string    
    direction:    
      enum:    
        - Inlet    
        - Outlet    
        - Entry    
        - Exit    
      type: string    
    distance:    
      type: number    
    firmwareVersion:    
      type: string    
    hardwareVersion:    
      type: string    
    id:    
      anyOf: *device_-_properties_-_id_-_anyof    
    ipAddress:    
      items:    
        oneOf:    
          - format: ipv4    
          - format: ipv6    
        type: string    
      type: array    
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
      items:    
        pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
        type: string    
      type: array    
    mnc:    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    osVersion:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *device_-_properties_-_id_-_anyof    
      type: Property    
    provider:    
      type: string    
    refDeviceModel:    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *device_-_properties_-_id_-_anyof    
    relativePosition:    
      type: string    
    rssi:    
      type: number    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    serialNumber:    
      type: string    
    softwareVersion:    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Device    
      type: string    
    value:    
      type: string    
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
Voici un exemple d'un appareil au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'appareil au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
