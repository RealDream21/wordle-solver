# wordle solver

Nume echipa: Multiplexorii

GRUPA:134

Membri: Stancila Ionut-Marian
        Florete Fabian-Andrei
        Iacovita Cristian-Alexandru
        Radu Alexandru-Mihail

versiunea de python folosita: Python 3.11

Pentru rularea programului exista 2 cazuri:
1) Rularea de pe Windows, ce se realizeaza direct prin pornirea start.bat
2) Rularea de pe Linux, caz in care trebuie deschise individual, in aceasta ordine: feedback.py si entropy.py

Cel mai bun cuvant de inceput este: TAREI, avand entropia de: 6.413805505806504

Numarul mediu de incercari pentru ghicirea unui cuvant: 4.374017810371923. O simulare a unui joc pentru fiecare cuvant se afla in fisierul solutii.txt

Am folosit entropia pentru a rezolva cerinta proiectului.

Pentru a calcula entropia am luat fiecare cuvant si am parcurs lista de cuvinte (cuvinte ramase din parcurgerea anterioara)
O parcurgere inseamna calcularea frecventei templateurilor aparute pentru fiecare cuvant astfel: 
->se considera cuvantul pentru care se calculeaza entropia drept input,
->se parcurge lista de cuvinte si se considera cuvintele din lista drept cuvantul care trebuie ghicit. 
->In urma feedbackului primit, crestem frecventa templateului (feedbackului) respectiv, unde un template e de forma XXXXX (unde X poate lua valoarea 0, 1 sau 2 in functie de cuvantul care trebuie ghicit, unde 0 inseamna ca litera nu e in cuvant, 1 = litera e pe alta pozitie in cuvant, 2 = litera e pe pozitia respectiva in cuvant). 
->Calculam entropia prin formula suma(p(i)*log(1/p(i))) unde p(i)=frecventa template/cuv ramase in lista iar i parcurge toate templateurile specifice inputului nostru.

De asemenea, am lasat folderul "Ciorne" pentru a se vedea progresul proiectului. Folderul "Ciorne" contine toate incercarile noastre de a calcula entropia, a face server, si calculul entropiei pentru feedbackul corect (nu cel cu "buggy behaviour"). 

Video-uri ce ne-au ajutat in dezvoltarea proiectului:
a) https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown
b) https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim
