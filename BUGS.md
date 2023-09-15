# Bugs found #

## API ##

### No validation for number higher or equal than 992

#### Steps to reproduce
```
1. Make a request with ‘number=992’ payload

Actual result
500
Expected result
	Status code: 400 or 200
Error message: 
400: Explanation why 992 is the limit
200: Make the calculation
```

### No validation for strings

#### Steps to reproduce
```
1. Make a request with ‘number=test payload

Actual result
500
Expected result
	Status code: 400
Error message: Explanation why strings are not valid
```

### No validation for negative numbers

#### Steps to reproduce
```
1. Make a request with ‘number=-1 payload

Actual result
500
Expected result
	Status code: 400
Error message: Explanation why negative numbers are not valid
```

### Changing content-type

#### Steps to reproduce
```
1. Change content-type any other thing than ‘application/x-www-form-urlencoded; charset=UTF-8’
2. Make a request with ‘number=2’ payload

Actual result
500
Expected result
	Status code: 415
Error message: “Unsupported Media Type client”
```

### Invalid Payload

#### Steps to reproduce
```
1. Make a request with ‘number=’ payload

Actual result
500
Expected result
	Status code: 400
Error message: “Bad request”
```
—
## UI ##

### Terms and conditions and privacy links are swapped

#### Steps to reproduce
```
1. Clicking on privacy we get the terms and conditions message
2. Clicking on terms and conditions we get the privacy message

Expected result
	Privacy should point to privacy message, terms should point to terms message
```

### No validation for negative numbers

#### Steps to reproduce
```
1. Type “-1” on input
2. click calculate

Actual result
Nothing happens
Expected result
	An error message explaining negative numbers are not valid input appears(or use API response)
```

### No validation for number higher or equal than 992

#### Steps to reproduce
```
1. Type “992” on input
2. click calculate

Actual result
Nothing happens
Expected result
	An error message explaining why 992 or higher is not valid input (or use API response)
```
