# Behave test #

## Bugs on factorial calculator ##

Go to [BUGS.md](https://github.com/lkrust/panda/blob/main/BUGS.md)

# How to install: #

To ease out installation and better manage packages, I decided to use pipenv. To install it [follow steps on their documentation](https://pipenv.pypa.io/en/latest/).


#### Install depedencies ####
    $ pipenv install

#### Start the new virtualenv ####
    $ pipenv shell

#### Installing allure shell ####
To install [follow steps on their documentation](https://docs.qameta.io/allure-report/#_installation_6)

### Running tests ###

To run all scenarios:

    $ pipenv run tests

To run api scenarios:

    $ pipenv run api

To run ui scenarios:

    $ pipenv run ui


### Checking the report ###
I am using allure to generate the report. After the test have finished executing, run:

    $ pipenv run report
