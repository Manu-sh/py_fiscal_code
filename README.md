## py_fiscal_code :id: :it:
simple script to calculate fiscal code (Italy)

#### Disclaimer

data la natura dei dati non mi è stato possibile fare test approfonditi, mancano inoltre eventuali codici catastali per stati/comuni esteri, ovvero lo script da per scontato che si sia nati in Italia. 

Sempre per quanto riguarda i comuni/codici catastali non contempla possibili riassegnazioni dei codici stessi che potrebbero essere avvenute nel corso della storia. es, se nel 1960 il codice D600 era assegnato a un comune oggi soppresso ed è stato riassegnato ed edge case del genere; Si limita a cercare nel dataset dell'agenzia delle entrate aggiornato al 2024 il match con il comune inserito via CLI. L'euristica per la ricerca è anch'essa abbastanza triviale perché dà per scontato che vi sia un'unico match Es. se per assurdo esistesse un comune "Firenzese" oltre a "Firenze" darebbe sicuramente errore inserendo "Firenze" come pattern perché Firenze è sottostringa di entrambi e quella che viene fatta è una ricerca per sottostringa.

- https://it.wikipedia.org/wiki/Codice_fiscale
- https://www.agenziaentrate.gov.it/portale/documents/20143/448357/T4_codicicatastali_comuni_17_01_2024.xlsx/6f942b12-2397-b59a-2a90-1d4bf1a1b8ff

###### Copyright © 2026, [Manu-sh](https://github.com/Manu-sh), s3gmentationfault@gmail.com. Released under the [MIT license](LICENSE).
