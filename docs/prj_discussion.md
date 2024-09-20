# CinemaTicket Test Project

### Contributor: Sajad tohidi majd

---

### Swagger Endpoint: `/swagger/` , `/redoc/`

## Applications

### all core applications are located in side `core_apps` directory.

### 1 - `account`

-  ### This app basically holds all user related functionality
-  ### APIS
    - `/account/api/v1/login/`
    - `/account/api/v1/register/`
    - `/account/api/v1/refresh/`

### 2 - `common`

-  ### This app holds common models and managers (can be used to hold more common stuff)

### 3 - `payment`

-  ### This app handles transactions
-  ### APIS
    - `/payment/api/v1/buy-ticket/`
    - `/payment/api/v1/gateways-list/`
    - `/payment/api/v1/purchase-detail/<transaction_id>/`
    - `/payment/api/v1/purchase-callback/`

### 4 - `redis_app`

- ### This app holds generic class and functionality to interact with redisDB

### 5 - `venue`

-  ### This app handles transactions
-  ### APIS
    - `/venue/api/v1/stadium/`
    - `/venue/api/v1/stadium/<stadium_id>/`
    - `/venue/api/v1/match/`
    - `/venue/api/v1/match/<match_id>/`
    - `/venue/api/v1/match/<match_id>/ticket-list/`
