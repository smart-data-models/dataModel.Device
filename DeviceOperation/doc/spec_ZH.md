<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。设备操作（DeviceOperation  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceOperation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体包含一个通用设备操作实体的统一描述。设备操作实体包含设备报告的动态数据，因此适用于所有物联网部分和相关的物联网应用**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `addressedAt[string]`: 事件或故障被处理或清除的时间戳。  - `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `device[*]`: 对该设备操作的相关设备的引用。  - `endedAt[string]`: 操作实际完成时的时间戳。  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `operationType[string]`: 从一个列举的列表中选择  . Model: [event, maintenance, fault, installation, upgrade, other](event, maintenance, fault, installation, upgrade, other)- `operator[*]`: 指进行操作的操作员  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `plannedEndAt[string]`: 该操作的计划结束日期/时间戳。请注意，这是一个建议，操作完成的实际时间可能在计划结束之前或之后。  - `plannedStartAt[string]`: 该操作的计划开始日期/时间戳。请注意，这是建议性的，操作开始的实际时间可能在计划开始之前或之后。  - `reportedAt[string]`: 报告该事件/故障的时间戳。  - `result[string]`: 操作的结果。Enum:'ok, aborted, failed'。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `startedAt[string]`: 操作实际开始执行的时间戳。  - `status[string]`: 从描述状态的枚举列表中的一个选择。枚举：'计划中的、正在进行的、已完成的、预定的、取消的'。  - `type[string]`: NGSI实体标识符。它必须是DeviceOperation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
设备是一个有形的物体，它包含一些逻辑，是数据的生产者和/或消费者。一个设备总是被认为能够通过网络进行电子通信。这个数据模型部分是与移动运营商和[GSMA](https://www.gsma.com/iot/iot-big-data/)合作开发的。这个数据模型重用了来自[ETSI](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf)标准的[SAREF Ontology](http://www.etsi.org)部分的概念。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceOperation:    
  description: 'This entity contains a harmonised description of a generic device operation entity. The device operation entity contains dynamic data reported by a device and is therefore applicable to all IoT segments and related IoT applications.'    
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
    addressedAt:    
      description: 'The timestamp when an event or fault was addressed or cleared.'    
      format: date-time    
      type: string    
      x-ngsi:    
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
    device:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the associated Device for this device operation.'    
      x-ngsi:    
        type: Relationship    
    endedAt:    
      description: 'Timestamp when the operation actually finished.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &deviceoperation_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'A choice from an enumerated list'    
      enum:    
        - event    
        - fault    
        - installation    
        - maintenance    
        - other    
        - upgrade    
      type: string    
      x-ngsi:    
        model: 'event, maintenance, fault, installation, upgrade, other'    
        type: Property    
    operator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the operator conducting the operation'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *deviceoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plannedEndAt:    
      description: 'The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    plannedStartAt:    
      description: 'The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    reportedAt:    
      description: 'Timestamp when the event/ fault was reported.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    result:    
      description: 'The result of the operation. Enum:''ok, aborted, failed'''    
      enum:    
        - aborted    
        - failed    
        - ok    
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
    startedAt:    
      description: 'Timestamp when the operation actually started to be performed.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''    
      enum:    
        - cancelled    
        - finished    
        - ongoing    
        - planned    
        - scheduled    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be DeviceOperation'    
      enum:    
        - DeviceOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/DeviceOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/DeviceOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### DeviceOperation NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的DeviceOperation的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "operationType": "fault",  
  "description": "Backup battery needs replacement",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "ongoing",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "addressedAt": "2016-08-28T10:18:16Z"  
}  
```  
</details>  
#### DeviceOperation NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的DeviceOperation的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "device": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "fault"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Backup battery needs replacement"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "ongoing"  
  },  
  "operator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "addressedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  }  
}  
```  
</details>  
#### DeviceOperation NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为key-values的DeviceOperation的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
    "type": "DeviceOperation",  
    "addressedAt": "2016-08-28T10:18:16Z",  
    "dataProvider": "https://provider.example.com",  
    "description": "Backup battery needs replacement",  
    "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
    "endedAt": "2016-08-28T10:18:16Z",  
    "operationType": "fault",  
    "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
    "plannedEndAt": "2016-08-28T10:18:16Z",  
    "plannedStartAt": "2016-08-22T10:18:16Z",  
    "reportedAt": "2016-08-28T10:18:16Z",  
    "result": "ok",  
    "source": "https://source.example.com",  
    "startedAt": "2016-08-22T10:18:16Z",  
    "status": "ongoing",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Device/DeviceOperation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 设备操作NGSI-LD正常化的例子  
下面是一个规范化的JSON-LD格式的DeviceOperation的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
    "type": "DeviceOperation",  
    "addressedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-28T10:18:16Z"  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Backup battery needs replacement"  
    },  
    "device": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-28T10:18:16Z"  
        }  
    },  
    "operationType": {  
        "type": "Property",  
        "value": "fault"  
    },  
    "operator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
    },  
    "plannedEndAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-28T10:18:16Z"  
        }  
    },  
    "plannedStartAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "reportedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-28T10:18:16Z"  
        }  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "startedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "status": {  
        "type": "Property",  
        "value": "ongoing"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Device/DeviceOperation/context.jsonld",  
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
