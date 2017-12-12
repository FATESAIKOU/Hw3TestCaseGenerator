#include <stdio.h>
#include <stdlib.h>

#include "BST.h"


void freeNode(Node **aim) {
    free(&(*aim)->word);
    free(*aim);
    *aim = NULL;
}

void delete(Node **aim) {
    Node *tmp_next;

    if ((*aim)->left_node == NULL && (*aim)->right_node == NULL) {
        freeNode(aim);
    } else if ((*aim)->left_node == NULL && (*aim)->right_node != NULL) {
        tmp_next = (*aim)->right_node;
        freeNode(aim);
        *aim = tmp_next;
    } else if ((*aim)->left_node != NULL && (*aim)->right_node == NULL) {
        tmp_next = (*aim)->left_node;
        freeNode(aim);
        *aim = tmp_next;
    } else {
        Node **aim2 = &((*aim)->left_node);
        
        while ((*aim2)->right_node != NULL) {
            aim2 = &((*aim2)->right_node);
        }

        free(&(*aim)->word);
        (*aim)->word = (*aim2)->word;
        (*aim)->count = (*aim2)->count;

        delete(aim2);
    }
}

int main() {

}
