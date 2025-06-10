<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티 UWBAnchor  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Device/blob/master/UWBAnchor/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **UWB 태그에서 방출되는 UWB 펄스를 감지하여 태그 위치를 계산하기 위해 위치 서버로 전달하는 전자 장치인 초광대역(UWB) 앵커의 데이터 모델**입니다.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `data[object]`: UWB 앵커의 해당 데이터입니다.  	- `anchorData[array]`: 앵커 데이터 정보.    
	- `coordinates[object]`: 좌표 데이터.    
	- `metrics[object]`: 메트릭 데이터.    
	- `moving[boolean]`: 이동 상태.    
	- `tagData[object]`: 데이터 정보에 태그를 지정합니다.    
	- `zones[array]`: 구역 정보.    
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `success[boolean]`: 성공 상태.  - `tagId[string]`: 태그 ID.  - `timestamp[number]`: 데이터의 타임스탬프.  - `type[string]`: NGSI 엔티티 유형. UWBAnchor여야 합니다.  - `version[string]`: 데이터의 버전입니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `tagId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UWBAnchor:    
  description: Data model for the Ultra Wideband (UWB) Anchor which are electronic devices that detect UWB pulses emitted by UWB Tags and forward them to the location server for calculating tag positions.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    data:    
      description: Corresponding data of the UWB Anchor.    
      properties:    
        anchorData:    
          description: Anchor data information.    
          items:    
            properties:    
              anchorId:    
                description: Anchor ID.    
                type: string    
                x-ngsi:    
                  type: Property    
              rss:    
                description: RSS value.    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
        coordinates:    
          description: Coordinates data.    
          properties:    
            x:    
              description: X-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
            y:    
              description: Y-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
            z:    
              description: Z-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        metrics:    
          description: Metrics data.    
          properties:    
            latency:    
              description: Latency value.    
              type: number    
              x-ngsi:    
                type: Property    
            rates:    
              description: Rates data.    
              properties:    
                success:    
                  description: Success rate.    
                  type: number    
                  x-ngsi:    
                    type: Property    
                update:    
                  description: Update rate.    
                  type: number    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        moving:    
          description: Moving status.    
          type: boolean    
          x-ngsi:    
            type: Property    
        tagData:    
          description: Tag data information.    
          properties:    
            accelerometer:    
              description: Accelerometer readings.    
              items:    
                description: Each of the accelaration measurements in X, Y, and Z-axis    
                properties:    
                  x:    
                    description: X-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  y:    
                    description: Y-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  z:    
                    description: Z-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            blinkIndex:    
              description: Blink index value.    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        zones:    
          description: Zones information.    
          items:    
            properties:    
              id:    
                description: Zone ID.    
                type: string    
                x-ngsi:    
                  type: Property    
              name:    
                description: Zone name.    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
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
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    name:    
      description: The name of this item    
      type: string    
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
          type: Relationship    
      type: array    
      x-ngsi:    
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
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    success:    
      description: Success status.    
      type: boolean    
      x-ngsi:    
        type: Property    
    tagId:    
      description: Tag ID.    
      type: string    
      x-ngsi:    
        type: Property    
    timestamp:    
      description: Timestamp of the data.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be UWBAnchor    
      enum:    
        - UWBAnchor    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: Version of the data.    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
    - tagId    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/UWBAnchor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Aeronautics/UWB/schema.json    
  x-model-tags: P2CODE    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### UWBAnchor NGSI-v2 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 UWBAnchor의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": "0.1",  
    "tagId": "10006789",  
    "timestamp": 1671165464.3779979,  
    "success": true,  
    "data": {  
        "coordinates": {  
            "x": 29340,  
            "y": 69521,  
            "z": 1000  
        },  
        "tagData": {  
            "blinkIndex": 1896215,  
            "accelerometer": [  
                {  
                    "x": 402,  
                    "y": -890,  
                    "z": -27  
                }  
        ]  
        },  
        "anchorData": [  
            {  
                "anchorId": "4678",  
                "rss": -85  
            },  
            {  
                "anchorId": "5565",  
                "rss": -100  
            },  
            {  
                "anchorId": "4589",  
                "rss": -102  
            },  
            {  
                "anchorId": "8902",  
                "rss": -86  
            },  
            {  
                "anchorId": "5470",  
                "rss": -84  
            },  
            {  
                "anchorId": "3497",  
                "rss": -84  
            }  
        ],  
        "metrics": {  
            "latency": 22,  
            "rates": {  
                "success": 1,  
                "update": 1  
            }  
        },  
        "zones": [  
            {  
                "id": "638a0dert89e49ae7jioy8cc",  
                "name": "Office"  
            }  
        ],  
        "moving": false  
    }  
}  
```  
</details>  
#### UWBAnchor NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 UWBAnchor의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": {  
        "type": "Text",  
        "value": "0.1"  
    },  
    "tagId": {  
        "type": "Text",  
        "value": "10006789"  
    },  
    "timestamp": {  
        "type": "Number",  
        "value": 1671165464.3779979  
    },  
    "success": {  
        "type": "Boolean",  
        "value": true  
    },  
    "data": {  
        "type": "StructuredValue",  
        "value": {  
            "coordinates": {  
                "x": 29340,  
                "y": 69521,  
                "z": 1000  
            },  
            "tagData": {  
                "blinkIndex": 1896215,  
                "accelerometer": [  
                    {  
                        "x": 402,  
                        "y": -890,  
                        "z": -27  
                    }  
                ]  
            },  
            "anchorData": [  
                {  
                    "anchorId": "4678",  
                    "rss": -85  
                },  
                {  
                    "anchorId": "5565",  
                    "rss": -100  
                },  
                {  
                    "anchorId": "4589",  
                    "rss": -102  
                },  
                {  
                    "anchorId": "8902",  
                    "rss": -86  
                },  
                {  
                    "anchorId": "5470",  
                    "rss": -84  
                },  
                {  
                    "anchorId": "3497",  
                    "rss": -84  
                }  
            ],  
            "metrics": {  
                "latency": 22,  
                "rates": {  
                    "success": 1,  
                    "update": 1  
                }  
            },  
            "zones": [  
                {  
                    "id": "638a0dert89e49ae7jioy8cc",  
                    "name": "Office"  
                }  
            ],  
            "moving": false  
        }  
    }  
}  
```  
</details>  
#### UWBAnchor NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 UWBAnchor의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": "0.1",  
    "tagId": "10006789",  
    "timestamp": 1671165464.3779979,  
    "success": true,  
    "data": {  
        "coordinates": {  
            "x": 29340,  
            "y": 69521,  
            "z": 1000  
        },  
        "tagData": {  
            "blinkIndex": 1896215,  
            "accelerometer": [  
                {  
                    "x": 402,  
                    "y": -890,  
                    "z": -27  
                }  
        ]  
        },  
        "anchorData": [  
            {  
                "anchorId": "4678",  
                "rss": -85  
            },  
            {  
                "anchorId": "5565",  
                "rss": -100  
            },  
            {  
                "anchorId": "4589",  
                "rss": -102  
            },  
            {  
                "anchorId": "8902",  
                "rss": -86  
            },  
            {  
                "anchorId": "5470",  
                "rss": -84  
            },  
            {  
                "anchorId": "3497",  
                "rss": -84  
            }  
        ],  
        "metrics": {  
            "latency": 22,  
            "rates": {  
                "success": 1,  
                "update": 1  
            }  
        },  
        "zones": [  
            {  
                "id": "638a0dert89e49ae7jioy8cc",  
                "name": "Office"  
            }  
        ],  
        "moving": false  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/refs/heads/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### UWBAnchor NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 UWBAnchor의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": {  
        "type": "Property",  
        "value": "0.1"  
    },  
    "tagId": {  
        "type": "Property",  
        "value": "10006789"  
    },  
    "timestamp": {  
        "type": "Property",  
        "value": 1671165464.3779979  
    },  
    "success": {  
        "type": "Property",  
        "value": true  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "coordinates": {  
                "x": 29340,  
                "y": 69521,  
                "z": 1000  
            },  
            "tagData": {  
                "blinkIndex": 1896215,  
                "accelerometer": [  
                    {  
                        "x": 402,  
                        "y": -890,  
                        "z": -27  
                    }  
                ]  
            },  
            "anchorData": [  
                {  
                    "anchorId": "4678",  
                    "rss": -85  
                },  
                {  
                    "anchorId": "5565",  
                    "rss": -100  
                },  
                {  
                    "anchorId": "4589",  
                    "rss": -102  
                },  
                {  
                    "anchorId": "8902",  
                    "rss": -86  
                },  
                {  
                    "anchorId": "5470",  
                    "rss": -84  
                },  
                {  
                    "anchorId": "3497",  
                    "rss": -84  
                }  
            ],  
            "metrics": {  
                "latency": 22,  
                "rates": {  
                    "success": 1,  
                    "update": 1  
                }  
            },  
            "zones": [  
                {  
                    "id": "638a0dert89e49ae7jioy8cc",  
                    "name": "Office"  
                }  
            ],  
            "moving": false  
        }  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/refs/heads/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
