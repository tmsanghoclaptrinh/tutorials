// Tham khảo code từ @bobamilktea

#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <chrono>

using namespace std;
using namespace std::chrono;

steady_clock::time_point tstart;
steady_clock::time_point tend;

void time_start()
{
    tstart = std::chrono::steady_clock::now();
}

void time_end()
{
    tend = std::chrono::steady_clock::now();
}

void time_elapsed()
{
    cout << duration_cast<std::chrono::milliseconds>(tend - tstart).count() << "ms";
}

int ReadInt()
{
    char ch;
    do
        ch = getchar();
    while (ch != '-' && ch != '+' && (ch < '0' || ch > '9'));
    int sign;
    ch == '-' ? sign = -1 : sign = 1;
    int res = (ch >= '0' && ch <= '9') ? ch - '0' : 0;
    ch = getchar();
    while (ch >= '0' && ch <= '9')
        res = res * 10 + ch - '0',
        ch = getchar();
    return res * sign;
}

int main()
{
    // 1. Fast I/O
    ios_base::sync_with_stdio(false);
    time_start();
    if (true)
    {
        freopen("input.txt", "r", stdin);
        int v;
        for (int i = 0; i < 10000000; i++)
            v = ReadInt();
    }
    fclose(stdin);
    time_end();
    cout << "\"Fast I/O\": ";
    time_elapsed();
    cout << endl;

    // 2. C scanf
    time_start();
    if (true)
    {
        FILE *fin = fopen("input.txt", "r");
        int v;
        while (fscanf(fin, "%d", &v) != EOF);
        fclose(fin);
    }
    time_end();
    cout << "C scanf: ";
    time_elapsed();
    cout << endl;

    // 3. C++ input stream
    time_start();
    if (true)
    {
        ifstream fin("input.txt");
        int v;
        while (fin >> v);
    }
    time_end();
    cout << "C++ input stream: ";
    time_elapsed();

    return 0;
}
