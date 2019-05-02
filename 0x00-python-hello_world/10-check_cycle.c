#include "lists.h"

/**
 * check_cycle - function to check if the linked list has a cycle
 * @list: the list send it
 * Return: return 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *t1 = list;
	listint_t *t2 = list;

	if (list == NULL)
		return (0);

	while (t1->next != NULL && t2->next != NULL && t2->next->next != NULL)
	{
		t1 = t1->next;
		t2 = t2->next->next;

		if (t1->n == t2->n)
			return (1);
	}
	return (0);
}
