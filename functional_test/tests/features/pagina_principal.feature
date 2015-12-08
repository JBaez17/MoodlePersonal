Feature: Como alumno
  Quiero ver el menu principal
  para realizar consultas 
  o realizar examenes

  Scenario: Verificar que se muestra el menu principal para el alumno sam
	Given Que ingreso a la pagina de login con el usuario "sam", contraseña "sam"
	Cuando se muestra la pantalla principal
	Entonces Puedo ver las diferentes opciones

  Scenario: Verificar que se muestra el menu principal para el alumno Alberto
	Given Que ingreso a la pagina de login con el usuario "Alberto", contraseña "beto"
	Cuando se muestra la pantalla principal
	Entonces Puedo ver las diferentes opciones

  Scenario: Verificar que se muestra el menu principal para el alumno Sarah
	Given Que ingreso a la pagina de login con el usuario "Sarah", contraseña "sari"
	Cuando se muestra la pantalla principal
	Entonces Puedo ver las diferentes opciones