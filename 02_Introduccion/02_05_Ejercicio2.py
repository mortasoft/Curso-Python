
salario = 256000

porcentajeBanco = 0.01
invalidez_vejez_muerte = 0.0284
enfermedad_maternidad = 0.0550

enfermedad_patrono = 0.0925
invalidez_patrono = 0.0508
popular_patrono = 0.0050
fodesaf = 0.05
fcl = 0.03
pension_complementaria = 0.015

print(f"Salario Bruto: {salario}")
print(f"Porcentaje de Banco Popular: ${porcentajeBanco*salario}" )
print(f"Invalidez Vejez y Muerte Obrero: ${invalidez_vejez_muerte*salario}" )
print(f"Seguro de Enfermedad y Maternidad Obr: ${enfermedad_maternidad*salario}" )
print(f"Seguro de Enfermedad y Maternidad Patrono: ${enfermedad_patrono*salario}" )
print(f"Invalidez Vejez y Muerte Patrono: ${invalidez_patrono*salario}" )
print(f"Banco Popular Patrono: ${popular_patrono*salario}" )
print(f"Fondo de Desarrollo de Asignaciones Familiares: ${fodesaf*salario}" )
print(f"Fondo de Capitalización Laboral: ${fcl*salario}" )
print(f"Régimen Obligatorio de Pensión Complementaria: ${pension_complementaria*salario}" )

deducciones = (porcentajeBanco+invalidez_vejez_muerte+enfermedad_maternidad+enfermedad_patrono+invalidez_patrono+popular_patrono+fodesaf+fcl+pension_complementaria)*salario
print(f"Deducciones: {deducciones}")
print(f"Salario Neto: {salario-deducciones}")º11111111111111111111111111111111111111111111111