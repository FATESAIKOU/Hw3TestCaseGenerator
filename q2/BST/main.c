#include <stdio.h>
#include <stdlib.h>

#include "BST.h"

#define CMD_MAX 1024

int main(int argc, char *argv[]) {
    FILE *fptr = fopen(argv[1], "r");

    char cmd[CMD_MAX];
    Node **bst_root = NULL;


    while (fgets(cmd, CMD_MAX - 1, fptr) != NULL) {
        if (cmd[0] == '+') {
            // add(bst_root, cmd + 1);           
        } else if (cmd[0] == '-') {
            // min(bst_root, cmd + 1);
        }
    }

    /*
    preorder(*bst_root);
    inorder(*bst_root);
    posorder(*bst_root);
    */

    printf("Hello World\n");
    
    return 0;
}
