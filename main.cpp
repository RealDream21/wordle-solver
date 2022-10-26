#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("wordlist.in");
ofstream fout("occurance.out");


//0 for wron
//1 for got word right but not position
//2 for word right, position right
//calculate some sort of accuracy index

const int N = 11454; //N = nr de cuvinte
char dic[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

struct wordType{
    int cnt = 0;
    char lit = 0;
    char s[6];
}word[12000];

struct lit{
    int ap = 0;
    char lit;
}l[30];

void letter_count(wordType text)
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
    return;
}

int main()
{
    cin.getline(word[0].s, 5);
    letter_count(word[0]);


    return 0;
}
