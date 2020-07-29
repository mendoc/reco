package main

import (
	"bufio"
	"crypto/sha1"
	"encoding/hex"
	"fmt"
	"io"
	"os"
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

func main() {

	now := time.Now()
	msec := now.Unix()

	var version int = 1
	var taille int = 0
	var nbu int = 0
	var filename string = os.Args[0]

	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

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
	_, e = m.WriteString(":")
	check(e)
	_, errHash := m.Write(hash)
	check(errHash)

	// Écriture du nombre de bits à 1
	_, e = m.WriteString(":")
	check(e)
	_, e = m.Write(intToByteArray(nbu))
	check(e)

	// Écriture de la taille du fichier
	_, e = m.WriteString(":")
	check(e)
	_, e = m.Write(intToByteArray(taille))
	check(e)

	// Écriture du nom du fichier
	_, e = m.WriteString(":")
	check(e)
	_, e = m.WriteString(filename)
	check(e)

	m.Sync()
	m.Close()

	// Résumé
	fmt.Println("\n version:", version)
	fmt.Println("   SHA-1:", hex.EncodeToString(hash))
	fmt.Printf("     nbu: %d (0x%x)\n", nbu, nbu)
	fmt.Printf("  taille: %d (0x%x)\n", taille, taille)
	fmt.Println("     nom:", filename)

	fmt.Println("\nTemps d'exécution:", (time.Now().Unix() - msec), "s")
}
