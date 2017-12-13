#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "BST.h"


void freeNode(Node **aim) {
    free((*aim)->word);
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

        free((*aim)->word);
        (*aim)->word = strdup((*aim2)->word);
        (*aim)->count = (*aim2)->count;

        delete(aim2);
    }
}

void increase(Node **node, const char *w) {
    if ((*node) == NULL) {
        *node = (Node*) malloc(sizeof(Node));
        

        (*node)->word = strdup(w);
        (*node)->count = 1;
        (*node)->left_node = NULL;
        (*node)->right_node = NULL;
    } else {
        (*node)->count ++;
    }
}

void decrease(Node **node) {
    if ((*node) != NULL) {
        (*node)->count --;

        if ((*node)->count == 0) {
            delete(node);
        }
    }
}

Node **find(Node **node, const char *w) {
    if (node == NULL) return NULL;

    int res;

    if ((*node) == NULL || (res = strcmp(w, (*node)->word)) == 0) {
        return node;
    } else if (res > 0) {
        return find( &((*node)->right_node), w );
    } else if (res < 0) {
        return find( &((*node)->left_node), w );
    }
}


// Interface
void add(Node **node, const char *w) {
    Node **aim = find(node, w);

    increase(aim, w);
}

void min(Node **node, const char *w)  {
    Node **aim = find(node, w);
    
    decrease(aim);
}

void preorder(Node *node) {
    if(node == NULL) return;

    printf("%s %d\n", node->word, node->count);
    inorder(node->left_node);
    inorder(node->right_node);
}

void inorder(Node *node) {
    if(node == NULL) return;

    inorder(node->left_node);
    printf("%s %d\n", node->word, node->count);
    inorder(node->right_node);
}

void posorder(Node *node) {
    if(node == NULL) return;

    inorder(node->left_node);
    inorder(node->right_node);
    printf("%s %d\n", node->word, node->count);
}
