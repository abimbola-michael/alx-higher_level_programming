#include "hash_tables.h"

/**
 * hash_table_create - a function that creates a hash table.
 * @size:  is the size of the array
 * Return: a pointer to the newly created hash table of NULL
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hasht;
	unsigned long int i;

	hasht = malloc(sizeof(hash_table_t));

	if (hasht == NULL)
		return (NULL);

	hasht->size = size;
	hasht->array = malloc(sizeof(hash_table_t *) * size);

	if (hasht->array == NULL)
		return (NULL);

	for (i = 0; i < size; i++)
	{
		hasht->array[i] = NULL;
	}

	return (hasht);
}
