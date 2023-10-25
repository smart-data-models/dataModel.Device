<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 장치 모델  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티는 디바이스의 정적 속성을 캡처합니다. **  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `annotations[array]`: 항목에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 디바이스 브랜드 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 센서: 빛, 동작, 온도 변화 등 물리적 환경의 이벤트나 변화를 감지하고 이에 반응하는 장치 https://w3id.org/saref#Sensor. 액추에이터 : 메커니즘이나 시스템을 움직이거나 제어하는 역할을 하는 장치 https://w3id.org/saref#Actuator. 계량기 : 사람이 읽을 수 있는 형태로 수량을 정확하게 감지하고 표시하도록 제작된 장치. SAREF에서 부분적으로 정의. HVAC: 실내 환경의 쾌적함을 제공하는 난방, 환기 및 에어컨(HVAC) 장치. https://w3id.org/saref#HVAC. 네트워크: LAN 또는 센서 네트워크의 허브, 스위치 또는 라우터와 같이 네트워크에서 다른 장치를 연결하는 데 사용되는 장치. (https://w3id.org/saref#Network. 멀티미디어 : 오디오, 이미지, 애니메이션, 비디오와 같은 멀티미디어 콘텐츠를 표시, 저장, 녹화 또는 재생하도록 설계된 장치. 열거형: '액추에이터, 비콘, 엔드건, HVAC, 구현, irrSection, irrSystem, 미터, 멀티미디어, 네트워크, 센서'. 원시 카테고리는 더 이상 사용되지 않습니다. 카테고리라는 이름의 다른 어트리뷰트와의 충돌을 피하기 위해 대신 deviceCategory를 사용하십시오.  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)- `controlledProperty[array]`: 감지, 측정 또는 제어할 수 있는 모든 항목입니다. Enum:'공기오염, 대기압력, 평균속도, 배터리수명, 배터리수급, cdom, 컨덕턴스, 전도도, 깊이, 먹는활동, 전기소비량, 에너지, 충전량레벨, 무료염소, 가스소비량, 게이트개방, 방향, 습도, 빛, 위치, 착유, 동작, 이동활동, 소음레벨, 점유, orp, pH, 전력, 강수량, 압력, 굴절지수, 염분, 연기, 토양수분, 태양복사, 속도, tds, 온도, 교통흐름, tss, 탁도, 물소비량, 물흐름, 물레벨, 물오염, 날씨조건, 무게, 바람방향, 바람속도'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `deviceCategory[array]`: 센서: 빛, 동작, 온도 변화 등 물리적 환경의 이벤트나 변화를 감지하고 이에 반응하는 장치 https://w3id.org/saref#Sensor. 액추에이터 : 메커니즘이나 시스템을 움직이거나 제어하는 역할을 하는 장치 https://w3id.org/saref#Actuator. 계량기 : 사람이 읽을 수 있는 형태로 수량을 정확하게 감지하고 표시하도록 제작된 장치. SAREF에서 부분적으로 정의. HVAC: 실내 환경의 쾌적함을 제공하는 난방, 환기 및 에어컨(HVAC) 장치. https://w3id.org/saref#HVAC. 네트워크: LAN 또는 센서 네트워크의 허브, 스위치 또는 라우터와 같이 네트워크에서 다른 장치를 연결하는 데 사용되는 장치. (https://w3id.org/saref#Network. 멀티미디어 : 오디오, 이미지, 애니메이션, 비디오와 같은 멀티미디어 콘텐츠를 표시, 저장, 녹화 또는 재생하도록 설계된 장치. 열거형: '액추에이터, 비콘, 엔드건, HVAC, 구현, irrSection, irrSystem, 미터, 멀티미디어, 네트워크, 센서'. 원시 카테고리는 더 이상 사용되지 않습니다. 카테고리라는 이름의 다른 어트리뷰트와의 충돌을 피하기 위해 대신 deviceCategory를 사용하십시오.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceClass[string]`: RFC 7228에 지정된 제약 장치의 클래스. 장치가 제약된 장치가 아닌 경우 이 속성은 존재하지 않습니다. 규범 참조: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). 열거형:'C0, C1, C2'  . Model: [https://schema.org/Text](https://schema.org/Text)- `documentation[uri]`: 디바이스 설명서 링크  . Model: [https://schema.org/URL](https://schema.org/URL)- `energyLimitationClass[string]`: RFC 7228에 따른 디바이스의 에너지 제한 등급. 규범 참조: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). 열거형:'E0, E1, E2, E9'  . Model: [https://schema.org/Text](https://schema.org/Text)- `function[array]`: 장치가 설계된 작업을 수행하는 데 필요한 기능입니다. 장치는 하나 이상의 기능을 수행하도록 설계될 수 있습니다. SAREF](https://w3id.org/saref#Function)에서 정의합니다. Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `macAddress[string]`: 장치의 MAC 주소  . Model: [https://schema.org/Text](https://schema.org/Text)- `manufacturerName[string]`: 장치의 제조업체 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: 디바이스 모델명  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `supportedProtocol[array]`: 지원되는 프로토콜 또는 네트워크  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `supportedUnits[array]`: 장치에서 지원하는 측정 단위입니다. UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정된 측정 단위 코드(텍스트)(최대 3자)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 엔티티 유형은 DeviceModel이어야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceModel:    
  description: 'This entity captures the static properties of a Device. '    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: Device's brand name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    deviceClass:    
      description: "Class of constrained device as specified by RFC 7228. If the device is not a constrained device this property shall not be present. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'"    
      enum:    
        - C0    
        - C1    
        - C2    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    documentation:    
      description: A link to device's documentation    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    energyLimitationClass:    
      description: "Device's class of energy limitation as per RFC 7228. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'"    
      enum:    
        - E0    
        - E1    
        - E2    
        - E9    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    function:    
      description: "The functionality necessary to accomplish the task for which a Device is designed. A device can be designed to perform more than one function. Defined by [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification"    
      items:    
        enum:    
          - levelControl    
          - sensing    
          - onOff    
          - openClose    
          - metering    
          - eventNotification    
        type: string    
      type: array    
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
    macAddress:    
      description: The MAC address of the device    
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manufacturerName:    
      description: Device's manufacturer name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: Device's model name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
          type: Property    
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
    supportedUnits:    
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters)'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. it has to be DeviceModel    
      enum:    
        - DeviceModel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - category    
    - controlledProperty    
    - manufacturerName    
    - brandName    
    - modelName    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/DeviceModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/DeviceModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### DeviceModel NGSI-v2 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 DeviceModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "name": "myDevice Sensor for Containers 345",  
  "brandName": "myDevice",  
  "modelName": "S4Container 345",  
  "manufacturerName": "myDevice Inc.",  
  "deviceCategory": ["sensor"],  
  "function": ["sensing"],  
  "controlledProperty": ["fillingLevel", "temperature"]  
}  
```  
</details>  
#### DeviceModel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 DeviceModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "deviceCategory": {  
    "type": "array",  
    "value": [  
      "sensor"  
    ]  
  },  
  "function": {  
    "type": "array",  
    "value": [  
      "sensing"  
    ]  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "S4Container 345"  
  },  
  "name": {  
    "type": "Text",  
    "value": "myDevice Sensor for Containers 345"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "myDevice"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "myDevice Inc."  
  },  
  "controlledProperty": {  
    "type": "array",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  }  
}  
```  
</details>  
#### 장치모델 NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 DeviceModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "brandName": "myDevice",  
  "deviceCategory": [  
    "sensor"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "function": [  
    "sensing"  
  ],  
  "manufacturerName": "myDevice Inc.",  
  "modelName": "S4Container 345",  
  "name": "myDevice Sensor for Containers 345",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### DeviceModel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 DeviceModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "brandName": {  
    "type": "Property",  
    "value": "myDevice"  
  },  
  "deviceCategory": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "function": {  
    "type": "Property",  
    "value": [  
      "sensing"  
    ]  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "myDevice Inc."  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "S4Container 345"  
  },  
  "name": {  
    "type": "Property",  
    "value": "myDevice Sensor for Containers 345"  
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
