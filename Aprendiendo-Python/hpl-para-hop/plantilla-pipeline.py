import json

# Estructura del pipeline en formato JSON compatible con Apache Hop (.hpl)
pipeline = {
    "pipeline-meta": {
        "name": "Prueba_SelectValues_Length",
        "description": "Pipeline de prueba para Select Values - Rename y Length",
        "parameters": [],
        "transformations": [
            {
                "name": "Input Excel",
                "type": "ExcelInput",
                "description": "Lee el archivo de ejemplo",
                "id": "ExcelInput",
                "transform": {
                    "filename": "${Internal.Entry.Current.Directory}/Ejemplo_Input_SelectValues.xlsx",
                    "sheetname": "Sheet1",
                    "startrow": "1",
                    "startcol": "0",
                    "fields": [
                        {"name": "Nombre", "type": "String"},
                        {"name": "Apellido", "type": "String"},
                        {"name": "Edad", "type": "Integer"},
                        {"name": "Ciudad", "type": "String"}
                    ]
                },
                "xloc": 100,
                "yloc": 100
            },
            {
                "name": "Select Values",
                "type": "SelectValues",
                "description": "Renombrar y truncar campo",
                "id": "SelectValues",
                "transform": {
                    "fields": [
                        {
                            "name": "Nombre",
                            "rename": "PrimerNombre",
                            "length": "5",
                            "precision": ""
                        }
                    ],
                    "select_unspecified": "Y"
                },
                "xloc": 300,
                "yloc": 100
            },
            {
                "name": "Dummy Output",
                "type": "Dummy",
                "description": "Salida final para inspección",
                "id": "Dummy",
                "xloc": 500,
                "yloc": 100
            }
        ],
        "hops": [
            {"from": "Input Excel", "to": "Select Values", "enabled": "Y"},
            {"from": "Select Values", "to": "Dummy Output", "enabled": "Y"}
        ]
    }
}

# Guardar como archivo .hpl
hpl_path = "/home/server-test/Documentos/Practicante-Practicando/Aprendiendo-Python/hpl-para-hop/Pipeline_Prueba_SelectValues.hpl"
with open(hpl_path, "w", encoding="utf-8") as f:
    json.dump(pipeline, f, indent=2)

hpl_path

