Entidad: SmartMeteringObservation  
=================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción armonizada de la observación de un contador inteligente, generalmente aplicable a los hogares inteligentes, la industria, las ciudades y la agricultura. Se basa principalmente en la definición de entidad de la GSMA, pero se amplía**.  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `entityVersion`: La versión de la especificación de la entidad. Un número de versión 2.0 o posterior indica que la entidad está representada con NGSI-LD  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `meterType`: El tipo de suministro que se mide, por ejemplo Electricidad, gasolina, agua, metano, gasóleo.  - `name`: El nombre de este artículo.  - `offPeakConsumption`: La cantidad total de producto suministrado durante las horas de menor consumo (especialmente en el caso del suministro de electricidad) registrada por el contador desde su instalación. Debe especificarse el código de unidad correspondiente, como KWH (kilovatios hora) para la electricidad, LTR (litros) o MTQ (metros cúbicos) para los gases o líquidos.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `peakConsumption`: La cantidad total de producto suministrado durante las horas "punta" (especialmente en el caso del suministro de electricidad) registrada por el contador desde su instalación. Debe especificarse el código de unidad correspondiente, como KWH (kilovatios hora) para la electricidad, LTR (litros) o MTQ (metros cúbicos) para los gases o líquidos.  - `powerFactor`: Relevante para los suministros eléctricos trifásicos que se utilizan a menudo en la industria: el factor de potencia oscila entre -1 y +1, dependiendo del equilibrio neto entre las cargas capacitivas e inductivas. Si se utiliza, mide el factor de potencia medio desde la instalación del contador.  - `refDevice`: Identificador único de la entidad  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `totalConsumption`: La cantidad total de producto suministrado registrada por el contador desde su instalación. Debe especificarse el código de unidad correspondiente, como KWH (kilovatios hora) para la electricidad, LTR (litros) o MTQ (metros cúbicos) para los gases o líquidos.  - `type`: Tiene que ser SmartMeteringObservation. Tipo de entidad NGSI    
Propiedades requeridas  
- `id`  - `type`    
Adaptado de los modelos de datos de la GSMA, pero para que sea compatible con todos los modelos de datos inteligentes. Ampliado por propiedades individuales.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### SmartMeteringObservation NGSI-v2 key-values Ejemplo  
Este es un ejemplo de una SmartMeteringObservation en formato JSON-LD como valores clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### SmartMeteringObservation NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una SmartMeteringObservation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### SmartMeteringObservation NGSI-LD key-values Ejemplo  
Este es un ejemplo de una SmartMeteringObservation en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### SmartMeteringObservation NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una SmartMeteringObservation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
