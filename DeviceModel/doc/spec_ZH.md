<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。设备模型  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体捕获了一个设备的静态属性。**  
版本：0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `alternateName[string]`: 这个项目的一个替代名称  - `annotations[array]`: 关于该项目的注释  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 设备的品牌名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 传感器。检测并对物理环境中的事件或变化做出反应的装置，如光、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制一个机制或系统的装置。https://w3id.org/saref#Actuator。计量器 : 为准确检测并以人类可读的形式显示某一数量而建造的设备。部分由SAREF定义。HVAC : 暖气、通风和空调（HVAC）设备，提供室内环境舒适度。https://w3id.org/saref#HVAC。网络 : 用于连接网络中其他设备的设备，如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network.多媒体 :用于显示、存储、记录或播放多媒体内容的设备，如音频、图像、动画、视频。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'。原始类别将被废弃，使用deviceCategory代替，以避免与其他名为类别的aqttributes冲突。  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `controlledProperty[array]`: 任何可以被感知、测量或控制的东西。枚举。空气污染, 大气压力, 平均速度, 电池寿命, 电池供应, 电池容量, 电导率, 电导率, 深度, 饮食活动, 电力消耗, 能量, 填充水平, 自由氯, 气体消耗, 开门, 湿度, 光, 位置, 挤奶, 运动, 运动活动,噪声水平, 占用率, orp, pH值, 功率, 降水, 压力, 折射指数, 盐度, 烟雾, 土壤湿度, 太阳辐射, 速度, tds, 温度, 交通流量, tss, 浊度, 耗水量, 水流量, 水位, 水污染, 天气状况, 重量, 风向, 风速'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `deviceCategory[array]`: 传感器。探测并对物理环境中的事件或变化做出反应的设备，如光、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制一个机制或系统的设备。https://w3id.org/saref#Actuator。计量器 : 为准确检测并以人类可读的形式显示某一数量而建造的设备。部分由SAREF定义。HVAC : 暖气、通风和空调（HVAC）设备，提供室内环境舒适度。https://w3id.org/saref#HVAC。网络 : 用于连接网络中其他设备的设备，如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network.多媒体 :用于显示、存储、记录或播放多媒体内容的设备，如音频、图像、动画、视频。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'。原始类别将被废弃，使用deviceCategory代替，以避免与其他名为类别的aqttributes冲突。  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceClass[string]`: RFC 7228规定的受约束设备的类别。如果设备不是受限设备，这个属性不应出现。规范性引用。[RFC7228](https://tools.ietf.org/html/rfc7228#section-3)。Enum:'C0, C1, C2'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `documentation[string]`: 链接到设备的文档。  . Model: [https://schema.org/URL](https://schema.org/URL)- `energyLimitationClass[string]`: 根据RFC 7228，设备的能量限制等级。规范性引用。[RFC7228](https://tools.ietf.org/html/rfc7228#page-11)。Enum:'E0, E1, E2, E9'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `function[array]`: 完成一个设备所设计的任务所必需的功能。一个设备可以被设计为执行一个以上的功能。由[SAREF]（https://w3id.org/saref#Function）定义。Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `image[string]`: 该物品的图像  . Model: [https://schema.org/URL](https://schema.org/URL)- `macAddress[string]`: 设备的MAC地址。  . Model: [https://schema.org/Text](https://schema.org/Text)- `manufacturerName[string]`: 设备的制造商名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: 设备的型号名称。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `supportedProtocol[array]`: 支持的协议或网络  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `supportedUnits[array]`: 设备支持的测量单位。使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出的测量单位代码（文本）（最多3个字符）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI实体类型。它必须是DeviceModel  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
      description: Device's brand name.    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"    
      items: &devicemodel_-_properties_-_devicecategory_-_items    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      items: *devicemodel_-_properties_-_devicecategory_-_items    
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
      description: A link to device's documentation.    
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
      anyOf: &devicemodel_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
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
      description: The MAC address of the device.    
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manufacturerName:    
      description: Device's manufacturer name.    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: Device's model name.    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *devicemodel_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters).'    
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
## ＃＃＃＃有效载荷的例子  
#### DeviceModel NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的DeviceModel的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### DeviceModel NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的DeviceModel的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### DeviceModel NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的DeviceModel的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DeviceModel NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的DeviceModel的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
