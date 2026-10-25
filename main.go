package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Producto struct {
	ID        string `json:"id"`
	Nombre    string `json:"nombre"`
	Estado    string `json:"estado"`
	Ubicacion string `json:"ubicacion"`
}

type Bloque struct {
	Indice       int
	Timestamp    string
	Datos        Producto
	HashAnterior string
	Hash         string
}

var Blockchain []Bloque

func CrearBloque(datos Producto, hashAnterior string) Bloque {
	var nuevoBloque Bloque
	nuevoBloque.Indice = len(Blockchain) + 1
	nuevoBloque.Timestamp = time.Now().String()
	nuevoBloque.Datos = datos
	nuevoBloque.HashAnterior = hashAnterior
	nuevoBloque.Hash = fmt.Sprintf("HASH_SIMULADO_%d", nuevoBloque.Indice)
	return nuevoBloque
}

func RegistrarProducto(id string, nombre string, ubicacion string) {
	producto := Producto{ID: id, Nombre: nombre, Estado: "Manufacturado", Ubicacion: ubicacion}

	hashAnterior := "0"
	if len(Blockchain) > 0 {
		hashAnterior = Blockchain[len(Blockchain)-1].Hash
	}

	nuevoBloque := CrearBloque(producto, hashAnterior)
	Blockchain = append(Blockchain, nuevoBloque)

	fmt.Printf("Bloque %d agregado exitosamente a la Blockchain comercial\n", nuevoBloque.Indice)
	productoJSON, _ := json.MarshalIndent(producto, "", "  ")
	fmt.Println(string(productoJSON))
	fmt.Println("--------------------------------------------------")
}

func main() {
	fmt.Println("=== INICIANDO REGISTRO DE CADENA DE SUMINISTRO EN BLOCKCHAIN ===")
	fmt.Println("")

	RegistrarProducto("PROD001", "Vacuna Temperatura Critica", "Almacen Central")
	time.Sleep(1 * time.Second)
	RegistrarProducto("PROD002", "Medicamento Especializado", "Zona de Carga Aeropuerto")
}
