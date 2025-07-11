#include <stdio.h>

// Esta função lê um número double do terminal de forma robusta
// e o retorna. É a nossa substituta para o scanf direto.
double read_double() {
    double val;
    scanf(" %lf", &val);
    return val;
}