# behaveTestExample

## Set up

In order to execute this tests you need to place your driver executables
`chromedriver.exe` and `geckodriver.exe` on the `drivers/` folder

Some of this project's functions need to run on `Python 3.10` or later versions

Also, you need `Behave`, `Selenium` and `allure-behave` libraries. they are contained on `requirements.txt` file.

In your system you will need to compile the allure report. for that you need `allure`
https://docs.qameta.io/allure/

## test execution

`behave -f allure_behave.formatter:AllureFormatter -o ./reports ./features`

## report serving

`allure serve .\reports\`
