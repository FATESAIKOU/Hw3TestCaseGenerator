#include <stdio.h>
#include <stdlib.h>

#ifndef BST_INCLUDED
#define BST_INCLUDED

typedef struct _Node {
    char *word;
    int count;
    struct _Node *left_node;
    struct _Node *right_node;
} Node;

void freeNode(Node **aim);

void deleteNode(Node **aim);

void add(Node *root, const char *w);

void min(Node *root, const char *w);

void preorder(Node *root);

void inorder(Node *root);

void posorder(Node *root);

#endif
