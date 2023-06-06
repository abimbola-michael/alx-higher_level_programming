#include "lists.h"

/**
 * inert_node - a function that inserts a number into a sorted singly linked list
 * @head: linkedlist head
 * @number: number to add to linkedlist
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (temp_node == NULL || temp_node->n >= number)
	{
		new_node->next = temp_node;
		*head = new_node;
		return (new_node);
	}
	while (temp_node && temp_node->next && temp_node->next->n < number)
		temp_node = temp_node->next;
	new_node->next = temp_node->next;
	temp_node->next = new_node;

	return (new_node);
}
