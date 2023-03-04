#include <iostream>
using namespace std;

// Stałe

// Wartości początkowe
const int x_0 = 1;
const float x_1 = 1/3;

// Wspłóczynniki w zależności rekurencyjnej
const int a = 3;
const int b = -10;
const int c = 3;
const int d = 0;

// Wartość parametru k
const int k = 45;


// Funkcje
void rekurencjaPrzod(float x_k_1, float x_k, int k, int max_k) {
    float solution = (10*x_k-3*x_k_1)/3;
    if (k == max_k) {
        cout << "x_k: " << x_k << endl << "x_k+1: " << solution << endl;
    }
    else return rekurencjaPrzod(x_k, solution, k+1, max_k);
}

void rekurencjaPrzodDouble(long double x_k_1, long double x_k, int k, int max_k) {
    long double solution = (10*x_k-3*x_k_1)/3;
    if (k == max_k) {
        cout << "x_k: " << x_k << endl << "x_k+1: " << solution << endl;
    }
    else return rekurencjaPrzodDouble(x_k, solution, k+1, max_k);
}

// Main
int main() {
    rekurencjaPrzod(x_0, x_1, 1, k);
    rekurencjaPrzodDouble(x_0, x_1, 1, k);
    cout << "Hello, World!" << endl;
    return 0;
}