# Stvari, ki smo jih ugotovili, v prvih dneh uporabe kolaborativne robotske roke ABB GoFa CRB 15000

## Dan #1

Ko smo si podrobneje ogledali robotsko roko, nam je v oči padlo, da je SICK PLOC2D kamera vključena v `WAN` prilljuček na kontrolerju, kasneje smo izvedeli, da je to pravilno, saj je to industrijska naprava in industrijska logika deluje drugače


OmniCore Controller poganja Microwave-ov Windows 10, to ugotovimo precej hitro, če na ABB FlexPendant priključimo tipkovnico, in stisnemo kombinacijo tipk `Win + L` <br>
Prikaže se nam Windows prijavno okno, kjer vidimo 2 uporabnika; privzetega uporabnika, imenovanega `FlexPendant` in administratorskega uporabnika, imenovanega `FlexPendantAdmin`, tu smo naleteli na prvo težavo, administratorski račun, je zaščiten z geslom, katerega se je možno poiskati na internetu. <br>
Vsem upraviteljem ABB robotske roke, svetujemo menjavo tega gesla. <br>

V administratorskem računu, najdemo vsem poznano Windows 10 okolje, iz katerega je bila odstranjena vsa nepotrebna programska oprema <br>
Priporočamo, da se v administratorskem računu ustvari tudi golo kovinska varnostna kopija, podrobna navodila, kako se jo naredi, najdete [tukaj](https://www.windowscentral.com/how-make-full-backup-windows-10)

## Dan #2



***
# Zj pa actually po poglavjih

## 1. Začetek
### 1.0 Pred prvim zagonom
#### 1.0.1 Priprava

Pred prvim zagonom robotske roke, je priporočljivo prebrati vso uradno ABB dokumentacijo, predvsem pa poglavje o varnosti pri delu z robotsko roko.

preveriti, če so vsi kabli pravilno priključeni.
V krmilno enoto `OmniCore` ima več priljučkov. Kaj mora biti priključeno kam, najdete v spodnji tabeli
| Priključek | Opis |
|---|---|
| X0 | Napajalni kabel |
| X1 | Robotska roka |
| X2 | Zunanji I/O priključki |
| X4 | Nadzorna plošča `FlexPendant` |
| WAN | Komunikacija s kamero |

Ko smo preverili, da so vsi kabli pravilno priključeni na `OmniCore` krmilno enoto, lahko nadaljujemo s prižigom robota

### 1.1 Prvi zagon
Robotsko roko zaženemo tako, da napajalni kabel vključimo v električno omrežje in prižgemo stikalo `Q0` na `OmniCore` krmilniku. Na nadzorni plošči `FlexPendant` se bo pojavil `ABB`logo. Počakamo