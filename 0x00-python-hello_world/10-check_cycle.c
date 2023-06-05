#include "lists.h"

/**
*check_cycle-this function checks,if a singly linked list has
* a cycle or is cyclic
* @list: this is a pointer to the beginning of the relevant node
* Return: it returns 0 if no present cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *curr, *checked;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	checked = curr->next;

	while (curr != NULL && checked->next != NULL
		&& checked->next->next != NULL)
	{
		if (curr == checked)
			return (1);
		curr = curr->next;
		checked = checked->next->next;
	}
	return (0);
}

