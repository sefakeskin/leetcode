#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);

    char **new_list = (char **)malloc(numRows * sizeof(char *));
    for (int i = 0; i < numRows; i++) {
        new_list[i] = (char *)calloc(len, sizeof(char));
    }

    int flag = 1;
    int k = 0;
    for (int i = 0; k < len && i < len; i++) {
        if (flag) {
            for (int j = 0; j < numRows && k < len; j++) {
                new_list[j][i] = s[k++];
            }
            flag = 0;
        } else {
            for (int j = numRows - 2; j > 0 && k < len; j--) {
                new_list[j][i] = s[k++];
                i++;
            }
            flag = 1;
            i--;
        }
    }


    char *new_sentence = (char *)malloc((len + 1) * sizeof(char));
    int t = 0;
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < len; j++) {
            if (new_list[i][j] != '\0') {
                new_sentence[t++] = new_list[i][j];
            }
        }
    }
    new_sentence[t] = '\0';

    for (int i = 0; i < numRows; i++) free(new_list[i]);
    free(new_list);

    return new_sentence;
}
