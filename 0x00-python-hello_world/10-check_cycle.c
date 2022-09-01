#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check for a cycle in a list
 * @list - pointer to a singly linked list
 *
 * Return: 0 if cycle does not exist 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *lead;
	listint_t *inspector;

	lead = list;
	inspector = list;
	while (lead && lead->next && inspector)
	{
		lead = lead->next->next;
		inspector = inspector->next;
		if (lead == inspector)
			return (1);
	}
	return (0);
}
