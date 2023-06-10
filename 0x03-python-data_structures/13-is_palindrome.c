#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
* is_palindrome - this function checks if a singly linked list is a Palindrome
* @head: The given head of the singly linked list
* Return:returns 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *first = NULL, *last = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	first = *head;
	len = listint_len(first);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	last = *head;

	for (; i < len_cyc; i = i + 2)
	{
	if (first[i].n != last[len_list].n)
		return (0);

	len_list = len_list - 2;
	}
	return (1);
}

/**
  * get_nodeint_at_index - this fuction gets a given node from a linked list
  * @head: The given head of the linked list
  * @index: the given index to find in the linked list
  * Return: it returns the specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *now = head;
	unsigned int inter_times = 0;

	if (head)
	{
		while (now != NULL)
		{
			if (inter_times == index)
				return (now);

			now = now->next;
			++inter_times;
		}
	}

	return (NULL);
}

/**
  * slistint_len - this function counts the number of elements in a linked list
  * @h: the given linked list to count
  * Return: it returns then number of elements in the linked list
  */
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		++len;
		h = h->next;
	}

	return (len);
}
