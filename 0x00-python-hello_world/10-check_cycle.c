#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked
 * list has a cycle in it
 * @list: input linkedlist
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_list = list;
	listint_t *fast_list = list;

	if (!list)
		return (0);

	while (fast_list && slow_list && fast_list->next)
	{
		slow_list = slow_list->next;
		fast_list = fast_list->next->next;
		if (fast_list == slow_list)
			return (1);
	}

	return (0);
}


