<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: PolarH10  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Device/blob/master/PolarH10/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: RR, HRV, HR, ECG를 갖춘 Polar H10 심박수 센서의 데이터 모델****  
버전: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `acc[array]`: 25Hz, 50Hz, 100Hz, 200Hz의 샘플 속도와 2G, 4G, 8G 범위의 가속도계 데이터입니다. 축별 가속도 데이터(mG).  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientId[string]`: 클라이언트 ID  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceId[string]`: 장치 ID  - `ecg[array]`: 샘플 속도 130Hz의 µV 단위 심전도(ECG) 데이터.  - `hr[number]`: 1초 샘플 시간 또는 5초 샘플 시간의 심박수(HR)  - `hrv[number]`: 심박수 변동성(HRV) 심박수 변동성  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `rr[array]`: 연속적인 심장 박동 간격(RR)(ms)  - `sampleRate[number]`: 데이터 수집 속도  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `sensorTimeStamp[number]`: 센서 타임스탬프  - `sessionId[number]`: 세션 ID  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `timeStamp[number]`: 전화 타임스탬프  - `type[string]`: NGSI 엔티티 유형. PolarH10TopicACC여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PolarH10:    
  description: A Data Model of Polar H10 Heart Rate Sensor with RR, HRV, HR, and ECG    
  properties:    
    acc:    
      description: Accelerometer data with sample rates of 25Hz, 50Hz, 100Hz and 200Hz and range of 2G, 4G and 8G. Axis specific acceleration data in mG.    
      items:    
        description: Each of the measurement of the accelerometer    
        items:    
          description: Each of the measurement of the accelerometer in the X, Y, Z coordinates    
          type: integer    
          x-ngsi:    
            type: Property    
        maxItems: 3    
        minItems: 3    
        type: array    
        x-ngsi:    
          type: Property    
      maxItems: 36    
      minItems: 36    
      type: array    
      x-ngsi:    
        type: Property    
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
    clientId:    
      description: Client ID    
      type: string    
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
    deviceId:    
      description: Device ID    
      type: string    
      x-ngsi:    
        type: Property    
    ecg:    
      description: Electrocardiography (ECG) data in µV with sample rate 130Hz.    
      items:    
        description: Each of the ECG measurements    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    hr:    
      description: Heart Rate (HR) with one second sample time or with five second sample time    
      type: number    
      x-ngsi:    
        type: Property    
    hrv:    
      description: Heart Rate Variability (HRV) heart rate variability    
      type: number    
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
    rr:    
      description: Intervals between successive heartbeats (RR) in ms    
      items:    
        description: Each of the measurements of the RR    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    sampleRate:    
      description: Data acquisition rate    
      type: number    
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
    sensorTimeStamp:    
      description: Sensor Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    sessionId:    
      description: Session ID    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    timeStamp:    
      description: Phone Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be PolarH10TopicACC    
      enum:    
        - PolarH10    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PolarH10/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.Device/tree/master/PolarH10/schema.json    
  x-model-tags: P2CODE    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### PolarH10 NGSI-v2 키 값 예시  
다음은 JSON-LD 형식의 PolarH10을 키 값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PolarH10의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Text",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Text",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Number",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Number",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Number",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Number",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Array",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Number",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Number",  
        "value": 50  
    },  
    "rr": {  
        "type": "Array",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Array",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    }  
}  
```  
</details>  
#### PolarH10 NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 PolarH10을 키값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PolarH10의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Property",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Property",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Property",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Property",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Property",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Property",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Property",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Property",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Property",  
        "value": 50  
    },  
    "rr": {  
        "type": "Property",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Property",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
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
