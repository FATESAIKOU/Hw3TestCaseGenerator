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

void increase(Node **aim, const char *w);

Node **find(Node **node, const char *w);

// Interface
void add(Node **node, const char *w);

void min(Node **node, const char *w);

void preorder(Node *node);

void inorder(Node *node);

void posorder(Node *node);

#endif
