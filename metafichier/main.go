package main

import (
	"bufio"
	"crypto/sha1"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func intToByteArray(number int) []byte {

	snumber := fmt.Sprintf("%x", number)
	if len(snumber)%2 != 0 {
		snumber = "0" + snumber
	}

	x, e := hex.DecodeString(snumber)
	check(e)
	return x
}

func buildMetafichier(filename string) {
	var version int = 1
	var taille int = 0
	var nbu int = 0
	var sep []byte = []byte{31}

	fmt.Println("Génération du métafichier ...")

	// Ouverture d'un fichier
	f, e := os.Open(filename)
	check(e)

	h := sha1.New()

	r := bufio.NewReader(f)
	b := make([]byte, 512)
	for {
		n, err := r.Read(b)
		if err != nil {
			if err != io.EOF {
				fmt.Println("Error reading file:", err)
			}
			break
		}

		for i := 0; i < n; i++ {
			st := fmt.Sprintf("%b", b[i])
			nbu += len(strings.Replace(st, "0", "", -1))
		}
		taille += n
		h.Write(b[0:n])
	}

	hash := h.Sum(nil)[:20]

	f.Close()

	/* ########   Création du métafichier   ######## */

	metafichierPath := filename + ".reco"

	m, e := os.Create(metafichierPath)
	check(e)

	// Écriture de la version de reco
	_, e = m.Write(intToByteArray(version))
	check(e)

	// Écriture du hash
	_, errHash := m.Write(hash)
	check(errHash)

	// Écriture du nombre de bits à 1
	check(e)
	_, e = m.Write(intToByteArray(nbu))
	check(e)

	// Écriture du nom du fichier
	_, e = m.Write(sep)
	check(e)
	_, e = m.WriteString(filename)
	check(e)

	// Écriture de la taille du fichier
	_, e = m.Write(sep)
	check(e)
	_, e = m.Write(intToByteArray(taille))
	check(e)

	m.Sync()
	m.Close()

	// Résumé
	fmt.Println("\n version:", version)
	fmt.Println("   SHA-1:", hex.EncodeToString(hash))
	fmt.Printf("     nbu: %d (0x%x)\n", nbu, nbu)
	fmt.Printf("  taille: %d (0x%x)\n", taille, taille)
	fmt.Println("     nom:", filename)
}

func extractData(filename string) {

	fmt.Println("Lecture du métafichier ...")

	// Ouverture du metafichier
	m, e := os.Open(filename)
	check(e)

	r := bufio.NewReader(m)

	bVersion, e := r.ReadByte()
	check(e)

	// Récupération de la version utilisée de reco
	version := bVersion

	// Récupération du hash
	bHash := make([]byte, 20)
	_, e = r.Read(bHash)
	check(e)

	// Récupération du nombre de bits à 1
	bNBU, e := r.ReadBytes(31)
	check(e)
	bNBU = bNBU[:len(bNBU)-1]
	nbu, e := strconv.ParseUint(hex.EncodeToString(bNBU), 16, 32)
	check(e)

	// Récupération du nom du fichier
	bNom, e := r.ReadBytes(31)
	bNom = bNom[:len(bNom)-1]
	check(e)

	// Récupération de la taille du fichier
	bTaille, e := r.ReadBytes(31)
	if e != io.EOF {
		check(e)
	}
	taille, e := strconv.ParseUint(hex.EncodeToString(bTaille), 16, 32)
	check(e)

	fmt.Printf("\n version: %x\n", version)
	fmt.Printf("   SHA-1: %s\n", hex.EncodeToString(bHash))
	fmt.Printf("     nbu: %d\n", nbu)
	fmt.Printf("  taille: %d\n", taille)
	fmt.Printf("     nom: %s\n", bNom)
}

func main() {

	now := time.Now()
	msec := now.Unix()

	var filename string = os.Args[0]

	if len(os.Args) == 3 {
		param := os.Args[1]
		if param == "-m" {
			metafichier := os.Args[2]
			extractData(metafichier)
		}
	} else if len(os.Args) == 2 {
		filename = os.Args[1]
		buildMetafichier(filename)
	}

	fmt.Println("\nTemps d'exécution:", (time.Now().Unix() - msec), "s")
}
