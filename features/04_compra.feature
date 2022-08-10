Feature: compra exitosa

    As a common user
    I want to pourchase a product
    In order to validtae successfull compra

    Scenario: Generar una compra exitosa
        Given the user is on inventory page
        And el usuario tiene un producto en el carrito
        When el usuario completa la compra
        Then se muestra el mensaje de compra exitosa
