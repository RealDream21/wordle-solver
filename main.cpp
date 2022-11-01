#include <iostream>
#include <fstream>
#include <cstring>
//testing branch wtf
using namespace std;

ifstream fin("wordlist.in");
ofstream fout("occurance.out");

//0 for wron
//1 for got word right but not position
//2 for word right, position right
//calculate some sort of accuracy index

const int N = 11453; //N = nr de cuvinte
char dic[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

struct wordType{
    float indice = 0;
    char lit;
    char s[6];
}word[12000];

struct lit{
    int ap = 0;
    char lit;
}l[30];

void indice(wordType &text)
{
    float sum = 0;
    for(int r = 0; r <= N; r++)
    {
        char deGhicit[6];
        strcpy(deGhicit, word[r].s);
        for (int i = 0; i < 5; i++)
        {
            if(deGhicit[i] == text.s[i])
            {
                sum += 2;
                deGhicit[i] = '0';
            }
            else if (strchr(deGhicit, text.s[i])) sum += 1;
        }
    }
    text.indice = sum;
    return ;
}

void letter_count(wordType &text)
{
    int k = 0;
    for(int i = 0; i < strlen(text.s); i++)
    {
        if(strchr(dic, text.s[i]))
            l[strlen(dic) - strlen(strchr(dic, text.s[i]))].ap++;
            l[strlen(dic) - strlen(strchr(dic, text.s[i]))].lit = dic[strlen(dic) - strlen(strchr(dic, text.s[i]))];
    }
    for(int i = 0; i < 30; i++)
        for(int j = i + 1; j <= 30; j++)
            if(l[j].ap > l[i].ap) swap(l[i], l[j]);
    cout << l[0].lit;
    text.lit = l[0].lit;
    return;
}

int main()
{
    for(int i = 0; i <= N; i++)
        fin >> word[i].s;

    int maxim = 0, imax = 0;
    for(int i = 0; i <= N; i++)
    {
        indice(word[i]);
        if (word[i].indice > maxim)
        {
            imax = i;
            maxim = word[i].indice;
        }
    }
    cout << word[imax].s;
    return 0;
}
