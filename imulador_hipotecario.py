def simular_credito():
    # Tus datos
    prestamo_solicitado_usd = 120000
    sueldo_neto = 3157380
    
    # Cuántas veces entra el bloque de 10.000 dólares en lo que pedís (12 veces)
    multiplicador = prestamo_solicitado_usd / 10000

    # Base de datos extraída de las imágenes
    bancos = [
        {
            "nombre": "Banco de Neuquén", "tasa_uva": "3,5%/8,5% clientes / 4,5%/9,5% no clientes",
            "plazo_max": "20 años", "monto_max": "75 millones / 150 millones", "cuota_ingreso": "30%", "financiamiento": "80%",
            "cuota_10k": 81194, "ingreso_min_10k": 270648
        },
        {
            "nombre": "Banco de Rosario", "tasa_uva": "4,20%",
            "plazo_max": "20 años", "monto_max": "$100 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 86320, "ingreso_min_10k": 345280
        },
        {
            "nombre": "Banco Nación", "tasa_uva": "6,00% (12,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "260.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 83937, "ingreso_min_10k": 335748
        },
        {
            "nombre": "ICBC", "tasa_uva": "6,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "$360 millones", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 107703, "ingreso_min_10k": 430812
        },
        {
            "nombre": "BBVA", "tasa_uva": "7,50% (17,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 97890, "ingreso_min_10k": 391560
        },
        {
            "nombre": "Banco de Córdoba", "tasa_uva": "8,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "250.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 125063, "ingreso_min_10k": 500251
        },
        {
            "nombre": "Banco Del Sol", "tasa_uva": "9,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 125962, "ingreso_min_10k": 503847
        },
        {
            "nombre": "Santander", "tasa_uva": "9,50%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        },
        {
            "nombre": "Grupo Petersen", "tasa_uva": "9,90%",
            "plazo_max": "20 años", "monto_max": "315.184 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 134177, "ingreso_min_10k": 536707
        },
        {
            "nombre": "Banco de Chubut", "tasa_uva": "10,00%",
            "plazo_max": "15 años", "monto_max": "180 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 150445, "ingreso_min_10k": 601779
        },
        {
            "nombre": "Comafi", "tasa_uva": "10,50% (12,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "350 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 139773, "ingreso_min_10k": 559093
        },
        {
            "nombre": "Macro (en US$)", "tasa_uva": "11,5% (exclusivo Macro Selecta)",
            "plazo_max": "5 años", "monto_max": "Hasta US$ 1 millón", "cuota_ingreso": "25%", "financiamiento": "50%",
            "cuota_10k": 196834, "ingreso_min_10k": 787334
        },
        {
            "nombre": "Brubank", "tasa_uva": "12,00% (14,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "250 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 144006, "ingreso_min_10k": 576023
        },
        {
            "nombre": "Banco de Corrientes", "tasa_uva": "12,00%",
            "plazo_max": "20 años", "monto_max": "No informa", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 154152, "ingreso_min_10k": 616608
        },
        {
            "nombre": "Credicoop", "tasa_uva": "12,50% (13,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "200 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 159060, "ingreso_min_10k": 636239
        },
        {
            "nombre": "Patagonia", "tasa_uva": "12,50%",
            "plazo_max": "30 años", "monto_max": "120 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 149416, "ingreso_min_10k": 597664
        },
        {
            "nombre": "Banco Hipotecario", "tasa_uva": "12,50%",
            "plazo_max": "15 años", "monto_max": "$250 millones", "cuota_ingreso": "20%", "financiamiento": "80%",
            "cuota_10k": 172553, "ingreso_min_10k": 862765
        },
        {
            "nombre": "Supervielle", "tasa_uva": "15,00%",
            "plazo_max": "15 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "65%",
            "cuota_10k": 195942, "ingreso_min_10k": 783769
        },
        {
            "nombre": "Macro", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Hasta $350 millones", "cuota_ingreso": "25%", "financiamiento": "70% < 350 mill / 60% > 350 mill",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Galicia", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Banco Provincia (no UVA)", "tasa_uva": "39,20%",
            "plazo_max": "20 años / No clientes 15", "monto_max": "351.250 millones (eq. US$ 250.000)", "cuota_ingreso": "40%", "financiamiento": "80%",
            "cuota_10k": 457189, "ingreso_min_10k": 1142971
        },
        {
            "nombre": "Banco Ciudad", "tasa_uva": "9,5% general / 8,5% microcentro / 7,5% 1ra vivienda",
            "plazo_max": "20 años", "monto_max": "$350 millones / $100 millones para 1ra vivienda", "cuota_ingreso": "25%", "financiamiento": "70% / 75% 1ra vivienda",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        }
    ]

    print(f"Simulando pedido de USD {prestamo_solicitado_usd} con un sueldo neto de ${sueldo_neto}\n")
    print("-" * 50)

    for banco in bancos:
        # Calculamos los valores totales
        cuota_total = banco["cuota_10k"] * multiplicador
        ingreso_requerido = banco["ingreso_min_10k"] * multiplicador
        
        print(f"BANCO: {banco['nombre']}")
        print(f"Tasa (UVA+): {banco['tasa_uva']} | Plazo Máx: {banco['plazo_max']}")
        print(f"Monto Máximo: {banco['monto_max']} | Financiamiento: {banco['financiamiento']}")
        print(f"Relación Cuota/Ingreso exigida: {banco['cuota_ingreso']}")
        print(f"Cuota mensual calculada: ${cuota_total:,.2f}")
        print(f"Ingreso mínimo que te piden: ${ingreso_requerido:,.2f}")
        
        # Evaluación directa
        if sueldo_neto >= ingreso_requerido:
            print("ESTADO: APROBADO")
            print("Justificación: Tu sueldo supera el mínimo requerido. La cuota no excede el porcentaje máximo permitido de tus ingresos.")
        else:
            print("ESTADO: RECHAZADO")
            print(f"Justificación: Te faltan ${ingreso_requerido - sueldo_neto:,.2f} de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del {banco['cuota_ingreso']} del sueldo.")
        print("-" * 50)

simular_credito()
print("\n" + " " * 15 + "✨ Yamy la mejor ❤️ ✨")
def simular_credito():
    # Tus datos
    prestamo_solicitado_usd = 120000
    sueldo_neto = 3157380
    
    # Cuántas veces entra el bloque de 10.000 dólares en lo que pedís (12 veces)
    multiplicador = prestamo_solicitado_usd / 10000

    # Base de datos extraída de las imágenes
    bancos = [
        {
            "nombre": "Banco de Neuquén", "tasa_uva": "3,5%/8,5% clientes / 4,5%/9,5% no clientes",
            "plazo_max": "20 años", "monto_max": "75 millones / 150 millones", "cuota_ingreso": "30%", "financiamiento": "80%",
            "cuota_10k": 81194, "ingreso_min_10k": 270648
        },
        {
            "nombre": "Banco de Rosario", "tasa_uva": "4,20%",
            "plazo_max": "20 años", "monto_max": "$100 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 86320, "ingreso_min_10k": 345280
        },
        {
            "nombre": "Banco Nación", "tasa_uva": "6,00% (12,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "260.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 83937, "ingreso_min_10k": 335748
        },
        {
            "nombre": "ICBC", "tasa_uva": "6,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "$360 millones", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 107703, "ingreso_min_10k": 430812
        },
        {
            "nombre": "BBVA", "tasa_uva": "7,50% (17,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 97890, "ingreso_min_10k": 391560
        },
        {
            "nombre": "Banco de Córdoba", "tasa_uva": "8,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "250.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 125063, "ingreso_min_10k": 500251
        },
        {
            "nombre": "Banco Del Sol", "tasa_uva": "9,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 125962, "ingreso_min_10k": 503847
        },
        {
            "nombre": "Santander", "tasa_uva": "9,50%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        },
        {
            "nombre": "Grupo Petersen", "tasa_uva": "9,90%",
            "plazo_max": "20 años", "monto_max": "315.184 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 134177, "ingreso_min_10k": 536707
        },
        {
            "nombre": "Banco de Chubut", "tasa_uva": "10,00%",
            "plazo_max": "15 años", "monto_max": "180 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 150445, "ingreso_min_10k": 601779
        },
        {
            "nombre": "Comafi", "tasa_uva": "10,50% (12,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "350 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 139773, "ingreso_min_10k": 559093
        },
        {
            "nombre": "Macro (en US$)", "tasa_uva": "11,5% (exclusivo Macro Selecta)",
            "plazo_max": "5 años", "monto_max": "Hasta US$ 1 millón", "cuota_ingreso": "25%", "financiamiento": "50%",
            "cuota_10k": 196834, "ingreso_min_10k": 787334
        },
        {
            "nombre": "Brubank", "tasa_uva": "12,00% (14,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "250 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 144006, "ingreso_min_10k": 576023
        },
        {
            "nombre": "Banco de Corrientes", "tasa_uva": "12,00%",
            "plazo_max": "20 años", "monto_max": "No informa", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 154152, "ingreso_min_10k": 616608
        },
        {
            "nombre": "Credicoop", "tasa_uva": "12,50% (13,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "200 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 159060, "ingreso_min_10k": 636239
        },
        {
            "nombre": "Patagonia", "tasa_uva": "12,50%",
            "plazo_max": "30 años", "monto_max": "120 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 149416, "ingreso_min_10k": 597664
        },
        {
            "nombre": "Banco Hipotecario", "tasa_uva": "12,50%",
            "plazo_max": "15 años", "monto_max": "$250 millones", "cuota_ingreso": "20%", "financiamiento": "80%",
            "cuota_10k": 172553, "ingreso_min_10k": 862765
        },
        {
            "nombre": "Supervielle", "tasa_uva": "15,00%",
            "plazo_max": "15 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "65%",
            "cuota_10k": 195942, "ingreso_min_10k": 783769
        },
        {
            "nombre": "Macro", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Hasta $350 millones", "cuota_ingreso": "25%", "financiamiento": "70% < 350 mill / 60% > 350 mill",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Galicia", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Banco Provincia (no UVA)", "tasa_uva": "39,20%",
            "plazo_max": "20 años / No clientes 15", "monto_max": "351.250 millones (eq. US$ 250.000)", "cuota_ingreso": "40%", "financiamiento": "80%",
            "cuota_10k": 457189, "ingreso_min_10k": 1142971
        },
        {
            "nombre": "Banco Ciudad", "tasa_uva": "9,5% general / 8,5% microcentro / 7,5% 1ra vivienda",
            "plazo_max": "20 años", "monto_max": "$350 millones / $100 millones para 1ra vivienda", "cuota_ingreso": "25%", "financiamiento": "70% / 75% 1ra vivienda",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        }
    ]

    print(f"Simulando pedido de USD {prestamo_solicitado_usd} con un sueldo neto de ${sueldo_neto}\n")
    print("-" * 50)

    for banco in bancos:
        # Calculamos los valores totales
        cuota_total = banco["cuota_10k"] * multiplicador
        ingreso_requerido = banco["ingreso_min_10k"] * multiplicador
        
        print(f"BANCO: {banco['nombre']}")
        print(f"Tasa (UVA+): {banco['tasa_uva']} | Plazo Máx: {banco['plazo_max']}")
        print(f"Monto Máximo: {banco['monto_max']} | Financiamiento: {banco['financiamiento']}")
        print(f"Relación Cuota/Ingreso exigida: {banco['cuota_ingreso']}")
        print(f"Cuota mensual calculada: ${cuota_total:,.2f}")
        print(f"Ingreso mínimo que te piden: ${ingreso_requerido:,.2f}")
        
        # Evaluación directa
        if sueldo_neto >= ingreso_requerido:
            print("ESTADO: APROBADO")
            print("Justificación: Tu sueldo supera el mínimo requerido. La cuota no excede el porcentaje máximo permitido de tus ingresos.")
        else:
            print("ESTADO: RECHAZADO")
            print(f"Justificación: Te faltan ${ingreso_requerido - sueldo_neto:,.2f} de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del {banco['cuota_ingreso']} del sueldo.")
        print("-" * 50)

simular_credito()
print("\n" + " " * 15 + "✨ Yamy la mejor ❤️ ✨")def simular_credito():
    # Tus datos
    prestamo_solicitado_usd = 120000
    sueldo_neto = 3157380
    
    # Cuántas veces entra el bloque de 10.000 dólares en lo que pedís (12 veces)
    multiplicador = prestamo_solicitado_usd / 10000

    # Base de datos extraída de las imágenes
    bancos = [
        {
            "nombre": "Banco de Neuquén", "tasa_uva": "3,5%/8,5% clientes / 4,5%/9,5% no clientes",
            "plazo_max": "20 años", "monto_max": "75 millones / 150 millones", "cuota_ingreso": "30%", "financiamiento": "80%",
            "cuota_10k": 81194, "ingreso_min_10k": 270648
        },
        {
            "nombre": "Banco de Rosario", "tasa_uva": "4,20%",
            "plazo_max": "20 años", "monto_max": "$100 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 86320, "ingreso_min_10k": 345280
        },
        {
            "nombre": "Banco Nación", "tasa_uva": "6,00% (12,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "260.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 83937, "ingreso_min_10k": 335748
        },
        {
            "nombre": "ICBC", "tasa_uva": "6,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "$360 millones", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 107703, "ingreso_min_10k": 430812
        },
        {
            "nombre": "BBVA", "tasa_uva": "7,50% (17,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 97890, "ingreso_min_10k": 391560
        },
        {
            "nombre": "Banco de Córdoba", "tasa_uva": "8,90% (9,90% No clientes)",
            "plazo_max": "20 años", "monto_max": "250.000 UVAs", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 125063, "ingreso_min_10k": 500251
        },
        {
            "nombre": "Banco Del Sol", "tasa_uva": "9,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 125962, "ingreso_min_10k": 503847
        },
        {
            "nombre": "Santander", "tasa_uva": "9,50%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        },
        {
            "nombre": "Grupo Petersen", "tasa_uva": "9,90%",
            "plazo_max": "20 años", "monto_max": "315.184 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 134177, "ingreso_min_10k": 536707
        },
        {
            "nombre": "Banco de Chubut", "tasa_uva": "10,00%",
            "plazo_max": "15 años", "monto_max": "180 millones", "cuota_ingreso": "30%", "financiamiento": "75%",
            "cuota_10k": 150445, "ingreso_min_10k": 601779
        },
        {
            "nombre": "Comafi", "tasa_uva": "10,50% (12,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "350 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 139773, "ingreso_min_10k": 559093
        },
        {
            "nombre": "Macro (en US$)", "tasa_uva": "11,5% (exclusivo Macro Selecta)",
            "plazo_max": "5 años", "monto_max": "Hasta US$ 1 millón", "cuota_ingreso": "25%", "financiamiento": "50%",
            "cuota_10k": 196834, "ingreso_min_10k": 787334
        },
        {
            "nombre": "Brubank", "tasa_uva": "12,00% (14,00% No clientes)",
            "plazo_max": "30 años", "monto_max": "250 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 144006, "ingreso_min_10k": 576023
        },
        {
            "nombre": "Banco de Corrientes", "tasa_uva": "12,00%",
            "plazo_max": "20 años", "monto_max": "No informa", "cuota_ingreso": "25%", "financiamiento": "80%",
            "cuota_10k": 154152, "ingreso_min_10k": 616608
        },
        {
            "nombre": "Credicoop", "tasa_uva": "12,50% (13,50% No clientes)",
            "plazo_max": "20 años", "monto_max": "200 millones", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 159060, "ingreso_min_10k": 636239
        },
        {
            "nombre": "Patagonia", "tasa_uva": "12,50%",
            "plazo_max": "30 años", "monto_max": "120 millones", "cuota_ingreso": "25%", "financiamiento": "75%",
            "cuota_10k": 149416, "ingreso_min_10k": 597664
        },
        {
            "nombre": "Banco Hipotecario", "tasa_uva": "12,50%",
            "plazo_max": "15 años", "monto_max": "$250 millones", "cuota_ingreso": "20%", "financiamiento": "80%",
            "cuota_10k": 172553, "ingreso_min_10k": 862765
        },
        {
            "nombre": "Supervielle", "tasa_uva": "15,00%",
            "plazo_max": "15 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "65%",
            "cuota_10k": 195942, "ingreso_min_10k": 783769
        },
        {
            "nombre": "Macro", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Hasta $350 millones", "cuota_ingreso": "25%", "financiamiento": "70% < 350 mill / 60% > 350 mill",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Galicia", "tasa_uva": "15,00%",
            "plazo_max": "20 años", "monto_max": "Sin límite de monto", "cuota_ingreso": "25%", "financiamiento": "70%",
            "cuota_10k": 184351, "ingreso_min_10k": 737402
        },
        {
            "nombre": "Banco Provincia (no UVA)", "tasa_uva": "39,20%",
            "plazo_max": "20 años / No clientes 15", "monto_max": "351.250 millones (eq. US$ 250.000)", "cuota_ingreso": "40%", "financiamiento": "80%",
            "cuota_10k": 457189, "ingreso_min_10k": 1142971
        },
        {
            "nombre": "Banco Ciudad", "tasa_uva": "9,5% general / 8,5% microcentro / 7,5% 1ra vivienda",
            "plazo_max": "20 años", "monto_max": "$350 millones / $100 millones para 1ra vivienda", "cuota_ingreso": "25%", "financiamiento": "70% / 75% 1ra vivienda",
            "cuota_10k": 130498, "ingreso_min_10k": 521993
        }
    ]

    print(f"Simulando pedido de USD {prestamo_solicitado_usd} con un sueldo neto de ${sueldo_neto}\n")
    print("-" * 50)

    for banco in bancos:
        # Calculamos los valores totales
        cuota_total = banco["cuota_10k"] * multiplicador
        ingreso_requerido = banco["ingreso_min_10k"] * multiplicador
        
        print(f"BANCO: {banco['nombre']}")
        print(f"Tasa (UVA+): {banco['tasa_uva']} | Plazo Máx: {banco['plazo_max']}")
        print(f"Monto Máximo: {banco['monto_max']} | Financiamiento: {banco['financiamiento']}")
        print(f"Relación Cuota/Ingreso exigida: {banco['cuota_ingreso']}")
        print(f"Cuota mensual calculada: ${cuota_total:,.2f}")
        print(f"Ingreso mínimo que te piden: ${ingreso_requerido:,.2f}")
        
        # Evaluación directa
        if sueldo_neto >= ingreso_requerido:
            print("ESTADO: APROBADO")
            print("Justificación: Tu sueldo supera el mínimo requerido. La cuota no excede el porcentaje máximo permitido de tus ingresos.")
        else:
            print("ESTADO: RECHAZADO")
            print(f"Justificación: Te faltan ${ingreso_requerido - sueldo_neto:,.2f} de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del {banco['cuota_ingreso']} del sueldo.")
        print("-" * 50)

simular_credito()Simulando pedido de USD 120000 con un sueldo neto de $3157380

--------------------------------------------------
BANCO: Banco de Neuquén
Tasa (UVA+): 3,5%/8,5% clientes / 4,5%/9,5% no clientes | Plazo Máx: 20 años
Monto Máximo: 75 millones / 150 millones | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 30%
Cuota mensual calculada: $974,328.00
Ingreso mínimo que te piden: $3,247,776.00
ESTADO: RECHAZADO
Justificación: Te faltan $90,396.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 30% del sueldo. 
--------------------------------------------------
BANCO: Banco de Rosario
Tasa (UVA+): 4,20% | Plazo Máx: 20 años
Monto Máximo: $100 millones | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,035,840.00
Ingreso mínimo que te piden: $4,143,360.00
ESTADO: RECHAZADO
Justificación: Te faltan $985,980.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco Nación
Tasa (UVA+): 6,00% (12,00% No clientes) | Plazo Máx: 30 años
Monto Máximo: 260.000 UVAs | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,007,244.00
Ingreso mínimo que te piden: $4,028,976.00
ESTADO: RECHAZADO
Justificación: Te faltan $871,596.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: ICBC
Tasa (UVA+): 6,90% (9,90% No clientes) | Plazo Máx: 20 años
Monto Máximo: $360 millones | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,292,436.00
Ingreso mínimo que te piden: $5,169,744.00
ESTADO: RECHAZADO
Justificación: Te faltan $2,012,364.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: BBVA
Tasa (UVA+): 7,50% (17,00% No clientes) | Plazo Máx: 30 años
Monto Máximo: Sin límite de monto | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,174,680.00
Ingreso mínimo que te piden: $4,698,720.00
ESTADO: RECHAZADO
Justificación: Te faltan $1,541,340.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco de Córdoba
Tasa (UVA+): 8,90% (9,90% No clientes) | Plazo Máx: 20 años
Monto Máximo: 250.000 UVAs | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,500,756.00
Ingreso mínimo que te piden: $6,003,012.00
ESTADO: RECHAZADO
Justificación: Te faltan $2,845,632.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco Del Sol
Tasa (UVA+): 9,00% | Plazo Máx: 20 años
Monto Máximo: Sin límite de monto | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,511,544.00
Ingreso mínimo que te piden: $6,046,164.00
ESTADO: RECHAZADO
Justificación: Te faltan $2,888,784.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Santander
Tasa (UVA+): 9,50% | Plazo Máx: 20 años
Monto Máximo: Sin límite de monto | Financiamiento: 70%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,565,976.00
Ingreso mínimo que te piden: $6,263,916.00
ESTADO: RECHAZADO
Justificación: Te faltan $3,106,536.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Grupo Petersen
Tasa (UVA+): 9,90% | Plazo Máx: 20 años
Monto Máximo: 315.184 millones | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 30%
Cuota mensual calculada: $1,610,124.00
Ingreso mínimo que te piden: $6,440,484.00
ESTADO: RECHAZADO
Justificación: Te faltan $3,283,104.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 30% del sueldo.
--------------------------------------------------
BANCO: Banco de Chubut
Tasa (UVA+): 10,00% | Plazo Máx: 15 años
Monto Máximo: 180 millones | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 30%
Cuota mensual calculada: $1,805,340.00
Ingreso mínimo que te piden: $7,221,348.00
ESTADO: RECHAZADO
Justificación: Te faltan $4,063,968.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 30% del sueldo.
--------------------------------------------------
BANCO: Comafi
Tasa (UVA+): 10,50% (12,50% No clientes) | Plazo Máx: 20 años
Monto Máximo: 350 millones | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,677,276.00
Ingreso mínimo que te piden: $6,709,116.00
ESTADO: RECHAZADO
Justificación: Te faltan $3,551,736.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Macro (en US$)
Tasa (UVA+): 11,5% (exclusivo Macro Selecta) | Plazo Máx: 5 años
Monto Máximo: Hasta US$ 1 millón | Financiamiento: 50%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $2,362,008.00
Ingreso mínimo que te piden: $9,448,008.00
ESTADO: RECHAZADO
Justificación: Te faltan $6,290,628.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Brubank
Tasa (UVA+): 12,00% (14,00% No clientes) | Plazo Máx: 30 años
Monto Máximo: 250 millones | Financiamiento: 70%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,728,072.00
Ingreso mínimo que te piden: $6,912,276.00
ESTADO: RECHAZADO
Justificación: Te faltan $3,754,896.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco de Corrientes
Tasa (UVA+): 12,00% | Plazo Máx: 20 años
Monto Máximo: No informa | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,849,824.00
Ingreso mínimo que te piden: $7,399,296.00
ESTADO: RECHAZADO
Justificación: Te faltan $4,241,916.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Credicoop
Tasa (UVA+): 12,50% (13,50% No clientes) | Plazo Máx: 20 años
Monto Máximo: 200 millones | Financiamiento: 70%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,908,720.00
Ingreso mínimo que te piden: $7,634,868.00
ESTADO: RECHAZADO
Justificación: Te faltan $4,477,488.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Patagonia
Tasa (UVA+): 12,50% | Plazo Máx: 30 años
Monto Máximo: 120 millones | Financiamiento: 75%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,792,992.00
Ingreso mínimo que te piden: $7,171,968.00
ESTADO: RECHAZADO
Justificación: Te faltan $4,014,588.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco Hipotecario
Tasa (UVA+): 12,50% | Plazo Máx: 15 años
Monto Máximo: $250 millones | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 20%
Cuota mensual calculada: $2,070,636.00
Ingreso mínimo que te piden: $10,353,180.00
ESTADO: RECHAZADO
Justificación: Te faltan $7,195,800.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 20% del sueldo.
--------------------------------------------------
BANCO: Supervielle
Tasa (UVA+): 15,00% | Plazo Máx: 15 años
Monto Máximo: Sin límite de monto | Financiamiento: 65%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $2,351,304.00
Ingreso mínimo que te piden: $9,405,228.00
ESTADO: RECHAZADO
Justificación: Te faltan $6,247,848.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Macro
Tasa (UVA+): 15,00% | Plazo Máx: 20 años
Monto Máximo: Hasta $350 millones | Financiamiento: 70% < 350 mill / 60% > 350 mill
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $2,212,212.00
Ingreso mínimo que te piden: $8,848,824.00
ESTADO: RECHAZADO
Justificación: Te faltan $5,691,444.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Galicia
Tasa (UVA+): 15,00% | Plazo Máx: 20 años
Monto Máximo: Sin límite de monto | Financiamiento: 70%
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $2,212,212.00
Ingreso mínimo que te piden: $8,848,824.00
ESTADO: RECHAZADO
Justificación: Te faltan $5,691,444.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------
BANCO: Banco Provincia (no UVA)
Tasa (UVA+): 39,20% | Plazo Máx: 20 años / No clientes 15
Monto Máximo: 351.250 millones (eq. US$ 250.000) | Financiamiento: 80%
Relación Cuota/Ingreso exigida: 40%
Cuota mensual calculada: $5,486,268.00
Ingreso mínimo que te piden: $13,715,652.00
ESTADO: RECHAZADO
Justificación: Te faltan $10,558,272.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 40% del sueldo.
--------------------------------------------------
BANCO: Banco Ciudad
Tasa (UVA+): 9,5% general / 8,5% microcentro / 7,5% 1ra vivienda | Plazo Máx: 20 años
Monto Máximo: $350 millones / $100 millones para 1ra vivienda | Financiamiento: 70% / 75% 1ra vivienda
Relación Cuota/Ingreso exigida: 25%
Cuota mensual calculada: $1,565,976.00
Ingreso mínimo que te piden: $6,263,916.00
ESTADO: RECHAZADO
Justificación: Te faltan $3,106,536.00 de sueldo para calificar. El banco exige ganar más plata para que la cuota no te coma más del 25% del sueldo.
--------------------------------------------------

               ✨ Yamy la mejor ❤️ ✨
print("\n" + " " * 15 + "✨ Yamy la mejor ❤️ ✨")
