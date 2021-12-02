Entität: SmartMeteringObservation  
=================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung einer Smart Meter Observation, allgemein anwendbar für Smart Homes, Industrie, Städte und Landwirtschaft. Sie basiert größtenteils auf der GSMA-Entity-Definition, ist aber erweitert**.  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `entityVersion`: Die Version der Entitätsspezifikation. Eine Versionsnummer von 2.0 oder höher bedeutet, dass die Entität mit NGSI-LD dargestellt wird  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `meterType`: Die Art der Versorgung, die gemessen wird, z. B.: Elektrizität, Benzin, Wasser, Methan, Diesel.  - `name`: Der Name dieses Elements.  - `offPeakConsumption`: Die vom Zähler seit der Installation aufgezeichnete Gesamtmenge des Produkts, die während der Schwachlastzeiten geliefert wurde (besonders relevant für die Stromversorgung). Es sollte der entsprechende UnitCode angegeben werden, z. B. KWH (Kilo Watt Hours) für Strom, LTR (Liter) oder MTQ (Kubikmeter) für Gase oder Flüssigkeiten.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `peakConsumption`: Die vom Zähler seit der Installation aufgezeichnete Gesamtmenge des gelieferten Produkts während der "Spitzenstunden" (besonders relevant für die Stromversorgung). Es sollte der entsprechende UnitCode angegeben werden, z. B. KWH (Kilo Watt Hours) für Strom, LTR (Liter) oder MTQ (Kubikmeter) für Gase oder Flüssigkeiten.  - `powerFactor`: Relevant für 3-Phasen-Stromversorgungen, die häufig in der Industrie verwendet werden - der Leistungsfaktor reicht von -1 bis +1, abhängig von der Nettobilanz zwischen kapazitiven und induktiven Lasten. Falls verwendet, misst dies den durchschnittlichen Leistungsfaktor seit der Zählerinstallation.  - `refDevice`: Eindeutiger Bezeichner der Entität  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `totalConsumption`: Die Gesamtmenge des gelieferten Produkts, wie vom Zähler seit der Installation aufgezeichnet. Es sollte der entsprechende UnitCode angegeben werden, z. B. KWH (Kilo Watt Hours) für Strom, LTR (Liter) oder MTQ (Kubikmeter) für Gase oder Flüssigkeiten.  - `type`: Es muss SmartMeteringObservation sein. NGSI-Entitätstyp    
Erforderliche Eigenschaften  
- `id`  - `type`    
Angepasst von GSMA-Datenmodellen, aber kompatibel mit allen Smart-Datenmodellen zu sein. Erweitert um individuelle Eigenschaften.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SmartMeteringObservation:    
  description: 'This entity contains a harmonised description of a Smart Meter Observation, generally applicable for Smart Homes, Industry, Cities and Agriculture. It is based mostly in the GSMA entity definition but it is extended'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    entityVersion:    
      description: 'The entity specification version. A version number of 2.0 or later denotes the entity is represented using NGSI-LD'    
      enum:    
        - 2.0    
        - LD    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: &smartmeteringobservation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    meterType:    
      description: 'The type of supply being metered e.g.: Electricity, Gasoline, Water, Methane, Diesel.'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    offPeakConsumption:    
      description: 'The total amount of product supplied during ''off-peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartmeteringobservation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    peakConsumption:    
      description: 'The total amount of product supplied during ''peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids.'    
      type: Property    
    powerFactor:    
      description: 'Relevant to 3-Phase electricity supplies often used in industry - the power factor ranges from -1 to +1 depending on the net balance between capacitive and inductive loads. If used this measures the average power factor since meter installation.'    
      type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    totalConsumption:    
      description: 'The total amount of product supplied as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids.'    
      type: Property    
    type:    
      description: 'It has to be SmartMeteringObservation. NGSI entity type'    
      enum:    
        - SmartMeteringObservation    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### SmartMeteringObservation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine SmartMeteringObservation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "entityVersion": "2.0",  
  "meterType": "Electricity",  
  "refDevice": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "image": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg==",  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook"  
  },  
  "totalConsumption": 7.0,  
  "peakConsumption": 9.3,  
  "offPeakConsumption": 8.0,  
  "powerFactor": 0.98  
}  
```  
#### SmartMeteringObservation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine SmartMeteringObservation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "entityVersion": {  
    "type": "Number",  
    "value": "2.0"  
  },  
  "meterType": {  
    "type": "Text",  
    "value": "Electricity"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "image": {  
    "type": "Text",  
    "value": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg=="  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook"  
    }  
  },  
  "totalConsumption": {  
    "type": "Number",  
    "value": 7.0  
  },  
  "peakConsumption": {  
    "type": "Number",  
    "value": 9.3  
  },  
  "offPeakConsumption": {  
    "type": "Number",  
    "value": 8.0  
  },  
  "powerFactor": {  
    "type": "Number",  
    "value": 0.98  
  }  
}  
```  
#### SmartMeteringObservation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine SmartMeteringObservation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "entityVersion": "2.0",  
  "meterType": "Electricity",  
  "refDevice": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "image": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg==",  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook"  
  },  
  "totalConsumption": 7.0,  
  "peakConsumption": 9.3,  
  "offPeakConsumption": 8.0,  
  "powerFactor": 0.98,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SmartMeteringObservation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine SmartMeteringObservation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "entityVersion": {  
    "type": "Property",  
    "value": "2.0"  
  },  
  "meterType": {  
    "type": "Property",  
    "value": "Electricity"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "image": {  
    "type": "Property",  
    "value": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg=="  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook"  
    }  
  },  
  "totalConsumption": {  
    "type": "Property",  
    "value": 7.0  
  },  
  "peakConsumption": {  
    "type": "Property",  
    "value": 9.3  
  },  
  "offPeakConsumption": {  
    "type": "Property",  
    "value": 8.0  
  },  
  "powerFactor": {  
    "type": "Property",  
    "value": 0.98  
  }  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht