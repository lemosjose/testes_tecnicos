#include <stdio.h>
#include <string.h>

int main(){
	char inputString[20];
	char stringInvertida[20];
	printf("digite a palavra a ser lida: ");
	int i;
	fgets(inputString, 20, stdin); // NÃO USAR GETS. Perigo de estouro de buffer por array de tamanho determinado anteriormente.
	// -1 para não cair em out of range
	for (i = strlen(inputString) - 1; i >= 0 ; i--){
		printf("%c", inputString[i]);
	}
	return 0; 
}
