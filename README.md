# Introduction

Nepali Municipalities  was built from the  with  JSON API that makes it easy for developers and basically during Kyc Form fill up by user.

These docs describe how to use the [Nepali Municpalities](https://nepali-municipalities.herokuapp.com/api/docs/) API. We hope you enjoy these docs, and please don't hesitate to [file an issue](https://github.com/nawarazpokhrel/nepali_municipalities) if you see anything missing and 
if you want any endpoints to be added I am very open to new ideas from you.

This api uses technology of django-restframework along with postgres database

## Use Cases

There are many reasons to use the Nepali Municipalitis API. There are many cases when kyc or user form fill is tedious job as user don't want to fill all address form.
If we have key i.e municipalities can provide all info about certain place we can autocomplete rest of necessary detiails from database i.e District and Pradesh.
## Authorization

As of now This api is completely free and will be free of cost as I love open source API.



```http
GET /api/municipalities/all/list
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `api_key` | `string` | **Required**. Your Gophish API key |

## Responses

This API endpoints return the JSON representation of the list. I have included pagination default pagiation  shows 50 results.
```
{
      "id": 1,
      "name": "Bhojpur",
      "district": "Bhojpur",
      "province": "Province 1",
      "country": "Nepal"
    },
```

The id is basically integer field.
The name is basically charcter field which gives name of municipalities.
The district is char field which gives name of  municipalites associated with it.
The province is char field which gives name of  province  associated with district.

## Status Codes

Nepali municipalites  returns the only  single status codes in its API however following are general api status codes:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |
