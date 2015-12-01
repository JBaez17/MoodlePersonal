Feature: Como programador del proyecto
		quiero ver la pagina de inicio de django
		para poder saber que la instalacion fue exitosa

Scenario: Verificar la instalacion de django
	Given Que ingreso en el navegador la url "http://127.0.0.1:8000" en la barra de direcciones
	When Oprimo la tecla Enter 
	Then Puedo ver en el titulo del navegador la palabra "Django".
