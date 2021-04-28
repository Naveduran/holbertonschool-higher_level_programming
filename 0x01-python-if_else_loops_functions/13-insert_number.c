#include "lists.h"

/**
 * insert_node - ..
 * @head: ..
 * @number: ..
 * Return:..
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = (*head)->next->next->next->next->next;
	(*head)->next->next->next->next->next = new;
	new->n = number;
	return (new);
}
