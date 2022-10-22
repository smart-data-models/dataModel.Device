<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。隐私对象  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Device/blob/master/PrivacyObject/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**关于物联网设备的隐私信息**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 传感器。探测并对物理环境中的事件或变化做出反应的设备，如光、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制一个机制或系统的设备。https://w3id.org/saref#Actuator。计量器 : 为准确检测并以人类可读的形式显示某一数量而建造的设备。部分由SAREF定义。HVAC : 暖气、通风和空调（HVAC）设备，提供室内环境舒适度。https://w3id.org/saref#HVAC。网络 : 用于连接网络中其他设备的设备，如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network.多媒体 :用于显示、存储、记录或播放多媒体内容的设备，如音频、图像、动画、视频。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `crossborderTransfer[string]`: 说明与该实体有关的跨境转移。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `floor[number]`: 在建筑物内或同等情况下，设备安装的楼层。  - `id[*]`: 实体的唯一标识符  - `image[string]`: 该物品的图像  . Model: [https://schema.org/URL](https://schema.org/URL)- `isIndoor[boolean]`: 表示该实体是安装在室内还是室外的标志。  - `isPersonalData[boolean]`: 标志，表明该实体是否提供或包含个人数据。  - `legitimateInterest[string]`: 与该实体相关的合法利益。这意味着数据收集是为了哪个高级别的最终目的而进行的。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `purpose[string]`: 收集数据的目的。  - `recipientList[array]`: 包含接收者的列表。收件人是使用传感器所产生的数据的受益人。每个接收者由一个URI表示，允许其独特的识别。隐私:'低'  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: 源数据集的唯一标识符。  - `retentionPeriod[string]`: 保留数据的期限。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI类型属性。它必须是PrivacyObject。  - `user[string]`: 一个匿名用户的标识符。这个标识符实际上是一个独特的URN，可以用来匿名识别一个用户。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
PrivacyObject实体代表一个物联网设备（通常是一个传感器），其隐私信息直接与该物联网设备相关联。几个属性被用来描述隐私背景下的物联网设备。值得注意的是，一个属性提供了物联网设备的位置，另外两个属性提供了关于确切位置的更多信息。一个属性也被用来描述物联网设备，第二个属性给出了物联网传感器的目的。其他属性非常注重隐私和GDPR，目的是对与物联网设备相关的信息进行分类。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PrivacyObject:    
  description: 'Information about privacy for an IoT device'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
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
    crossborderTransfer:    
      description: 'Indication about the crossborder transfer linked to the entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    floor:    
      description: 'The floor where the device is installed when in building or equivalent.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &privacyobject_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    isIndoor:    
      description: 'Flag to indicate if the entity is installed indoor or outdoor.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isPersonalData:    
      description: 'Flag to indicate if the entity is providing or contains personal data.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    legitimateInterest:    
      description: 'Legitimate interest associated to the entity. This means for which high-level finality the data collection is made.'    
      type: string    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *privacyobject_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    purpose:    
      description: 'Purpose of the data gathering.'    
      type: string    
      x-ngsi:    
        type: Property    
    recipientList:    
      description: 'List containing the recipients. A recipient is the beneficiary using the data generated by a sensor. Each recipient is represented by an URI which allows its unique identification. Privacy:''Low'''    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Relationship. Device linked to this PrivacyObject entity. Model:''https://schema.org/URL'''    
          format: uri    
          type: string    
      description: 'Unique identifier from the source data set.'    
      x-ngsi:    
        type: Property    
    retentionPeriod:    
      description: 'Period of data retention.'    
      type: string    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type property. It has to be PrivacyObject.'    
      enum:    
        - PrivacyObject    
      type: string    
      x-ngsi:    
        type: Property    
    user:    
      description: 'Identifier of an anonymous user. This identifier is in fact a unique URN which can be used to recognize anonymously a user.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PrivacyObject/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/PrivacyObject/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### PrivacyObject NGSI-v2 关键值示例  
