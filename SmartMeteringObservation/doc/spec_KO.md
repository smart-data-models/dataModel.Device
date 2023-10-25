<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: SmartMeteringObservation  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티에는 일반적으로 스마트 홈, 산업, 도시 및 농업에 적용되는 스마트 미터 관측에 대한 조화로운 설명이 포함되어 있습니다. 대부분 GSMA 엔티티 정의에 기반하지만 확장**되었습니다.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `entityVersion[string]`: 엔티티 사양 버전입니다. 버전 번호가 2.0 이상이면 엔티티가 NGSI-LD를 사용하여 표현되었음을 나타냅니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `meterType[string]`: 계량되는 공급 유형(예: 전기, 휘발유, 경유): 전기, 휘발유, 수도, 메탄, 디젤  - `name[string]`: 이 항목의 이름  - `offPeakConsumption[number]`: 설치 이후 계량기에 기록된 '사용량이 적은' 시간대(특히 전기 공급과 관련됨)에 공급된 제품의 총량입니다. 전기의 경우 KWH(킬로와트시), 가스 또는 액체의 경우 LTR(리터) 또는 MTQ(세제곱미터)와 같은 관련 단위코드를 지정해야 합니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `peakConsumption[number]`: 설치 이후 계량기에 기록된 '피크' 시간대(특히 전기 공급과 관련됨) 동안 공급된 제품의 총량입니다. 전기의 경우 KWH(킬로와트시), 가스 또는 액체의 경우 LTR(리터) 또는 MTQ(세제곱미터)와 같은 관련 단위코드를 지정해야 합니다.  - `powerFactor[number]`: 산업에서 자주 사용되는 3상 전기 공급 장치와 관련된 역률은 용량성 부하와 유도성 부하 간의 순 균형에 따라 -1에서 +1까지 다양합니다. 이 값을 사용하면 계량기 설치 이후 평균 역률을 측정합니다.  - `refDevice[*]`: SmartMeteringObservation에 연결된 엔티티(장치)의 고유 식별자  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `totalConsumption[number]`: 설치 이후 계량기에 기록된 대로 공급된 제품의 총량입니다. 관련 단위코드는 전기의 경우 KWH(킬로와트시), 가스 또는 액체의 경우 LTR(리터) 또는 MTQ(세제곱미터)와 같이 지정해야 합니다.  - `type[string]`: SmartMeteringObservation이어야 합니다. NGSI 엔티티 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
GSMA 데이터 모델에서 채택되었지만 모든 스마트 데이터 모델과 호환됩니다. 개별 속성에 따라 확장됩니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SmartMeteringObservation:    
  description: 'This entity contains a harmonised description of a Smart Meter Observation, generally applicable for Smart Homes, Industry, Cities and Agriculture. It is based mostly in the GSMA entity definition but it is extended'    
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
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    entityVersion:    
      description: The entity specification version. A version number of 2.0 or later denotes the entity is represented using NGSI-LD    
      enum:    
        - 2.0    
        - LD    
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
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
    meterType:    
      description: 'The type of supply being metered e.g.: Electricity, Gasoline, Water, Methane, Diesel'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    offPeakConsumption:    
      description: 'The total amount of product supplied during ''off-peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
      x-ngsi:    
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
    peakConsumption:    
      description: 'The total amount of product supplied during ''peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
      x-ngsi:    
        type: Property    
    powerFactor:    
      description: Relevant to 3-Phase electricity supplies often used in industry - the power factor ranges from -1 to +1 depending on the net balance between capacitive and inductive loads. If used this measures the average power factor since meter installation    
      type: number    
      x-ngsi:    
        type: Property    
    refDevice:    
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
      description: Unique identifier of the entity (Device) linked to the SmartMeteringObservation    
      x-ngsi:    
        type: Relationship    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    totalConsumption:    
      description: 'The total amount of product supplied as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be SmartMeteringObservation. NGSI entity type    
      enum:    
        - SmartMeteringObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/SmartMeteringObservation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### SmartMeteringObservation NGSI-v2 키 값 예제  
다음은 JSON-LD 형식의 스마트미터링옵저버를 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SmartMeteringObservation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SmartMeteringObservation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SmartMeteringObservation NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 스마트미터링옵저버를 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
    "type": "SmartMeteringObservation",  
    "address": {  
        "addressLocality": "London",  
        "postalCode": "EC4N 8AF",  
        "streetAddress": "25 Walbrook"  
    },  
    "dataProvider": "https://provider.example.com",  
    "entityVersion": "2.0",  
    "image": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg==",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -103.9904,  
            39.7564  
        ]  
    },  
    "meterType": "Electricity",  
    "offPeakConsumption": 8.0,  
    "peakConsumption": 9.3,  
    "powerFactor": 0.98,  
    "refDevice": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac",  
    "source": "https://source.example.com",  
    "totalConsumption": 7.0,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SmartMeteringObservation NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SmartMeteringObservation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
    "type": "SmartMeteringObservation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "London",  
            "postalCode": "EC4N 8AF",  
            "streetAddress": "25 Walbrook"  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "entityVersion": {  
        "type": "Property",  
        "value": "2.0"  
    },  
    "image": {  
        "type": "Property",  
        "value": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg=="  
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
    "meterType": {  
        "type": "Property",  
        "value": "Electricity"  
    },  
    "offPeakConsumption": {  
        "type": "Property",  
        "value": 8.0  
    },  
    "peakConsumption": {  
        "type": "Property",  
        "value": 9.3  
    },  
    "powerFactor": {  
        "type": "Property",  
        "value": 0.98  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac"  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "totalConsumption": {  
        "type": "Property",  
        "value": 7.0  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
