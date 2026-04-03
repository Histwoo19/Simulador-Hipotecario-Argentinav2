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