这里有一个JSON-LD格式的PrivacyObject作为key-values的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
  "type": "PrivacyObject",  
  "refDevice": "Device:1044_parking",  
  "name": "1004_parking",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      46.18311,  
      6.14132  
    ]  
  },  
  "isIndoor": false,  
  "floor": 0,  
  "description": "Electromagnetic and ultrasonic sensor",  
  "description_fr": "Capteur électromagnétique et à ultrasons",  
  "user": "urn:ngsi-ld:User:abcdef",  
  "purpose": "Detecting the presence of a vehicle on a parking slot.",  
  "purpose_fr": "Détecter la présence d'un véhicule sur une place de parc.",  
  "category": [  
    "sensor"  
  ],  
  "recipientList": [  
    "urn:ngsi-ld:User:CommunalAdministration",  
    "urn:ngsi-ld:User:Motorists"  
  ],  
  "owner": [  
    "ngsi-ld:city:CityofCarouge"  
  ],  
  "isPersonalData": false,  
  "retentionPeriod": "< 1 month",  
  "legitimateInterest": "Facilitate and understand parking habits",  
  "crossborderTransfer": "None",  
  "image": "http://www.example.com/device1.jpg"  
}  
```  
</details>  
#### PrivacyObject NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的PrivacyObject的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
  "type": "PrivacyObject",  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:1044_parking"  
  },  
  "name": {  
    "type": "Text",  
    "value": "1004_parking"  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        46.18311,  
        6.14132  
      ]  
    }  
  },  
  "isIndoor": {  
    "type": "Text",  
    "value": "false"  
  },  
  "floor": {  
    "type": "Text",  
    "value": "false"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Electromagnetic and ultrasonic sensor"  
  },  
  "description_fr": {  
    "type": "Text",  
    "value": "Capteur électromagnétique et à ultrasons"  
  },  
  "user": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:User:abcdef"  
  },  
  "purpose": {  
    "type": "Text",  
    "value": "Detecting the presence of a vehicle on a parking slot."  
  },  
  "purpose_fr": {  
    "type": "string",  
    "value": "Détecter la présence d'un véhicule sur une place de parc."  
  },  
  "category": {  
    "type": "array",  
    "value": [  
      "sensor"  
    ]  
  },  
  "recipientList": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:User:CommunalAdministration",  
      "urn:ngsi-ld:User:Motorists"  
    ]  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "ngsi-ld:city:CityofCarouge"  
    ]  
  },  
  "isPersonalData": {  
    "type": "Text",  
    "value": "false"  
  },  
  "retentionPeriod": {  
    "type": "Text",  
    "value": "< 1 month"  
  },  
  "legitimateInterest": {  
    "type": "Text",  
    "value": "Facilitate and understand parking habits"  
  },  
  "crossborderTransfer": {  
    "type": "Text",  
    "value": "None"  
  },  
  "image": {  
    "type": "Text",  
    "value": "http://www.example.com/device1.jpg"  
  }  
}  
```  
</details>  
#### PrivacyObject NGSI-LD关键值示例  
这里有一个JSON-LD格式的PrivacyObject作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
    "type": "PrivacyObject",  
    "category": [  
        "sensor"  
    ],  
    "crossborderTransfer": "None",  
    "description": "Electromagnetic and ultrasonic sensor",  
    "description_fr": "Capteur electromagnetique et ultrasons",  
    "floor": 0,  
    "image": "http://www.example.com/device1.jpg",  
    "isIndoor": false,  
    "isPersonalData": false,  
    "legitimateInterest": "Facilitate and understand parking habits",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            46.18311,  
            6.14132  
        ]  
    },  
    "name": "1004_parking",  
    "owner": [  
        "ngsi-ld:city:CityofCarouge"  
    ],  
    "purpose": "Detecting the presence of a vehicle on a parking slot.",  
    "purpose_fr": "Detecter la presence d'un vehicule sur une place de parc.",  
    "recipientList": [  
        "urn:ngsi-ld:User:CommunalAdministration",  
        "urn:ngsi-ld:User:Motorists"  
    ],  
    "refDevice": "Device:1044_parking",  
    "retentionPeriod": "< 1 month",  
    "user": "urn:ngsi-ld:User:abcdef",  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PrivacyObject NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的PrivacyObject的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
    "type": "PrivacyObject",  
    "category": {  
        "type": "Property",  
        "value": [  
            "sensor"  
        ]  
    },  
    "crossborderTransfer": {  
        "type": "Property",  
        "value": "None"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Electromagnetic and ultrasonic sensor"  
    },  
    "description_fr": {  
        "type": "Property",  
        "value": "Capteur electromagnetique et ultrasons"  
    },  
    "floor": {  
        "type": "Property",  
        "value": "false"  
    },  
    "image": {  
        "type": "Property",  
        "value": "http://www.example.com/device1.jpg"  
    },  
    "isIndoor": {  
        "type": "Property",  
        "value": "false"  
    },  
    "isPersonalData": {  
        "type": "Property",  
        "value": "false"  
    },  
    "legitimateInterest": {  
        "type": "Property",  
        "value": "Facilitate and understand parking habits"  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                46.18311,  
                6.14132  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "1004_parking"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "ngsi-ld:city:CityofCarouge"  
        ]  
    },  
    "purpose": {  
        "type": "Property",  
        "value": "Detecting the presence of a vehicle on a parking slot."  
    },  
    "purpose_fr": {  
        "type": "string",  
        "value": "Detecter la presence d'un vehicule sur une place de parc."  
    },  
    "recipientList": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:User:CommunalAdministration",  
            "urn:ngsi-ld:User:Motorists"  
        ]  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "value": "Device:1044_parking"  
    },  
    "retentionPeriod": {  
        "type": "Property",  
        "value": "< 1 month"  
    },  
    "user": {  
        "type": "Property",  
        "value": "urn:ngsi-ld:User:abcdef"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
