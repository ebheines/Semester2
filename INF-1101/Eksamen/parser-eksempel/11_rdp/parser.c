

#include "printing.h"
#include "plot.h"

/*

Grammar:

<expr>   ::= <term> | <term> ('+'|'-') <expr>
<term>   ::= <factor> | <factor> ('*'|'/') <term>
<factor> ::= <number> | '(' <expr> ')'
<number> ::= <sequence of digits 0-9>

*/


typedef enum 
{
	NUM, ADD, SUB, MUL, DIV
} node_type;


typedef struct context context_t;
struct context
{
    char *input;
    char *p;
};


typedef struct node node_t;
struct node
{
    int value;
    node_type type;
    node_t *left;
    node_t *right;
};




// Forward declarations
static node_t *parse_expr(context_t *context);
static node_t *parse_term(context_t *context);
static node_t *parse_factor(context_t *context);
static node_t *parse_number(context_t *context);


static node_t *newnode(node_type type, int value, node_t *left, node_t *right) 
{
    node_t *node = (node_t *)calloc(1, sizeof(node_t));
    if (node == NULL)
    {
        ERROR_PRINT("Could not allocate space for node\n");
    }

    node->type = type;
    node->value = value;
    node->left = left;
    node->right = right;

    return node;

}

static void skipwhitespace(context_t *context) 
{
    while (context->p[0] == ' ')
    {
        context->p++;
    }
}

node_t *parse_expr(context_t *context)
{
    node_t *t2, *t1 = parse_term(context);

    if (context->p[0] == '+')
    {
        context->p++;
        t2 = parse_expr(context);
        return newnode(ADD, 0, t1, t2);
    }
    else if (context->p[0] == '-')
    {
        context->p++;
        t2 = parse_expr(context);
        return newnode(SUB, 0, t1, t2);
    }
    return t1;
}

node_t *parse_term(context_t *context)
{
    node_t *f2, *f1 = parse_factor(context);

    if (context->p[0] == '*')
    {
        context->p++;
        f2 = parse_term(context);
        return newnode(MUL, 0, f1, f2);
    }
    else if (context->p[0] == '/')
    {
        context->p++;
        f2 = parse_term(context);
        return newnode(DIV, 0, f1, f2);
    }

    return f1;
}

node_t *parse_factor(context_t *context)
{
    skipwhitespace(context);

    if (context->p[0] == '(')
    {
        node_t *e;
        context->p++;

        e = parse_expr(context);

        skipwhitespace(context);
        if (context->p[0] == ')')
        {
            context->p++;
        }
        else
        {
            ERROR_PRINT("Missing )\n");
        }
        skipwhitespace(context);
        return e;
    }
    else
    {
        return parse_number(context);
    }
}

node_t *parse_number(context_t *context)
{
    char *q;
    int value;

    skipwhitespace(context);
    q = context->p;

    while (*q >= '0' && *q <= '9')
    {
        q++;
    }

    if (context->p == q)
    {
        ERROR_PRINT("Not a number %s\n", context->p);
    }

    value = atoi(context->p);
    context->p = q;
    skipwhitespace(context);

    return newnode(NUM, value, NULL, NULL);
}



static int evaluate(node_t *expr)
{
    int n;

    switch (expr->type)
    {
        case NUM:
            return expr->value;

        case MUL:
            return evaluate(expr->left) * evaluate(expr->right);

        case DIV:
            n = evaluate(expr->right);
            if (n == 0)
            {
                ERROR_PRINT("Division by 0\n");
            }
            return evaluate(expr->left) / n;

        case ADD:
            return evaluate(expr->left) + evaluate(expr->right);

        case SUB:
            return evaluate(expr->left) - evaluate(expr->right);
    }

    ERROR_PRINT("Unknown node type\n");
    return 0;
}


node_t *parse(char *input) 
{
    node_t *result;

    context_t context;
    context.input = input;
    context.p = input;

    result = parse_expr(&context);

    if (*context.p)
    {
        ERROR_PRINT("Unparsed input: %s\n", context.p);
    }
    return result;
}

char *strnode(char *name, node_t *n)
{
	switch(n->type) {
		case NUM:
			sprintf(name, "%d", n->value);
			break;
		case MUL:
			sprintf(name, "*");
			break;
		case DIV:
			sprintf(name, "/");
			break;
		case ADD:
			sprintf(name, "+");
			break;
		case SUB:
			sprintf(name, "-");
			break;
	}
	
    return name;
}

void _calc_print(plot_t *plot, node_t *current)
{
    char from[128];
    char to[128];
	
    if (current == NULL)
        return;

    strnode(from, current);
    if (current->left != NULL) {
        plot_addlink2(plot, current, current->left, from, strnode(to, current->left));
    } 
	
    if (current->right != NULL) {
        plot_addlink2(plot, current, current->right, from, strnode(to, current->right));
    } 
    
    _calc_print(plot, current->left);
    _calc_print(plot, current->right);
}

void calc_print(node_t *parse)
{
    plot_t *plot;
    
    plot = plot_create("calc");
    _calc_print(plot, parse);
    plot_doplot(plot);
	plot_cleanup(plot);
}

void cleanup(node_t *node)
{
	if(!node)
		return;
	/* Traverse the tree! */
	cleanup(node->left);
	cleanup(node->right);

	free(node);
}


int main()
{
    char *input = "(2 + 4) * (6/(2+(2+4)))";

    node_t *ast = parse(input);

    calc_print(ast);

    int res = evaluate(ast);
    INFO_PRINT("Evaluated %s = %d\n", input, res);

    cleanup(ast);

    return 0;
}