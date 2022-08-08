# cvs-api

__cvs-api__ is a Flask RESTful api for extracting store data from FamilyMart in Taiwan, a chain convenience store brand. 

__Data source__: FamilyMart official website.

__API available time__: 8:40 am to 9:30 am on every Saturday. (GMT+8)

__Resources__:
  - Get stores by store name
  - Get stores in a given city
  - Count number of stores in each city in Taiwan
  - Count number of stores in each district(town) in a given city
 
## Usage

- Get stores by store name
  - Request url:　`https://cvs-api-tw.herokuapp.com/fm_byname/<store_name>`
  - Return values: `extracted date`, `input name` and store information. Store information includes `store_name`, `address`, `longitude` and `latitude`. 
  - Return example:
    ```
    {
      "extract_date": "2022-01-01",
      "input_name": "馬祖",
      "store" : [
        "store_name": "全家馬祖福澳店",
        "address": "連江縣南竿鄉福澳村１３５號１樓",
        "longitude": "119.94068100",
        "latitude": "26.16091900"
      ]
    }
    ```
- Get stores in a given city
  - Request url:　`https://cvs-api-tw.herokuapp.com/fm_bycity/<city_name>`
  - Return values: `extracted date`, `input_city` and store information. Store information includes `store_name`, `address`, `longitude` and `latitude`. 
  - Return example:
    ```
    {
      "extract_date": "2022-01-01",
      "input_city": "雲林",
      "store" : [
        "store_name": "全家斗南林子店",
        "address": "雲林縣斗南鎮林子里林子２０１號１３５號１樓",
        "longitude": "120.48419595",
        "latitude": "23.65480786"
      ]
    }
    ```
- Count number of stores in each city in Taiwan.
  - Request url:　`https://cvs-api-tw.herokuapp.com/fm_stores`
  - Return values: `extracted date` and `store_counts` 
  - Return example:
    ```
    {
      "extract_date": "2022-08-06",
      "store_counts": {
          "新北市": 891,
          "台北市": 596,
          "台中市": 568,
          "桃園市": 376,
          "高雄市": 351,
          "台南市": 245,
          ...
    }
    ```
- Count number of stores in each district in a given city.
  - Request url:　`https://cvs-api-tw.herokuapp.com/fm_stores/<city_name>`
  - Return values: `extracted date`, `input_city` and `store_counts` 
  - Return example:
    ```
    {
      "extract_date": "2022-08-06",
      "input_city": "雲林",
      "store_counts": {
          "雲林縣斗六市": 22,
          "雲林縣虎尾鎮": 14,
          "雲林縣麥寮鄉": 8,
          "雲林縣斗南鎮": 7,
          ...
    }
    ```
